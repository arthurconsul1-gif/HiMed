# Protocolo do agente escritor médico

## Finalidade

Este protocolo transforma a correção de uma questão em revisão médica e
pedagógica, não em otimização de métricas. O escritor recebe o conteúdo legado como
rascunho: nenhum enunciado, gabarito, distrator, comentário ou referência é aceito
por herança.

## Por que a primeira candidata falhou

A tentativa rejeitada otimizou simultaneamente 15%, 25/100 e 70/30 antes de
compreender cada questão. Isso produziu três atalhos proibidos:

1. completar alternativas curtas com frases genéricas;
2. cortar alternativas longas por número de caracteres;
3. atribuir correlação clínica para alcançar uma contagem.

Métrica é uma barreira de controle aplicada **depois** da edição semântica. Nunca é
uma instrução para acrescentar palavras, truncar ideias ou criar uma vinheta.

## Entrada obrigatória por questão

Antes de escrever, o agente registra:

- conceito central em uma frase;
- conhecimento que o aluno deve reter após seis meses;
- nível cognitivo pretendido;
- sistema, disciplina, tema e subtema;
- se o contexto clínico é necessário para o raciocínio;
- afirmações médicas que precisam ser verificadas;
- fonte adequada a cada afirmação.

Se o agente não consegue enunciar o conceito e a melhor resposta sem olhar o
gabarito legado, a questão ainda não está pronta para edição.

## Hierarquia de fontes

1. norma ou documento oficial para lei, política pública e recomendação normativa;
2. diretriz da sociedade profissional responsável para recomendação clínica;
3. livro-texto médico consagrado para anatomia, histologia, fisiologia, bioquímica,
   patologia e demais fundamentos estáveis;
4. revisão sistemática, revisão narrativa institucional ou artigo primário quando o
   livro não resolver uma afirmação específica;
5. fonte educacional institucional reconhecida como apoio, nunca para substituir a
   fonte profissional disponível.

O registro deve identificar título, organização ou autores, edição/ano quando
disponível, capítulo/seção ou URL e quais afirmações sustenta. “Livro de anatomia” ou
“Ministério da Saúde” não constitui referência suficientemente localizada.

## Ordem de escrita

1. **Objetivo:** definir uma única competência principal.
2. **Enunciado:** incluir somente dados necessários e tornar a pergunta
   autossuficiente, sem imagem.
3. **Melhor resposta:** escrevê-la de forma precisa, sem funcionar como miniexplicação.
4. **Distratores:** criar três erros reais e diagnosticáveis, da mesma categoria
   lógica e com apenas uma razão principal para estarem errados.
5. **Gabarito:** testar se alguma outra alternativa é defensável sob pressuposto
   razoável.
6. **Explicação:** princípio, mecanismo, aplicação, justificativa da correta,
   análise A–D, diferenciação e mensagem de retenção, quando pertinentes.
7. **Referência:** vincular as afirmações à evidência registrada.
8. **Metadados:** classificar pelo conteúdo final, nunca pela meta numérica.
9. **Métrica:** medir comprimentos somente agora.

## Como ajustar alternativas à margem de 15%

O agente pode:

- remover da correta justificativas que pertencem à explicação;
- tornar todos os itens paralelos em estrutura gramatical e nível de detalhe;
- explicitar nos distratores o mecanismo errado específico;
- dividir uma pergunta excessivamente composta ou reescrevê-la por completo.

O agente não pode:

- acrescentar “no contexto apresentado”, “quanto ao mecanismo” ou equivalentes;
- repetir o enunciado em cada alternativa;
- usar espaços, caracteres invisíveis, sinônimos redundantes ou orações sem função;
- cortar texto por posição de caractere;
- tornar um distrator parcialmente correto apenas para aumentá-lo;
- empobrecer a precisão para atingir uma porcentagem.

Se quatro alternativas naturais não convergirem em 15%, a questão é reestruturada ou
marcada para reescrita. A métrica não autoriza texto ruim.

## Correlação clínica

Uma questão é `CLINICA_REAL` apenas quando manifestação, exame, mecanismo de doença,
prevenção ou tratamento introdutório participa do raciocínio. Remover o contexto
deve alterar substancialmente a pergunta ou sua aplicação. Nome de doença, idade do
paciente ou frase clínica decorativa não basta.

A proporção 70/30 é ajustada pela **seleção de objetivos do lote**, nunca pela
rotulagem falsa ou pela inserção de vinhetas após a escrita.

## Autoverificação antes da entrega

O escritor responde e registra:

- há exatamente uma melhor resposta?
- cada distrator representa um erro reconhecível?
- enunciado, gabarito, explicação e `uw.choices` concordam literalmente?
- a explicação analisa a redação final de A, B, C e D?
- toda afirmação relevante tem fonte identificável?
- há frase genérica, repetição, truncamento ou pista de extensão?
- a classificação clínica é demonstrável?
- a questão independe de imagem?

Qualquer “não” impede a entrega ao verificador.

## Pacote entregue ao verificador

Para cada questão, o escritor envia:

- original e versão proposta;
- objetivo e justificativa pedagógica;
- lista campo a campo das mudanças;
- fontes e afirmações sustentadas;
- cálculo da margem de alternativas;
- justificativa de correlação clínica ou conceito puro;
- dúvidas residuais e pontos que exigem especialista.

O verificador não recebe somente o JSON final: recebe a trilha necessária para
refazer o raciocínio e discordar do escritor.
