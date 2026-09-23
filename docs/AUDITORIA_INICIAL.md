# Auditoria inicial do banco de questões

## Escopo e método

Este diagnóstico substitui as conclusões antigas referentes a 358 questões. Ele foi
refeito sobre o `banco_completo.json` do commit `47d5ec8`, sem modificar nenhuma
questão. A conferência reproduzível é feita por `scripts/auditar_questoes.py`, que
usa apenas a biblioteca padrão do Python e trata como imagem somente um valor de
`img` que seja uma string não vazia.

> **Princípio editorial:** estes números medem integridade estrutural e ajudam a
> priorizar revisão humana. Eles não certificam correção médica. Nenhum conteúdo
> médico deve ser criado ou corrigido sem validação editorial e bibliográfica.

## Resultado executivo

| Verificação | Resultado |
|---|---:|
| JSON sintaticamente válido | sim |
| Tamanho | 4.316.334 bytes (aprox. 4,12 MiB) |
| Questões | 1.034 |
| IDs únicos | 1.034 |
| IDs duplicados | 0 |
| Enunciados exatamente duplicados | 0 |
| Questões com imagem real (`img` não vazio) | 109 |
| Questões sem imagem | 925 |
| Valores de imagem distintos | 99 |
| Imagens com `imgalt` não vazio | 109 de 109 |
| Questões com `img_revisar` não vazio | 6 |

As 109 questões com imagem dividem-se em **86 SVGs embutidos** e **23 URLs
remotas**. Não há referência a arquivo de imagem local. A contagem não considera
os seis pedidos textuais de `img_revisar` como imagens existentes.

## Campos existentes

Há 26 nomes de campo no conjunto. Vinte aparecem nas 1.034 questões:
`alts`, `area`, `armadilha`, `dif`, `enun`, `esp`, `exp`, `flag`, `gab`, `id`,
`img`, `imgalt`, `integradora`, `num`, `palavras_chave`, `referencia`, `sistema`,
`subtema`, `tema` e `uw`.

Os campos de presença parcial são:

| Campo | Presentes | Ausentes |
|---|---:|---:|
| `credito` | 748 | 286 |
| `correlacao_clinica` | 358 | 676 |
| `disciplinas_integradas` | 358 | 676 |
| `status` | 358 | 676 |
| `versao` | 358 | 676 |
| `img_revisar` | 6 | 1.028 |

## Distribuições

### Status

| Status | Questões |
|---|---:|
| ausente | 676 |
| `draft` | 358 |

Portanto, não é correto concluir que o banco inteiro está em `draft`: isso só é
explicitamente verdadeiro para 358 registros.

### Sistema

| Sistema | N | Sistema | N |
|---|---:|---|---:|
| REPRO | 93 | LOCO | 90 |
| RENAL | 88 | HEMATO | 87 |
| ENDO | 86 | TEG | 86 |
| NERV | 85 | RESP | 83 |
| CARDIO | 82 | DIG | 82 |
| IMUNO | 82 | Cardiovascular | 12 |
| Digestivo | 12 | Imunológico | 12 |
| Respiratório | 12 | Nervoso | 9 |
| Endócrino | 8 | Hematopoético | 7 |
| Tegumentar | 7 | Renal/Urinário | 6 |
| Locomotor | 4 | Reprodutor | 1 |

Há duas taxonomias misturadas (códigos e nomes por extenso). Elas devem ser
normalizadas somente após definir o vocabulário canônico e validar o mapeamento.

### Disciplina

O campo canônico de código, `area`, apresenta:

| Área | N | Área | N |
|---|---:|---|---:|
| FISI | 162 | ANAT | 134 |
| BIOQ | 114 | PATO | 99 |
| HIST | 81 | BCM | 79 |
| MICR | 67 | FARM | 53 |
| IMUN | 47 | EMBR | 43 |
| GENE | 37 | EPI | 35 |
| SEMIO | 25 | PARA | 23 |
| SC | 18 | ETICA | 17 |

`esp` traz os nomes por extenso correspondentes:

| Disciplina (`esp`) | N |
|---|---:|
| Fisiologia | 162 |
| Anatomia | 134 |
| Bioquímica | 114 |
| Patologia | 99 |
| Histologia | 81 |
| Biologia Celular e Molecular | 79 |
| Microbiologia | 67 |
| Farmacologia | 53 |
| Imunologia | 47 |
| Embriologia | 43 |
| Genética | 37 |
| Semiologia | 25 |
| Parasitologia | 23 |
| Epidemiologia e Bioestatística | 21 |
| Saúde Coletiva | 12 |
| Bioética e Ética | 9 |
| Epidemiologia | 7 |
| Epidemiologia/Bioestatística | 7 |
| Bioética, Ética e Profissionalismo | 6 |
| Saúde Coletiva e SUS | 6 |
| Ética/Bioética | 1 |
| Bioética e Profissionalismo | 1 |

EPI, SC e ETICA têm variantes de nomenclatura. Antes de uma migração, `area` deve
ser a referência para contagem.

### Dificuldade

| Dificuldade | N |
|---|---:|
| `intermediaria` | 562 |
| `basica` | 237 |
| `avancada` | 235 |

## Achados editoriais e próximos passos

1. **Integridade básica aprovada:** todos os registros têm quatro alternativas,
   gabarito A–D, bloco `uw`, quatro comentários de alternativas e concordância
   entre `gab` e `uw.correct`; toda imagem existente tem texto alternativo.
2. **Schema heterogêneo:** 676 questões não possuem `status`, `versao`,
   `disciplinas_integradas` nem `correlacao_clinica`. Isso deve ser resolvido antes
   de usar filtros ou importar assumindo a presença desses campos.
3. **Taxonomia heterogênea:** `sistema` mistura códigos e nomes; `esp` contém
   variantes. Produzir um mapa explícito e revisá-lo antes de alterar o banco.
4. **Imagens:** revisar disponibilidade, licença e adequação das 23 URLs remotas,
   além dos seis pedidos em `img_revisar`. Os 99 valores distintos para 109 usos
   também indicam reutilização, que não é necessariamente erro.
5. **Possíveis reaproveitamentos:** não há enunciados idênticos, mas há seis pares
   de explicações (`exp`) idênticas. Eles merecem revisão contextual, sem correção
   automática: CB-ANAT-123/129, CB-BCM-029/CB-PATO-053,
   CB-EMBR-027/030, CB-EPI-019/022, CB-FISI-119/139 e CB-MICR-025/033.
6. **Próxima etapa segura:** validar primeiro o schema e a taxonomia; depois fazer
   revisão médica humana, questão a questão, contra as referências. Este relatório
   não autoriza geração, preenchimento ou alteração automática de conteúdo.

## Reprodução

```bash
python scripts/auditar_questoes.py banco_completo.json
```

O comando é somente leitura e emite o relatório completo em JSON, incluindo a
presença de cada campo, todas as distribuições, duplicidades textuais e listas de
IDs para qualquer problema estrutural encontrado.
