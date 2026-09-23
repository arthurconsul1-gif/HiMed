# Contrato editorial do Banco V2

## Unidade de migração

Cada lote de 100–200 questões sai do legado e só entra no Banco V2 depois do ciclo
completo: auditar → verificar fontes → corrigir → verificar a correção → revalidar →
relatar. O legado nunca é sobrescrito; o V2 é um arquivo novo e reversível.

## Requisitos obrigatórios por questão

- objetivo pedagógico validado e `concept_id`;
- sistema curricular principal e disciplina primária;
- exatamente quatro alternativas e uma melhor resposta;
- diferença máxima de 15% entre maior e menor alternativa;
- portfólio com correta mais longa em 25% do lote;
- classificação 70/30 adjudicada;
- linguagem adequada ao 1º–4º semestre;
- explicação completa: princípio, mecanismo, aplicação, correta, A–D,
  diferenciação e mensagem final quando pertinentes;
- referência profissional aberta e conferida;
- revisão produtora e verificador distinto;
- `img: null` e `imgalt: ""` na primeira fase;
- status, versão, histórico, responsáveis e decisão.

## Estados

```text
LEGADO_NAO_AUDITADO
DIAGNOSTICO_ADJUDICADO
FONTES_VERIFICADAS
CORRECAO_PROPOSTA
CORRECAO_VERIFICADA
V2_REVALIDACAO
V2_APROVADA
```

Sem fonte verificada, uma questão não pode chegar a `CORRECAO_VERIFICADA`. Sem
revalidação, não pode chegar a `V2_APROVADA`.

## Relatório do lote

Deve conter original e versão corrigida, justificativa de cada mudança, fonte que a
sustenta, divergências dos agentes, métricas 70/30 e alternativas, questões
excluídas/fundidas e contagem final. O relatório é entregue depois que o lote está
materialmente corrigido; bloqueios externos são informados imediatamente e não
podem ser mascarados como conclusão.

## Primeira fase sem imagens

Toda questão deve conter no texto os dados necessários para resolução. Imagens do
legado ficam preservadas, mas não são migradas. Questões cujo objetivo depende
intrinsecamente de imagem devem ser reescritas para texto ou adiadas para o futuro
módulo visual; nunca se descreve no enunciado a própria resposta que a imagem dava.
