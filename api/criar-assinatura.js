// HiMed — cria (ou reaproveita) a assinatura do usuário no Asaas.
// Roda na Vercel. O app chama esta função quando a pessoa clica em "Assinar".
//
// Variáveis de ambiente necessárias na Vercel:
//   ASAAS_API_KEY        -> a chave do Asaas ($aact_...)
//   ASAAS_BASE_URL       -> https://api-sandbox.asaas.com/v3  (teste) | https://api.asaas.com/v3 (produção)
//   SUPABASE_URL         -> https://gcwrggcbjeucbhgvishi.supabase.co
//   SUPABASE_SERVICE_ROLE-> a service_role key do Supabase (secreta)
//   ASSINATURA_VALOR     -> 27.00
//   ASSINATURA_TRIAL_DIAS-> 7

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ erro: "Método não permitido" });

  try {
    const { user_id, email, nome, cpfCnpj, billingType } = req.body || {};
    if (!user_id || !email) return res.status(400).json({ erro: "Faltam dados do usuário." });

    const ASAAS = process.env.ASAAS_BASE_URL;
    const KEY = process.env.ASAAS_API_KEY;
    const VALOR = Number(process.env.ASSINATURA_VALOR || "27.00");
    const TRIAL = Number(process.env.ASSINATURA_TRIAL_DIAS || "7");

    const asaas = (path, opts = {}) =>
      fetch(ASAAS + path, {
        ...opts,
        headers: { "Content-Type": "application/json", access_token: KEY, ...(opts.headers || {}) },
      }).then(async r => ({ ok: r.ok, status: r.status, data: await r.json().catch(() => ({})) }));

    // 1) Cria (ou acha) o cliente no Asaas
    let customerId;
    const busca = await asaas(`/customers?email=${encodeURIComponent(email)}`);
    if (busca.ok && busca.data.data && busca.data.data.length) {
      customerId = busca.data.data[0].id;
    } else {
      const novo = await asaas("/customers", {
        method: "POST",
        body: JSON.stringify({ name: nome || email, email, cpfCnpj: cpfCnpj || undefined }),
      });
      if (!novo.ok) return res.status(400).json({ erro: "Falha ao criar cliente no Asaas", detalhe: novo.data });
      customerId = novo.data.id;
    }

    // 2) Cria a assinatura mensal, com 1ª cobrança daqui a TRIAL dias (7) -> cobra no 8º dia
    const d = new Date();
    d.setDate(d.getDate() + TRIAL);
    const primeiraCobranca = d.toISOString().slice(0, 10); // YYYY-MM-DD

    const sub = await asaas("/subscriptions", {
      method: "POST",
      body: JSON.stringify({
        customer: customerId,
        billingType: billingType || "UNDEFINED", // UNDEFINED deixa o cliente escolher (cartão/pix) no checkout
        value: VALOR,
        nextDueDate: primeiraCobranca,
        cycle: "MONTHLY",
        description: "HiMed — assinatura mensal",
      }),
    });
    if (!sub.ok) return res.status(400).json({ erro: "Falha ao criar assinatura no Asaas", detalhe: sub.data });

    // 3) Guarda no Supabase (via service_role) que este usuário tem essa assinatura (status trial)
    await fetch(`${process.env.SUPABASE_URL}/rest/v1/subscriptions`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        apikey: process.env.SUPABASE_SERVICE_ROLE,
        Authorization: `Bearer ${process.env.SUPABASE_SERVICE_ROLE}`,
        Prefer: "resolution=merge-duplicates",
      },
      body: JSON.stringify({
        user_id, email,
        asaas_customer_id: customerId,
        asaas_subscription_id: sub.data.id,
        status: "trial",
        valor: VALOR,
        proxima_cobranca: primeiraCobranca,
        atualizado_em: new Date().toISOString(),
      }),
    });

    // 4) Devolve o link de pagamento do Asaas para o app abrir
    // (a fatura da assinatura tem uma invoiceUrl gerada; buscamos a 1ª cobrança)
    const pagamentos = await asaas(`/payments?subscription=${sub.data.id}`);
    const invoiceUrl =
      (pagamentos.ok && pagamentos.data.data && pagamentos.data.data[0] && pagamentos.data.data[0].invoiceUrl) || null;

    return res.status(200).json({
      ok: true,
      subscriptionId: sub.data.id,
      invoiceUrl, // o app abre esta URL para a pessoa pagar (cartão ou pix)
    });
  } catch (e) {
    return res.status(500).json({ erro: "Erro interno", detalhe: String(e) });
  }
}
