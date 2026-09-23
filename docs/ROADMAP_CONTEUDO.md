# Roadmap integrado de conteúdo do HiMed

## O que já existe

O banco possui 1.034 questões distribuídas por 16 áreas, 11 sistemas consolidados,
508 rótulos de `tema` e 886 rótulos de `subtema`. Desses, 320 temas e 770 subtemas
aparecem uma única vez. Isso demonstra amplitude de rótulos, mas ainda não prova
cobertura curricular: sinônimos, granularidades diferentes e conceitos repetidos
podem inflar a diversidade aparente.

### Sistemas consolidados

| Sistema | Questões | Temas distintos | Subtemas distintos |
|---|---:|---:|---:|
| Cardiovascular | 94 | 68 | 86 |
| Respiratório | 95 | 64 | 81 |
| Digestivo | 94 | 69 | 84 |
| Renal/Urinário | 94 | 63 | 83 |
| Endócrino | 94 | 59 | 85 |
| Reprodutor | 94 | 66 | 89 |
| Nervoso | 94 | 64 | 88 |
| Locomotor | 94 | 60 | 81 |
| Hematopoético | 94 | 61 | 80 |
| Imunológico | 94 | 58 | 82 |
| Tegumentar | 93 | 53 | 84 |

O equilíbrio de 93–95 questões por sistema é matemático, não evidência de cobertura
curricular adequada. Os sistemas não têm necessariamente a mesma extensão ou
prioridade; essa proporção não deve ser projetada automaticamente para 4.000.

| Área | Questões | Temas distintos | Subtemas distintos |
|---|---:|---:|---:|
| FISI | 162 | 98 | 135 |
| ANAT | 134 | 92 | 118 |
| BIOQ | 114 | 49 | 101 |
| PATO | 99 | 51 | 86 |
| HIST | 81 | 51 | 72 |
| BCM | 79 | 31 | 72 |
| MICR | 67 | 25 | 63 |
| FARM | 53 | 29 | 48 |
| IMUN | 47 | 20 | 40 |
| EMBR | 43 | 27 | 38 |
| GENE | 37 | 22 | 33 |
| EPI | 35 | 14 | 27 |
| SEMIO | 25 | 10 | 23 |
| PARA | 23 | 5 | 20 |
| SC | 18 | 11 | 13 |
| ETICA | 17 | 10 | 14 |

Os pesos por disciplina fornecidos no documento de transição têm duas versões
conflitantes. Uma delas soma 104% mesmo antes de incluir Genética e Parasitologia.
Nenhuma deve ser usada como orçamento de produção sem reconciliação.

### Fragmentação da taxonomia

- 508 temas exatos tornam-se 465 ao normalizar somente caixa e acentuação;
- 886 subtemas exatos tornam-se 866 com a mesma normalização;
- há 43 grupos de tema e 20 de subtema que diferem apenas por acento/codificação;
- existem possíveis relações de sinônimo ou hierarquia (`Neoplasia`/`Neoplasias`,
  `Herança`/`Padrões de herança`, por exemplo) que **não** devem ser fundidas por
  automação.

Foram encontradas 946 combinações `area + tema + subtema`: 882 aparecem uma vez.
As maiores concentrações são curva de dissociação da hemoglobina (6), sensibilidade
e especificidade (5), acoplamento excitação-contração (4) e níveis de prevenção
(4). Cada repetição precisa ser classificada como nova aplicação, revisão espaçada
ou redundância; a contagem sozinha não decide.

## Regra para chegar a 4.000 questões

Não gerar imediatamente “as 2.966 restantes”. Primeiro criar um inventário
conceitual canônico:

```text
sistema_id
disciplina_id
tema_id
subtema_id
conceito_id
objetivo_de_aprendizagem
pre_requisitos
semestre_faixa
prioridade
competencia_relacionada
nivel_cognitivo
cobertura_atual
meta_de_cobertura
lacuna
```

Somente depois será possível distinguir:

- conceito ausente;
- conceito coberto superficialmente;
- repetição espaçada útil;
- duplicação simples;
- excesso de questões de reconhecimento;
- falta de aplicação ou integração.

## Auditoria das 1.034

O piloto demonstrou que a auditoria por lote é indispensável. O plano completo terá
52 lotes: 51 de 20 e um de 14. Cada lote passa por:

1. congelamento da versão;
2. revisão médica/pedagógica primária;
3. pesquisa bibliográfica;
4. revisão crítica independente;
5. adjudicação;
6. diagnóstico antes de alterações;
7. correção controlada;
8. revalidação médica e estrutural;
9. histórico e possibilidade de rollback.

O piloto foi enriquecido com imagens, duplicatas e riscos; suas proporções não
devem ser extrapoladas diretamente às 1.034.

## Flashcards

Cada questão aprovada poderá originar de um a três flashcards editoriais. Eles não
devem ser produzidos antes da validação da questão, pois isso multiplicaria eventual
erro médico. Cada cartão deverá ter:

- `flashcard_id` e `concept_id`;
- `question_ids` de origem;
- pergunta/resposta atômicas;
- objetivo de retenção;
- fonte;
- versão e status editorial;
- regra de ativação e histórico de revisão.

A geração de 1–3 cartões e a ativação no ciclo são decisões diferentes. A regra de
ativação (sempre, após erro, após baixa confiança ou escolha do aluno) deverá ser
testada para evitar sobrecarga.

## Livraria Médica

O mesmo `concept_id` permite duas entradas:

- **pela questão:** abre diretamente a seção específica do conceito;
- **pelo menu:** navega sistema → disciplina → tema → subtema → conceito.

Artigos devem registrar visão geral, pré-requisitos, estrutura, mecanismo,
aplicação, diferenciações, erros comuns, imagens, fontes, questões e flashcards.
Não devem ser textos soltos nem repetir explicações sem governança.

## Relatórios

Relatórios devem agregar tentativas por `concept_id`, além de sistema e disciplina.
Isso permitirá mostrar lacunas reais, evolução, tempo, acertos, confiança,
reincidência de erro e revisões pendentes. Recomendações não devem ser baseadas
somente em uma porcentagem global.

## Atlas, imagem, laboratório e semiologia

- **Atlas:** estruturas precisam de identificadores anatômicos ligados aos mesmos
  conceitos, com proveniência, licença e desempenho no iPad.
- **Imagem:** modalidade, plano, anatomia, qualidade, achado e objetivo pedagógico;
  não usar imagem apenas decorativa.
- **Laboratório:** analito, fisiologia, pré-analítica, intervalo contextual,
  interpretação e limitações; evitar decorar valores sem mecanismo.
- **Semiologia/exame físico:** preparação, técnica, achado, mecanismo, limitações,
  segurança, comunicação e integração com anatomia/fisiologia.

## Ordem de execução

1. validar documentalmente a norma vigente;
2. fechar taxonomia e contrato de dados;
3. mapear as 1.034 por conceito;
4. auditar e corrigir em lotes;
5. definir metas conceituais das 4.000;
6. produzir novas questões somente para lacunas validadas;
7. gerar e revisar flashcards das questões aprovadas;
8. construir a Livraria sobre os mesmos conceitos;
9. reconstruir relatórios e arquitetura técnica;
10. desenvolver imagem, laboratório, semiologia e Atlas por etapas licenciadas.

Design e reconstrução do aplicativo ficam deliberadamente depois do contrato de
conteúdo. Isso evita construir uma interface nova sobre dados ainda inconsistentes.
