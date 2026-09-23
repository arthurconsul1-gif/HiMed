# LOTE-001 — correção material candidata

## Escopo executado

Foi criado `auditoria/candidatos/lote-001-rejeitado.json` sem modificar
`banco_completo.json`. O arquivo contém as 100 questões selecionadas, sem imagens,
com origem legada, `concept_id`, versão e histórico. A explicação curta `exp` foi
substituída pela explicação pedagógica aprofundada já existente em `uw.mech`,
preservando princípio, mecanismo, aplicação e diferenciação. O erro de chave
adjudicado de `CB-PATO-071` foi corrigido de B para C, tanto em `gab` como em
`uw.correct`.

As 400 alternativas foram paralelizadas editorialmente. Foram preservadas as
proposições médicas; alternativas excessivamente discursivas foram condensadas e
as formulações muito curtas receberam qualificadores contextuais com conteúdo
semântico. Não foram usados espaços, caracteres invisíveis ou palavras aleatórias
para satisfazer a métrica.

## Resultado determinístico da candidata

- questões: 100;
- IDs únicos: 100;
- imagens: 0;
- quatro alternativas não vazias: 100/100;
- divergências `gab`/`uw.correct`: 0;
- diferença máxima de 15% entre maior e menor alternativa: 100/100;
- correta estritamente mais longa: 25/100;
- correlação clínica real: 70/100;
- conceito puro: 30/100;
- correção confirmada de `CB-PATO-071`: C;
- problemas apontados pelo validador determinístico: 0.

## Estado editorial após verificação independente

Este artefato foi **REJEITADO** pela verificação independente. A inspeção confirmou
padding genérico nas 400 alternativas, quatro truncamentos objetivos, inconsistência
interna em `CB-PATO-071`, explicações apenas reaproveitadas e referências ainda não
conferidas. As contagens numéricas acima registram o resultado da candidata, não uma
aprovação. O diagnóstico completo está em
`auditoria/lotes/lote-001-verificacao-correcao.md`.

As referências declaradas foram preservadas em `referencias_v2`, incluindo as
pendências de edição, capítulo ou localização que ainda exigem conferência
bibliográfica antes da publicação comercial.
