# Verificação independente — LOTE-001-A

## Decisão

**REPROVADO. Nenhuma das 50 questões deste arquivo deve ser promovida ao Banco
V2.** A candidata satisfaz parte das métricas formais, mas não demonstra a revisão
médica, pedagógica e bibliográfica individual exigida pelo protocolo. Há cinco
gabaritos materialmente errados, erros de linguagem, redundâncias curriculares,
distratores frequentemente absurdos e comentários A–D produzidos por molde.

Arquivo verificado: `auditoria/produção/lote-001-a.json` (50 itens), comparado com
`banco_completo.json` e com `docs/PROTOCOLO_AGENTE_ESCRITOR.md`.

## Achados transversais bloqueadores

1. **Cinco gabaritos errados:** `CB-EPI-007`, `CB-EPI-010`, `CB-EPI-027`,
   `CB-FISI-007` e `CB-FISI-085`. Em todos, `uw.correct` e `uw.choices` apenas
   reproduzem o gabarito errado, portanto concordância interna não equivale a
   correção científica.
2. **Análise A–D por molde:** nas 50 corretas aparece literalmente “Esse
   enunciado expressa a relação causal ou anatômica central testada nesta
   questão”; nas 150 incorretas aparece “Em contraste, a relação correta é”.
   Isso repete a correta em vez de explicar o erro conceitual específico de cada
   distrator.
3. **Trilha de revisão não individual:** os 50 registros usam a mesma declaração
   “preservado o núcleo pedagógico correto...”. As autoverificações marcam tudo
   como verdadeiro mesmo diante dos cinco gabaritos errados e dos erros de
   português. Logo, essas declarações não são evidência confiável.
4. **Referências insuficientemente localizadas:** os sete grupos de referência
   remetem genericamente a “capítulos correspondentes” ou a grandes conjuntos de
   capítulos; não registram capítulo/seção por questão nem a afirmação sustentada.
   Isso descumpre explicitamente o protocolo. Para ética, citar conjuntamente o
   Código de Ética e um tratado de princípios também não indica qual dispositivo
   normativo sustenta cada exceção.
5. **Distratores de baixa qualidade:** em muitos itens, três opções são
   biologicamente impossíveis ou trocam aleatoriamente órgãos e funções. Isso
   permite acerto por eliminação sem dominar o objetivo.
6. **Equilíbrio formal não basta:** as 50 questões estão sem imagem e dentro da
   margem de 15%; a correta é estritamente a mais longa em 14/50, e não em 12 ou
   13 como seria esperado para 25%. Essas métricas não compensam os defeitos
   semânticos.
7. **Classificação clínica superestimada:** há 28 rótulos `CLINICA_REAL`, mas
   vários itens só apresentam uma aplicação nominal ou perguntam uma definição
   direta. A justificativa é idêntica em todos e não demonstra a necessidade do
   contexto.
8. **Acesso bibliográfico externo:** uma tentativa independente de abrir fontes
   institucionais (NCBI, CDC e OMS) retornou HTTP 401 no ambiente. Isso não
   transforma as referências genéricas do escritor em fontes verificadas. Os
   cinco erros inequívocos abaixo são fundamentos estáveis cobertos pelos próprios
   livros-texto declarados, mas a próxima versão ainda deve localizar edição e
   seção antes de aprovação.

## Achados por questão

### Anatomia

- **CB-ANAT-033 — REVISÃO NECESSÁRIA.** A alternativa B mistura o trajeto de
  secreção direta ao duodeno com o desvio de armazenamento pela vesícula: a bile
  não percorre obrigatoriamente o ducto cístico antes do colédoco. O enunciado
  pede um único “trajeto normal” sem esclarecer armazenamento versus fluxo direto.
  Reestruturar o objetivo e os distratores; localizar a seção de vias biliares.
- **CB-ANAT-040 — REVISÃO NECESSÁRIA.** Gabarito A aceitável, mas os três
  distratores são grosseiramente falsos e não diagnosticam confusões reais entre
  nervos cranianos. A explicação A–D é genérica e a fonte não está localizada.
- **CB-ANAT-052 — REVISÃO NECESSÁRIA.** A está correta, porém “hipoderme” não é
  propriamente camada da pele em sentido histológico estrito; o texto deve dizer
  pele e tecido subcutâneo. Distratores são simples permutações e pouco educativos.
- **CB-ANAT-057 — REVISÃO NECESSÁRIA.** B é a melhor resposta, mas “paralisia
  das cordas vocais” deve ser qualificada conforme lesão unilateral/bilateral e
  ramo afetado. Os distratores usam relações anatômicas absurdas. Individualizar
  a análise e localizar anatomia cirúrgica da tireoide.
- **CB-ANAT-100 — REVISÃO NECESSÁRIA.** D está correta. O item testa simultaneamente
  posição e secreções, embora esteja classificado como anatomia; os erros são
  excessivamente óbvios. Definir uma competência principal e criar erros plausíveis.
- **CB-ANAT-104 — REVISÃO NECESSÁRIA.** B é aceitável, mas “dividida em dois
  lobos” simplifica pars intermedia e subdivisões. Os demais locais são absurdos.
  A explicação chama a hipófise de “glândula-mestra” sem discutir o controle
  hipotalâmico, uma formulação que merece maior precisão pedagógica.
- **CB-ANAT-134 — REESCRITA NECESSÁRIA.** B é a melhor opção, mas o enunciado
  pergunta vagamente como o fígado “se organiza” e a resposta só informa topografia
  e drenagem biliar. Sobrepõe CB-ANAT-033; deve receber objetivo distinto ou ser
  removida como redundância.

### Biologia celular e molecular

- **CB-BCM-016 — REVISÃO NECESSÁRIA.** A está correta. Falta distinguir dano
  por UV, fotoprodutos e reparo por excisão de nucleotídeos com precisão; B–D
  combinam processos incompatíveis e são facilmente descartados.
- **CB-BCM-024 — REVISÃO NECESSÁRIA.** A é correta, mas o enunciado praticamente
  entrega “segundo mensageiro” e os distratores são biologicamente inverossímeis.
  Usar vias reais (GPCR, receptor enzimático, receptor intracelular) como contraste.
- **CB-BCM-025 — REESCRITA/CONSOLIDAÇÃO.** C é correta, mas A, B e D são
  absurdas. É duplicata conceitual de CB-BCM-047; uma deve testar resposta ao dano
  e p53/apoptose, e a outra regulação do ciclo/carcinogênese.
- **CB-BCM-030 — REVISÃO NECESSÁRIA.** A está correta; B–D apenas descrevem
  organelas diferentes e incluem “substitui funcionalmente”, tornando a eliminação
  trivial. Criar distratores baseados na troca entre microtúbulos, actina e
  filamentos intermediários.
- **CB-BCM-047 — REESCRITA/CONSOLIDAÇÃO.** D correta, porém repete CB-BCM-025.
  Falta nomear checkpoints/mecanismos de maneira compatível com a dificuldade;
  distratores não são defensáveis.
- **CB-BCM-069 — REVISÃO NECESSÁRIA.** C está correta, mas há erro textual
  (“issó”), o cenário é vago e a relação distrofina–complexo glicoproteico–matriz
  extracelular foi reduzida a “membrana”. Explicar instabilidade do sarcolema e
  usar distratores mecanísticos reais.

### Bioquímica

- **CB-BIOQ-010 — REVISÃO NECESSÁRIA.** B é a melhor resposta em nível
  introdutório, mas “LDL alto/HDL baixo” vira pista decorativa e a linguagem
  simplifica excessivamente o transporte por lipoproteínas. Corrigir “Qual e” e
  evitar apresentar HDL como medida causal isolada de proteção.
- **CB-BIOQ-018 — REVISÃO NECESSÁRIA.** B correta; corrigir “refeição” e pontuação.
  C e D usam “controla isoladamente todo metabolismo” e são absurdas. Contrastar
  efeitos reais de insulina, glucagon e catecolaminas em tecidos definidos.
- **CB-BIOQ-031 — REVISÃO NECESSÁRIA.** C correta; corrigir “excessó”. O item
  deveria distinguir produção/excreção de urato e deposição de cristais, enquanto
  os atuais distratores trocam substâncias sem plausibilidade.
- **CB-BIOQ-044 — REVISÃO/CONSOLIDAÇÃO.** A correta, mas o nutriente não é
  identificado; B12 e folato compartilham megaloblastose, mas possuem diferenças
  relevantes. Sobrepõe CB-BIOQ-059. Definir se o objetivo é mecanismo morfológico
  ou diagnóstico nutricional.
- **CB-BIOQ-059 — REVISÃO/CONSOLIDAÇÃO.** C correta, mas repete CB-BIOQ-044 e
  agrupa B12/folato sem ensinar como diferenciá-los. Distratores são antônimos
  artificiais. Necessita objetivo complementar, não repetido.
- **CB-BIOQ-094 — REVISÃO NECESSÁRIA.** D descreve o ciclo de Cori, mas
  “ácido láctico (lactato)” é terminologia imprecisa em pH fisiológico e nem todo
  lactato segue exclusivamente ao fígado. Ajustar linguagem e explicar destinos
  alternativos sem invalidar o objetivo.
- **CB-BIOQ-096 — REVISÃO NECESSÁRIA.** B correta; corrigir “issó”. A explicação
  deve relacionar menor interação da HbF com 2,3-BPG à maior afinidade. Distratores
  C/D são absurdos.

### Embriologia

- **CB-EMBR-015 — REVISÃO NECESSÁRIA.** A é genericamente correta, mas o item
  não delimita período crítico nem mecanismo e os três distratores são absurdos.
  O exemplo de teratógeno deve ser preciso e sustentado por seção localizada.
- **CB-EMBR-023 — REVISÃO NECESSÁRIA.** B correta, porém pergunta apenas dois
  dos três shunts fetais e diz “desviam a maior parte” de modo impreciso. Delimitar
  especificamente desvio pulmonar e diferenciar fechamento funcional/anatômico.
- **CB-EMBR-024 — REVISÃO NECESSÁRIA.** B correta. “Óvulo” deve ser revisto em
  favor de ovócito secundário no momento da fecundação. Os distratores de dois
  espermatozoides são pouco plausíveis.
- **CB-EMBR-030 — REVISÃO NECESSÁRIA.** B correta; corrigir “nervosó”. A também
  começa com “Ectoderma” e pode funcionar como pista/confusão mal construída; a
  análise deve ensinar derivados dos três folhetos.
- **CB-EMBR-033 — REVISÃO NECESSÁRIA.** A correta e a troca do legado D para A
  foi adequada. Entretanto, B–D contêm absolutismos facilmente elimináveis e a
  explicação individual continua sendo molde.
- **CB-EMBR-038 — REVISÃO NECESSÁRIA.** D correta em termos gerais, mas “cerca
  de uma semana” deve ser precisado (início por volta do 6º dia). Distratores usam
  sítios ectópicos com estágios/timing manifestamente incompatíveis.

### Epidemiologia

- **CB-EPI-007 — ERRO CRÍTICO DE GABARITO.** O arquivo marca C, mas a correta é
  **A**: randomização tende a equilibrar confundidores e mascaramento reduz vieses
  de aferição/desempenho. C afirma falsamente aumento da prevalência. Corrigir
  `gab`, `uw.correct`, explicação e as quatro análises.
- **CB-EPI-008 — REVISÃO NECESSÁRIA.** C é a resposta didática esperada, mas
  “um bom teste deve priorizar” é absoluto: escolha de limiar depende de danos,
  prevalência e confirmação. Explicitar o objetivo de minimizar falsos-negativos.
- **CB-EPI-010 — ERRO CRÍTICO DE GABARITO.** O arquivo marca D, mas a correta é
  **B**: coorte parte da exposição e caso-controle parte do desfecho. Corrigir toda
  a cadeia; o próprio item CB-EPI-033 apresenta B conceitualmente como correta.
- **CB-EPI-021 — REVISÃO NECESSÁRIA.** A correta. A questão é definição pura,
  não aplicação; os distratores C/D misturam medidas sem plausibilidade. Incluir
  matriz 2x2 ou consequência interpretativa se a dificuldade for intermediária.
- **CB-EPI-027 — ERRO CRÍTICO DE GABARITO.** O arquivo marca D, mas a correta é
  **A**: transversal mede exposição e desfecho em um recorte. D descreve
  falsamente ensaio clínico como observacional. Corrigir gabarito e explicações.
- **CB-EPI-033 — REVISÃO/CONSOLIDAÇÃO.** C correta, mas duplica CB-EPI-010.
  Manter apenas se um item passar a explorar medida de associação, temporalidade
  ou viés em vez da mesma definição.

### Ética

- **CB-ETICA-006 — REVISÃO NECESSÁRIA.** D correta em nível principialista,
  mas alocação de órgãos é normativa e exige regra oficial brasileira aplicável,
  não apenas tratado de bioética. Distratores apresentam caricaturas dos princípios.
- **CB-ETICA-010 — REVISÃO/CONSOLIDAÇÃO.** B correta, mas confunde na pergunta
  “princípio e instrumento” e responde apenas “consentimento informado” seguido
  de autonomia. Sobrepõe quase literalmente CB-ETICA-013.
- **CB-ETICA-011 — REVISÃO NECESSÁRIA.** B é a melhor resposta, mas exceções
  ao sigilo exigem dispositivo normativo localizado e distinção entre dever legal,
  motivo justo e consentimento. Os demais distratores são extremos absurdos.
- **CB-ETICA-012 — REVISÃO NECESSÁRIA.** A correta, porém é memorização direta
  e os distratores apenas embaralham definições. Precisa de decisão contextual se
  classificada como clínica.
- **CB-ETICA-013 — REESCRITA/CONSOLIDAÇÃO.** D correta; corrigir “processó”.
  É duplicata de CB-ETICA-010 e não adiciona novo raciocínio.
- **CB-ETICA-017 — REVISÃO NECESSÁRIA.** C correta, mas a pergunta pede “por
  que é importante” e nenhuma alternativa realmente responde essa parte. A
  exceção genérica precisa de norma localizada; os distratores absolutos são fracos.

### Farmacologia

- **CB-FARM-003 — REVISÃO NECESSÁRIA.** A correta. O mecanismo deve ligar
  receptor beta-2/Gs/adenilil ciclase/AMPc/PKA ao relaxamento sem sugerir que
  antimuscarínico “degrada muco”. Distratores devem representar mecanismos reais.
- **CB-FARM-005 — REVISÃO NECESSÁRIA.** D correta; corrigir “insuficiência”,
  “diurético” e “Qual é”. Explicar NKCC2, gradiente medular e efeitos eletrolíticos;
  as demais opções são pouco plausíveis.
- **CB-FARM-006 — REVISÃO/CONSOLIDAÇÃO.** C correta; corrigir
  “farmacocinético”. O efeito oral menor não prova sozinho primeira passagem,
  pois absorção incompleta também reduz biodisponibilidade. O enunciado precisa
  informar absorção ou passagem portal. Duplica CB-FARM-028.
- **CB-FARM-028 — REVISÃO/CONSOLIDAÇÃO.** C correta e o enunciado sustenta
  primeira passagem, mas repete CB-FARM-006. Separar objetivos ou manter apenas
  este, que é mais autossuficiente.
- **CB-FARM-030 — REVISÃO NECESSÁRIA.** D correta, mas associa inicialmente
  eliminação a rins quando meia-vida depende também de metabolismo e distribuição.
  É conceito puro, não `CLINICA_REAL`, na redação atual.
- **CB-FARM-050 — REVISÃO NECESSÁRIA.** D é aceitável para contraceptivos
  combinados, mas “pílula” abrange formulações só de progestagênio cujo mecanismo
  relativo difere. Especificar contraceptivo hormonal combinado. Na redação
  atual é conceito farmacológico, não correlação clínica real.

### Fisiologia

- **CB-FISI-007 — ERRO CRÍTICO DE GABARITO.** O arquivo marca D, mas a correta é
  **A**: hipóxia estimula produção renal de eritropoetina, que aumenta eritropoiese
  na medula. D nega o mecanismo central. Corrigir todos os campos e reclassificar
  como adaptação fisiológica contextual, não necessariamente clínica.
- **CB-FISI-039 — REVISÃO NECESSÁRIA.** C correta. A doença sem nome é apenas
  moldura; a explicação deve ensinar redução de capacitância, aumento de resistência
  e concentração nodal de canais. B é bom erro inverso; A/D são mais fracos.
- **CB-FISI-057 — REVISÃO NECESSÁRIA.** B correta; corrigir “potencializam”.
  Qualificar que os efeitos metabólicos variam entre tecidos e explicar aumento de
  responsividade beta-adrenérgica. Distratores usam absolutismos.
- **CB-FISI-073 — REVISÃO NECESSÁRIA.** A correta; corrigir “nervoso”. O item
  oferece todos os achados clássicos e pede apenas o rótulo; é conceito puro.
  D é parcialmente composto por efeitos simpáticos e pode confundir por categoria.
- **CB-FISI-085 — ERRO CRÍTICO DE GABARITO.** O arquivo marca C, mas a correta é
  **A**: entrada de Ca2+ pré-sináptico desencadeia exocitose de neurotransmissores
  na sinapse química. C é biologicamente absurda. Corrigir toda a cadeia.
- **CB-FISI-103 — REVISÃO NECESSÁRIA.** D correta. “Anemia dilucional fisiológica”
  merece linguagem cuidadosa (“anemia fisiológica da gestação” por hemodiluição),
  e a pergunta pede uma dentre várias adaptações enquanto B mistura duas falsas.

## Condições para uma nova submissão

1. Corrigir os cinco gabaritos e reescrever integralmente suas explicações e
   comentários A–D.
2. Remover o gerador de comentários por molde; cada distrator deve ter um erro
   conceitual nomeado e explicado.
3. Resolver as cinco sobreposições principais: BCM-025/047, BIOQ-044/059,
   EPI-010/033, ETICA-010/013 e FARM-006/028, além de ANAT-033/134.
4. Corrigir todos os erros ortográficos e realizar leitura humana integral.
5. Localizar a fonte por questão (edição, capítulo/seção ou dispositivo oficial)
   e indicar quais afirmações ela sustenta; não declarar “confrontado” sem trilha.
6. Reclassificar correlação clínica com justificativa específica por item, sem
   usar a frase-padrão.
7. Só depois repetir métricas de 15%, distribuição de extensão e validação
   estrutural. Uma nova verificação independente é obrigatória.
