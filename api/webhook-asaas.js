// HiMed — recebe os avisos do Asaas (webhook) e atualiza o acesso do usuário.
// O Asaas chama esta URL sozinho quando algo acontece com o pagamento.
//
// Variáveis de ambiente necessárias na Vercel:
//   ASAAS_WEBHOOK_TOKEN   -> um segredo que VOCÊ inventa e coloca também no painel do Asaas
//   SUPABASE_URL          -> https://gcwrggcbjeucbhgvishi.supabase.co
//   SUPABASE_SERVICE_ROLE -> a service_role key do Supabase
//   RESEND_API_KEY        -> a chave do Resend (re_...)
//   EMAIL_REMETENTE       -> HiMed <no-reply@himedapp.com.br>

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ erro: "Método não permitido" });

  // 1) Confere o token secreto (o Asaas envia no cabeçalho asaas-access-token)
  const tokenRecebido = req.headers["asaas-access-token"];
  if (process.env.ASAAS_WEBHOOK_TOKEN && tokenRecebido !== process.env.ASAAS_WEBHOOK_TOKEN) {
    return res.status(401).json({ erro: "Token inválido" });
  }

  try {
    const evento = req.body || {};
    const tipo = evento.event;                 // ex: PAYMENT_CONFIRMED, PAYMENT_OVERDUE...
    const pag = evento.payment || {};
    const subId = pag.subscription || null;    // id da assinatura no Asaas

    const SB = process.env.SUPABASE_URL;
    const SR = process.env.SUPABASE_SERVICE_ROLE;
    const sbHeaders = {
      "Content-Type": "application/json",
      apikey: SR,
      Authorization: `Bearer ${SR}`,
    };

    // 2) Registra o evento (auditoria)
    await fetch(`${SB}/rest/v1/payment_events`, {
      method: "POST",
      headers: sbHeaders,
      body: JSON.stringify({
        tipo, asaas_payment_id: pag.id || null, asaas_subscription_id: subId, payload: evento,
      }),
    });

    // 3) Decide o novo status a partir do tipo de evento
    let novoStatus = null;
    if (["PAYMENT_CONFIRMED", "PAYMENT_RECEIVED"].includes(tipo)) novoStatus = "ativo";
    else if (tipo === "PAYMENT_OVERDUE") novoStatus = "atrasado";
    else if (["PAYMENT_DELETED", "PAYMENT_REFUNDED", "SUBSCRIPTION_DELETED"].includes(tipo)) novoStatus = "cancelado";

    // 4) Atualiza a assinatura do usuário (busca pela assinatura do Asaas)
    if (novoStatus && subId) {
      const patch = {
        status: novoStatus,
        atualizado_em: new Date().toISOString(),
      };
      if (pag.dueDate) patch.proxima_cobranca = pag.dueDate;

      const r = await fetch(
        `${SB}/rest/v1/subscriptions?asaas_subscription_id=eq.${encodeURIComponent(subId)}`,
        { method: "PATCH", headers: { ...sbHeaders, Prefer: "return=representation" }, body: JSON.stringify(patch) }
      );
      const linhas = await r.json().catch(() => []);

      // 5) Se virou ATIVO agora, manda email de boas-vindas (Resend)
      if (novoStatus === "ativo" && Array.isArray(linhas) && linhas[0] && linhas[0].email) {
        await enviarEmailAtivado(linhas[0].email);
      }
    }

    // Sempre responde 200 rápido, senão o Asaas fica reenviando
    return res.status(200).json({ ok: true });
  } catch (e) {
    // Mesmo em erro, responde 200 para o Asaas não reenviar infinitamente;
    // o evento fica salvo em payment_events para investigarmos.
    return res.status(200).json({ ok: false, erro: String(e) });
  }
}

async function enviarEmailAtivado(email) {
  try {
    await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${process.env.RESEND_API_KEY}` },
      body: JSON.stringify({
        from: process.env.EMAIL_REMETENTE || "HiMed <no-reply@himedapp.com.br>",
        to: [email],
        subject: "Seu acesso ao HiMed está ativo 🎉",
        html: `
          <h2>Bem-vindo ao HiMed</h2>
          <p>Seu pagamento foi confirmado e seu acesso está liberado.</p>
          <p>É só entrar no app e começar a estudar. Bons estudos!</p>
          <p>Equipe HiMed</p>`,
      }),
    });
  } catch (_) { /* se o email falhar, não quebra o webhook */ }
}
