# Auditoria médica e pedagógica — piloto de 20 questões

## Escopo e limitações

Foi feita revisão primária, somente leitura, das 20 questões selecionadas. Nenhuma
questão foi modificada. Este documento é um **diagnóstico preliminar**: o acesso a
fontes oficiais na web foi bloqueado no ambiente, por isso nenhuma questão recebe
aprovação editorial final antes da reabertura das fontes, revisão crítica
independente e adjudicação.

Versão congelada:

- commit do banco: `47d5ec837af1b89cf700d8f1887a0156a68186e7`;
- blob Git de `banco_completo.json`: `c98cd16baa41578440a7c388f36a661ba8860ab7`.

## Decisão primária

| Decisão | N | IDs |
|---|---:|---|
| Aprovada sem ressalvas | 0 | — |
| Aprovada com ajustes | 7 | ANAT-008, FARM-005, GENE-009, HIST-009, SC-001, SEMIO-002, ANAT-003 |
| Revisão necessária | 9 | BCM-029, BIOQ-005, EMBR-012, EPI-033, ETICA-001, IMUN-017, MICR-003, PARA-009, BIOQ-020 |
| Reescrita necessária | 4 | PATO-053, FISI-002, FISI-119, FISI-139 |
| Exclusão definitiva | 0 | — |

Os IDs na tabela têm o prefixo `CB-`. “Aprovada com ajustes” ainda não significa
liberada para publicação: imagens e referências pendentes continuam bloqueando a
aprovação final.

## Achados confirmados de maior gravidade

1. **CB-FISI-002 — imagem incompatível (G3):** a pergunta trata de perfusão
   coronariana, mas o SVG e o `imgalt` tratam de potencial de ação cardíaco, fase de
   platô e tetania. A publicação deve permanecer bloqueada até remoção ou
   substituição validada da imagem.
2. **CB-EPI-033 — formulação conceitualmente imprecisa (G2):** coorte é ensinada
   como necessariamente prospectiva. Coortes também podem ser retrospectivas;
   exposição e seleção/direção lógica devem definir o contraste com caso-controle.
3. **Duplicação literal:** `CB-BCM-029`/`CB-PATO-053` e
   `CB-FISI-119`/`CB-FISI-139` possuem `exp` idêntico. Nos dois pares o objetivo é
   tão próximo que a repetição não demonstra, como está, revisão espaçada por nova
   aplicação.
4. **Imagens:** os nove SVGs do lote não têm autoria/licença explícita. As quatro
   URLs externas ainda exigem verificação da página original, autoria, licença,
   versão, atribuição e data de acesso.

## Revisão por questão

### CB-BCM-029 — revisão necessária (G2)

Gabarito e distinção central são adequados, mas a correta é uma definição completa
e muito maior, enquanto os distratores são caricatos. Apoptose/necrose são tratadas
em absolutos. A questão é reconhecimento, não intermediária integradora. O `exp` é
idêntico ao de PATO-053 e a referência não informa edição/capítulo.

### CB-PATO-053 — reescrita necessária (G3 editorial)

O gabarito está correto, mas a questão praticamente duplica BCM-029 e é incompatível
com a dificuldade avançada. Se mantida, deve ganhar objetivo próprio de Patologia,
com morfologia, mecanismo ou contexto; alternativamente, um dos itens deverá ser
fundido/excluído após adjudicação.

### CB-ANAT-008 — aprovada com ajustes

O trajeto biliar e o gabarito estão corretos. Ajustar acentuação e deixar explícita
a formação do hepático comum e do colédoco. O SVG permanece bloqueado para uso
comercial até confirmação de proveniência.

### CB-BIOQ-005 — revisão necessária (G2)

Mecanismo da cetoacidose e gabarito estão adequados. A correta é muito mais
informativa que os distratores. Especificar que acetoacetato e beta-hidroxibutirato
contribuem para a acidose; acetona não deve ser incluída genericamente como ácido.
A dificuldade pode ser intermediária. SVG sem proveniência.

### CB-EMBR-012 — revisão necessária (G2)

Relação entre folato e defeitos do tubo neural está adequada. “Essencial a ele” é
vago; explicitar metabolismo de um carbono/síntese de nucleotídeos. Distratores são
absurdos. Recomendação populacional, dose e alto risco exigem fonte oficial atual.
SVG sem proveniência.

### CB-EPI-033 — revisão necessária (G2)

O gabarito é o melhor, mas a definição confunde desenho de coorte com coleta
necessariamente prospectiva. A alternativa correta é desproporcionalmente longa.
Reescrever o contraste por seleção de participantes e direção lógica.

### CB-ETICA-001 — revisão necessária (G2)

O gabarito é aceitável sob as premissas do caso, mas “autonomia prevalece” é
absoluto demais. Capacidade, informação, voluntariedade, documentação e exceções
legais/emergenciais precisam aparecer. `NERV` não é sustentado pelo conteúdo. O
Código de Ética precisa de resolução, artigos e versão vigentes.

### CB-FARM-005 — aprovada com ajustes

Gabarito correto. Nomear NKCC2 no ramo ascendente espesso e explicar
natriurese/diurese. Corrigir acentuação e melhorar distratores. O `imgalt` é genérico
e o SVG não tem proveniência.

### CB-FISI-002 — reescrita necessária (G3)

Mecanismo central e gabarito são adequados, mas evitar afirmar ausência absoluta de
fluxo sistólico no ventrículo esquerdo. A imagem de potencial de ação é estranha ao
tema de perfusão coronariana e bloqueia publicação.

### CB-GENE-009 — aprovada com ajustes

O modelo mendeliano e o gabarito estão corretos. Manter explícito “a cada gestação”
e as proporções 25/50/25. “Necessariamente” depende das premissas do diagnóstico e
da parentalidade, embora o enunciado já defina dois portadores. SVG pertinente,
mas sem proveniência.

### CB-HIST-009 — aprovada com ajustes

Epitélio e função mucociliar estão corretos. Delimitar traqueia/brônquios e as
mudanças distais; corrigir acentuação. A página do Wikimedia e a licença CC BY 4.0
precisam ser verificadas, não apenas inferidas do campo `credito`.

### CB-IMUN-017 — revisão necessária (G2)

O gabarito descreve funções predominantes, mas não absolutamente exclusivas, de
CD4 e CD8. Usar essa qualificação. A questão é básica, não avançada; os distratores
são triviais. SVG sem proveniência.

### CB-MICR-003 — revisão necessária (G2)

O gabarito é o melhor. Explicar retenção do complexo cristal-violeta–iodo após a
descoloração e que betalactâmicos ligam PBPs/inibem transpeptidação, evitando dizer
que “miram o peptidoglicano” diretamente. Verificar a licença da imagem externa.

### CB-PARA-009 — revisão necessária (G2/G3 de imagem/fonte)

O diagnóstico geral está adequado, mas febre não deve ser apresentada como sempre
regular e anemia malárica é multifatorial, não apenas lise sincronizada das hemácias
infectadas. A imagem não necessariamente permite espécie. Validar arquivo e fonte
oficial de malária.

### CB-SC-001 — aprovada com ajuste textual

Vacinação como prevenção primária e gabarito estão adequados; as alternativas são
paralelas e equilibradas. A referência do Ministério da Saúde precisa de documento
identificável. O sistema RESP decorre do exemplo de gripe, não da disciplina.

### CB-SEMIO-002 — aprovada com ajustes

No adulto, pelo método auscultatório, fase I corresponde à sistólica e fase V à
diastólica. Explicitar adulto/técnica e reconhecer contextos em que fase IV é usada.
Integração com segunda disciplina precisa ser demonstrada. SVG sem proveniência.

### CB-BIOQ-020 — revisão necessária (G2)

A correta é a melhor, mas deve separar ações: PTH atua em rim/osso e aumenta
calcitriol; calcitriol aumenta sobretudo absorção intestinal. PTH não age
diretamente no intestino. O papel da calcitonina em adultos não deve ser apresentado
como eixo simétrico. Área BIOQ e sistema LOCO são discutíveis frente a FISI/ENDO.

### CB-FISI-119 — reescrita necessária (G3 editorial)

O resumo é essencialmente correto, mas a resposta é enorme, os distratores são
absurdos e “avançada” é incompatível. Explicar feedback positivo sustentado do
estradiol, pico de LH, seleção folicular e produção lútea sem cronologia fixa. É
duplicada de FISI-139.

### CB-FISI-139 — reescrita ou fusão após adjudicação (G3 editorial)

Repete objetivo, explicação e referência de FISI-119. “Meio do ciclo” não deve
transformar um ciclo ideal de 28 dias em regra universal. A marcação integradora
não demonstra duas disciplinas. Manter apenas se receber objetivo realmente novo.

### CB-ANAT-003 — aprovada com ajustes

Anatomia do brônquio principal direito está adequada. Não generalizar a localização
de pneumonia aspirativa sem considerar posição corporal e segmentos dependentes.
Validar autor, página, CC BY 2.5, atribuição e data de acesso da imagem externa.

## Padrões do lote

- resposta correta longa/enciclopédica contra três alternativas absurdas;
- dificuldade declarada acima do raciocínio realmente exigido;
- integração marcada sem duas disciplinas demonstradas;
- referências bibliográficas pouco identificáveis;
- imagens sem registro de proveniência;
- uso de absolutos onde existem nuances fisiológicas ou clínicas.

Não corrigir esses padrões alongando distratores. A correção deve partir de erros
conceituais reais, com alternativas paralelas, plausíveis e apenas uma melhor
resposta.

## Próximo controle

Antes de qualquer correção:

1. reabrir e registrar as fontes oficiais/primárias;
2. executar revisão crítica independente sem ancoragem na decisão acima;
3. adjudicar divergências;
4. apresentar o diagnóstico final;
5. somente então preparar um lote de mudanças versionado e reversível.
