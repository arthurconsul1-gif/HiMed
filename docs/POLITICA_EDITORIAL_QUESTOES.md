# Política editorial obrigatória das questões

## Regra 70/30

Esta é uma regra permanente do Banco V2:

- **70% — correlação clínica real**;
- **30% — conceito fundamental puro e direto**.

Em 4.000 questões, a meta final é 2.800 clínicas e 1.200 puras. Somente questões
aprovadas, corrigidas e adjudicadas contam. Legado não auditado e rascunho não
podem ser usados para declarar a meta atingida.

A proporção será monitorada no banco, por sistema, disciplina, dificuldade e lote.
Em lote produtivo de 100, o alvo é 70 clínicas e 30 puras; em 200, 140 e 60. Para
outro tamanho, aplica-se 70% com arredondamento registrado. A faixa 65–75 por 100 é
apenas um alerta transitório durante produção; o banco final precisa fechar 70/30.

## Correlação clínica real

O contexto precisa ser necessário para ensinar ou aplicar o conceito básico. São
válidos: manifestação, fisiopatologia, exame físico, laboratório, interpretação de
imagem clínica,
farmacologia, diagnóstico introdutório, prevenção, epidemiologia, ética/comunicação
e Saúde Coletiva.

### Teste de remoção

> Se idade, sintomas, exames e cenário forem removidos, a questão continua exigindo
> exatamente o mesmo raciocínio?

- **Sim:** vinheta decorativa; classificar como conceito puro e simplificar, ou
  reescrever para uma aplicação genuína.
- **Não:** há correlação real, desde que a profundidade permaneça adequada ao ciclo
  básico.

Ter “um paciente” no enunciado não basta. A doença deve funcionar como janela para
estrutura, função, mecanismo, consequência ou prevenção — não como pretexto para
cobrar protocolo clínico avançado.

## Conceito puro

Avalia diretamente fundamento indispensável, sem depender de doença ou situação de
cuidado. Pode conter aplicação na explicação, mas é classificado pelo raciocínio
necessário para responder. Os 30% puros protegem os pré-requisitos e impedem que uma
vinheta artificial piore perguntas que são melhores de forma direta.

## Metadados futuros

```text
clinical_classification:
  CLINICA_REAL | CONCEITO_PURO | VINHETA_DECORATIVA |
  CLASSIFICACAO_AMBIGUA | PENDENTE_REVISAO
clinical_correlation_type:
  manifestacao_clinica | fisiopatologia | exame_fisico | laboratorio | imagem |
  farmacologia | diagnostico_introdutorio | prevencao | epidemiologia |
  etica_comunicacao | saude_coletiva
clinical_context_required: true | false
clinical_condition_ids: []
classification_rationale: texto
classification_status: proposto | revisado | adjudicado
```

Campo ausente nunca equivale automaticamente a `false`.

## Condições clínicas essenciais por sistema

Estas condições pertencem a uma casa curricular principal e não formam um catálogo
de condutas. Servem para ensinar princípios/mecanismos introdutórios; mesmo SDRA,
estado hiperosmolar, doença trofoblástica, leucemias e CIVD não autorizam cobrança
de manejo avançado. Um diagrama anatômico puro não vira correlação clínica apenas
por ser imagem: o achado visual deve participar de aplicação ou exame clínico.

### CARDIO

**Hipertensão arterial pertence primariamente ao currículo cardiovascular**;
aterosclerose; angina/doença coronariana; infarto; insuficiência
cardíaca; choques; arritmias introdutórias; estenose/insuficiência valvar;
pericardite/derrame/tamponamento; cardiopatias congênitas introdutórias. Trombose é
primariamente HEMATO e embolia pulmonar, RESP; CARDIO recebe suas repercussões.
Hipertensão deve integrar débito × resistência, complacência, rim/SRAA, autonômico,
endotélio, lesão de órgão-alvo, prevenção e mecanismos farmacológicos.

### RESP

Asma; DPOC/enfisema; pneumonia; atelectasia; edema pulmonar como repercussão;
embolia pulmonar; pneumotórax; derrame pleural; fibrose; fibrose cística como
integração genética; lesão alveolar/SDRA apenas como aprofundamento; apneia
obstrutiva; tuberculose e insuficiência respiratória. Distúrbios ácido-base são
síndromes/mecanismos associados, não doenças respiratórias.

### DIG

Refluxo; gastrite/úlcera; gastroenterites; doença celíaca; intolerância à lactose;
diarreia osmótica/secretora; constipação; doença inflamatória intestinal;
colelitíase/obstrução; pancreatite; hepatites; esteatose; cirrose/hipertensão portal;
apendicite como correlação anatômica. Padrões de icterícia são manifestações para
aplicar o metabolismo da bilirrubina, não doenças autônomas.

### RENAL

Lesão renal aguda; doença renal crônica; síndromes nefrítica/nefrótica; infecção
urinária baixa e pielonefrite; litíase; distúrbios de sódio, potássio e ácido-base;
hipertensão renal; doença renal diabética. Diabetes insípido e SIADH pertencem
primariamente a ENDO, embora seus efeitos renais sejam usados na explicação.

### ENDO

**Diabetes mellitus pertence primariamente ao currículo endócrino**. Diabetes tipos
1 e 2; cetoacidose e estado hiperosmolar introdutórios; hipoglicemia;
hipo/hipertireoidismo; bócio/iodo; Cushing e insuficiência adrenal;
hiperaldosteronismo; alterações de GH; hiperprolactinemia; distúrbios de PTH;
diabetes insípido/SIADH; SOP; obesidade/síndrome metabólica. Diabetes deve atravessar
metabolismo, fisiologia, patologia, rim, coração, prevenção, epidemiologia e
farmacologia, sem repetir o mesmo objetivo.

### NERV

AVC; epilepsia; meningite; esclerose múltipla; neuropatia/Guillain-Barré como
contraste; Parkinson; Alzheimer introdutório; lesão medular; radiculopatia;
miastenia; cefaleias; hidrocefalia; trauma cranioencefálico
introdutório; lesões de pares cranianos.

### REPRO

SOP; endometriose; infertilidade; gravidez ectópica; pré-eclâmpsia introdutória;
doença trofoblástica apenas como aprofundamento; criptorquidia; hiperplasia adrenal
congênita; IST; miomas; doença inflamatória pélvica; HPV/câncer cervical;
hiperplasia prostática. Contracepção permanece como intervenção curricular.

### LOCO

Fratura/reparo; osteoporose; raquitismo/osteomalácia; osteoartrite; artrite reumatoide
como condição primariamente locomotora; gota; Duchenne; lesões nervosas; entorses e
tendinopatias; osteomielite; artrite séptica; síndrome compartimental apenas como
aprofundamento anatômico.

### HEMATO

Anemias ferropriva, megaloblástica e hemolítica; falciforme; talassemias; leucemias
como introdução à clonalidade; trombocitopenia; hemofilia e von Willebrand; CIVD;
trombose; deficiência de G6PD; leucemia/linfoma introdutórios; incompatibilidade
transfusional; doença hemolítica neonatal. CIVD é aprofundamento, não núcleo.

### IMUNO

Anafilaxia/alergia; lúpus como condição autoimune sistêmica;
imunodeficiência combinada; HIV; deficiências de complemento; doença granulomatosa
como modelo; rejeição; vacinação; sepse; imunidade tumoral introdutória.

### TEG

Dermatites atópica/de contato; psoríase; acne; impetigo/celulite; micoses;
queimaduras; úlcera por pressão; queloide; vitiligo; albinismo; câncer de pele como
prevenção; escabiose. Lesões elementares permanecem linguagem semiológica.

## Limites

Cada condição deve ser decomposta em objetivos de estrutura, mecanismo, manifestação
ou prevenção; o nome da doença sozinho não constitui cobertura. Uma condição tem um
**sistema curricular principal**, mesmo quando a explicação usa
fisiologia ou consequências de outros órgãos. Menções a rim/SRAA na hipertensão e a
rim/coração no diabetes são integrações explicativas; não mudam a casa principal de
CARDIO e ENDO, respectivamente.

Não cobrar doses, protocolos completos, decisões de especialista, classificações
voláteis extensas ou doença rara sem alto valor mecanístico. Hipertensão e diabetes
recebem ampla cobertura por objetivos diferentes, não repetição nominal.

## Controle de qualidade

Autor classifica e justifica; revisor independente aplica o teste de remoção;
divergências são adjudicadas e não contam até a decisão. O painel deve mostrar 70/30
geral e por recorte, vinhetas decorativas, campos ausentes e concentração excessiva
da mesma doença ou aplicação.

## Regra técnica das alternativas

Para cada questão aprovada no Banco V2:

- a diferença entre a maior e a menor alternativa deve ser no máximo 15%, calculada
  por `(maior − menor) / menor` após remover espaços externos;
- em cada lote aprovado, a alternativa correta será a mais longa em 25% dos itens;
- empates na maior extensão serão registrados e não usados para disfarçar o padrão;
- o controle de 25% é do portfólio, não justificativa para tornar uma resposta
  artificialmente longa;
- nenhuma alternativa será inflada com palavras vazias: paralelismo, plausibilidade
  e precisão continuam prioritários.

Em lote de 100, a correta será a mais longa em exatamente 25. Para 150 ou outro
tamanho não divisível por quatro, o manifesto registra o arredondamento e compensa
no lote seguinte; em 200, serão 50.

## Entrega completa por lote

Um lote não termina no diagnóstico. A entrega inclui, nesta ordem:

1. auditoria curricular, médica, pedagógica, linguística e estrutural;
2. verificação de fontes;
3. proposta de correção fora do legado;
4. verificação independente da correção;
5. aplicação no arquivo do Banco V2;
6. revalidação integral;
7. relatório antes/depois.

Enunciado, quatro alternativas, gabarito, explicação principal, explicação em blocos,
análise individual A–D, objetivo, armadilha, referências e metadados são corrigidos
como uma unidade. Uma troca isolada de gabarito não constitui correção completa.
