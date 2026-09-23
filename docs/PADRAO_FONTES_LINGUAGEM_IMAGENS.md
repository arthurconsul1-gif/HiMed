# Padrão de fontes, linguagem e imagens

## Fontes profissionais obrigatórias

Toda afirmação destinada a questão, alternativa, explicação, flashcard ou Livraria
deve ser rastreável a fonte de relevância profissional.

Ordem preferencial conforme o tipo de afirmação:

1. legislação, resolução, protocolo ou documento oficial vigente;
2. diretriz de Ministério da Saúde, OMS/OPAS ou sociedade profissional reconhecida;
3. revisão sistemática, consenso ou estudo primário quando a afirmação exigir;
4. livro-texto médico renomado e edição identificada para fundamentos estáveis;
5. fonte secundária apenas como apoio, nunca como evidência única de ponto crítico.

Cada registro deve incluir título, organização/autoria, edição/versão, capítulo ou
seção quando possível, URL/DOI/ISBN e data de acesso para conteúdo variável. Uma
referência genérica como “Ministério da Saúde” ou apenas o nome do livro é pendência,
não validação. Se a fonte não puder ser aberta ou não sustentar a frase, marcar
`NAO_VERIFICADO`; nunca completar por memória ou inventar continuidade.

## Linguagem de ensino

O texto deve ser acessível a estudante do 1º–4º semestre sem sacrificar precisão.
A pergunta de revisão é:

> Esta é a forma mais clara, natural e memorável de ensinar este mecanismo sem
> infantilizar o aluno nem pressupor conhecimento clínico avançado?

### Preferir

- frase direta, termo técnico correto e explicação imediata quando ele é novo;
- mecanismo em sequência causal;
- uma ideia principal por período quando o raciocínio for complexo;
- exemplos clínicos que realmente ajudam;
- conclusão curta e reutilizável;
- complexidade progressiva: fundamento → mecanismo → aplicação.

### Evitar

- tom infantil, coloquialismo excessivo ou analogia imprecisa;
- jargão não explicado;
- períodos muito longos;
- absolutos como “sempre” e “nunca” sem sustentação;
- enunciado artificialmente difícil;
- redundância entre `exp`, `uw.mech` e análises;
- resposta correta escrita como miniaula e distratores telegráficos.

O revisor pode simplificar ou elevar a linguagem, mas qualquer alteração de sentido
volta à verificação médica independente.

## Imagens: ensinar sem entregar o gabarito

### Decisão da primeira fase do Banco V2

As questões serão **autossuficientes e sem imagem**. No Banco V2 inicial, `img` será
`null`, `imgalt` ficará vazio e a resposta não dependerá de elemento visual. O banco
legado preserva as imagens para rastreabilidade, mas elas não migram nesta fase.

Atlas e questões visuais serão uma etapa posterior, com licença, acessibilidade e
auditoria próprias. Quando essa etapa começar, aplicam-se as regras abaixo.

A imagem deve ser necessária ou útil ao raciocínio e nunca funcionar como etiqueta
da resposta.

### Teste de vazamento da resposta

Antes de aprovar, o verificador deve ocultar as alternativas e perguntar:

1. há texto, seta, legenda, cor exclusiva ou rótulo que nomeia diretamente a resposta?
2. a imagem destaca apenas a estrutura correta e torna os distratores impossíveis?
3. o `imgalt` revela o diagnóstico ou a resposta, em vez de descrever a imagem?
4. nome de arquivo, crédito ou legenda contém o gabarito?
5. a imagem oferece uma pista pedagógica legítima ou resolve a questão sozinha?

Se entregar o gabarito, deve ser redesenhada, desrotulada, reequilibrada ou removida.
Uma imagem pode dar pista: relação espacial, padrão, curva, distribuição ou achado
que o aluno precisa interpretar. A pista deve exigir aplicação do conceito.

### SVGs

SVG autoral também exige revisão. Rótulos e camadas ocultas, texto alternativo,
cores e destaque visual serão auditados. Todo SVG precisa de autoria, proveniência,
licença interna e versão; “foi gerado” não basta.

### Acessibilidade e licença

O `imgalt` descreve o conteúdo necessário sem fornecer a resposta textual. Imagens
externas exigem página original, autoria, licença específica, atribuição, URL e data.
Estar no Wikimedia não é autorização automática.

## Verificação por dois agentes

O agente produtor registra fontes e justificativas. Um segundo agente dedicado
verifica afirmações, linguagem e vazamento visual. Divergência bloqueia o item até
adjudicação; nenhum dos dois aprova sozinho o próprio trabalho.
