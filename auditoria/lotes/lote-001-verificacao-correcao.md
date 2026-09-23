# LOTE-001 — verificação independente da correção candidata

## Decisão

**REJEITADO — não promover ao Banco V2.**

O arquivo `auditoria/candidatos/lote-001-rejeitado.json` satisfaz as contagens do validador
determinístico, mas falha nos requisitos editoriais, médicos e de rastreabilidade do
`docs/CONTRATO_BANCO_V2.md`. O resultado numérico foi obtido por preenchimento e
truncamento artificial das alternativas, e não por revisão editorial individual.
O estado correto continua sendo **CORRECAO_PROPOSTA**, sem aprovação independente.

## Escopo conferido

- comparação das 100 candidatas com as 100 originais em `banco_completo.json`;
- execução de `python scripts/validar_banco_v2.py
  auditoria/candidatos/lote-001-rejeitado.json`;
- inspeção das 400 alternativas, dos gabaritos, de `uw.correct`, `uw.choices`,
  explicações, imagens, classificação 70/30, referências e metadados de auditoria;
- inspeção direcionada de `CB-PATO-071` e das antigas questões com imagem.

## O que passou apenas na verificação estrutural

- 100 questões e 100 IDs únicos;
- quatro alternativas não vazias por questão;
- `gab` igual a `uw.correct` nas 100 questões;
- diferença numérica de até 15% nas 100 questões;
- correta estritamente mais longa em 25/100;
- rótulos declarados de 70 `CLINICA_REAL` e 30 `CONCEITO_PURO`;
- `img: null` e `imgalt: ""` nas 100 questões.

Esses resultados **não significam aprovação editorial**.

## Falhas bloqueantes confirmadas

### 1. Preenchimento artificial nas 400 alternativas

Todas as **400/400 alternativas** contêm ao menos uma expressão genérica acrescentada
para ajustar o comprimento, e todas as **100/100 questões** têm esse problema nas
quatro alternativas. Foram contadas, entre outras:

- `de acordo com a relação funcional apresentada`: 176 ocorrências;
- `como mecanismo central do fenômeno descrito`: 171;
- `dentro do contexto clínico ou biológico proposto`: 169;
- `com repercussão direta no processo avaliado`: 163;
- `considerando o processo biológico em análise`: 161;
- `como explicação principal para o achado descrito`: 157;
- `no contexto fisiopatológico apresentado`: 148.

Essas expressões são semanticamente vazias em numerosos distratores, tornam a
linguagem repetitiva e artificial e violam expressamente a regra de não inflar
distratores para alcançar 15%. Há ainda repetições da mesma expressão dentro da
mesma alternativa em dezenas de itens, por exemplo `CB-PATO-071` A.

Exemplos claros: `CB-ANAT-033`, `CB-BIOQ-031`, `CB-FARM-005`, `CB-FISI-039`,
`CB-FISI-057` e `CB-PATO-071`.

### 2. Truncamento com perda de sentido

Foram confirmadas alternativas com parênteses abertos e frases truncadas:

- `CB-ANAT-100` D;
- `CB-EPI-021` A;
- `CB-ETICA-011` B;
- `CB-MICR-036` C.

Em `CB-ANAT-100` D, a alternativa correta termina no meio da enumeração de
hormônios (`"como, ... quanto ao mecanismo avaliado"`), portanto não constitui uma
proposição completa. Isso sozinho impede a aprovação do lote.

### 3. `CB-PATO-071` continua internamente incoerente

A mudança de gabarito de B para C está correta em relação ao texto das alternativas:
a alternativa C descreve adequadamente necrose de coagulação. Contudo, a explicação
e a análise individual não foram atualizadas:

- `uw.choices.B` ainda começa com `Correto`;
- `uw.choices.C` ainda diz que C inverte coagulação e liquefação;
- o parágrafo de diferenciação ainda chama a alternativa C de invertida;
- a candidata removeu de C as associações completas de liquefação e caseosa que
  constavam da alternativa original, mas a explicação continua descrevendo-as como
  se estivessem na resposta.

Logo, a candidata corrigiu `gab`/`uw.correct`, mas não realizou a correção conjunta
exigida de alternativa, explicação e análises A–D.

### 4. As explicações não foram materialmente revisadas

Os 100 enunciados permanecem idênticos aos originais. Em 100/100 questões, o novo
`exp` é apenas a concatenação literal dos blocos preexistentes de `uw.mech`. As
100 referências também permanecem idênticas. Portanto, a afirmação de correção
integral e aprofundamento novo não é sustentada pelo diff: houve reaproveitamento do
texto legado, não revisão médica e pedagógica demonstrável.

Além disso, `uw.choices` foi preservado, embora todas as 400 alternativas tenham
sido modificadas. Mesmo quando o núcleo conceitual foi mantido, a análise A–D
precisa ser reconferida contra a redação final, não simplesmente herdada.

### 5. Referências não verificadas

As 100/100 questões estão marcadas simultaneamente como:

- `fonte_status: REFERENCIA_PROFISSIONAL_DECLARADA_PENDENTE_CHECAGEM_LOCALIZADA`;
- `referencias_v2[].verificacao: PENDENTE_LOCALIZACAO_EDICAO_CAPITULO`.

Assim, nenhuma atende ao requisito contratual de referência profissional aberta e
conferida. Uma citação genérica como livro + tema pode ser ponto de partida, mas não
é evidência de conferência da afirmação usada na questão.

### 6. O 70/30 foi atingido por rótulo, não demonstrado semanticamente

O arquivo declara exatamente 70/30, porém os 100 enunciados são os mesmos do legado.
Há 39 itens rotulados `CLINICA_REAL` sem sequer marcadores textuais clínicos básicos
na triagem automática. Essa triagem não decide sozinha a categoria, mas, combinada
à ausência de justificativa item a item, demonstra que o número exato não pode ser
aceito como adjudicação semântica. Correlação clínica exige que o contexto modifique
o raciocínio ou a aplicação; citar uma doença ou adicionar uma vinheta decorativa
não basta.

### 7. O validador produz falso positivo editorial

O validador retorna `aprovado: true` porque mede estrutura, comprimentos e rótulos.
Ele não detecta:

- padding semântico;
- truncamento e parênteses abertos;
- contradição entre `gab` e o texto de `uw.choices`;
- fonte explicitamente pendente;
- reaproveitamento integral da explicação legada;
- classificação clínica meramente declarada.

Portanto, a palavra `aprovado` na saída atual deve ser interpretada somente como
“passou nas regras computadas”, nunca como `V2_APROVADA`.

## Avaliação médica e pedagógica

Não foi identificada evidência de que as proposições médicas centrais tenham sido
deliberadamente alteradas em massa; em geral, o núcleo das alternativas originais
foi preservado. Isso, porém, não basta para atestar ausência de distorção. O
truncamento confirmou perda de informação, e o preenchimento indiscriminado torna
algumas alternativas gramaticalmente associadas a mecanismos que elas negam. A
qualidade não é compatível com material de ensino.

Não é possível certificar uma melhor resposta nas 100 questões enquanto as 400
alternativas não forem reescritas individualmente e as análises A–D não forem
sincronizadas. `CB-PATO-071` prova objetivamente essa necessidade.

## Correção necessária antes de nova verificação

1. Descartar integralmente as 400 alternativas geradas desta candidata e retornar
   ao núcleo semântico original.
2. Reescrever cada conjunto A–D individualmente, com paralelismo natural e sem
   qualquer frase de enchimento; a margem de 15% deve resultar da edição semântica.
3. Corrigir os quatro itens truncados e executar verificação de sintaxe textual.
4. Em `CB-PATO-071`, manter C somente após atualizar explicação, diferenciação e
   `uw.choices`; decidir se a correta deve recuperar todos os padrões de necrose.
5. Revisar `exp` e `uw.mech` por questão, em vez de apenas copiar o legado.
6. Reescrever `uw.choices.A–D` contra as alternativas finais.
7. Localizar edição/capítulo/seção ou documento oficial de cada referência e mudar
   o status apenas após conferência real.
8. Adjudicar a classificação clínica item a item e documentar a justificativa.
9. Rodar novamente o validador e uma nova verificação independente completa.

## Alterações feitas pelo verificador

Nenhuma questão foi alterada. As falhas são substantivas e generalizadas; corrigi-las
pontualmente mascararia a necessidade de refazer a candidata. Este relatório é o
registro independente da rejeição e não concede estado `CORRECAO_VERIFICADA` ou
`V2_APROVADA`.
