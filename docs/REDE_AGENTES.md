# Rede longitudinal de agentes do HiMed

## O que é possível

O trabalho pode usar um coordenador e até três agentes especializados em paralelo.
Os agentes não ficam trabalhando infinitamente em segundo plano: cada execução tem
escopo, entrada e saída. A continuidade vem de filas e artefatos versionados no
repositório, não de memória informal nem de promessa de autonomia permanente.

## Regra obrigatória de verificação em pares

Todo trabalho produzido por um agente deve ser conferido por **outro agente criado
especificamente para verificá-lo**. Não basta QA genérico posterior. O manifesto da
tarefa registra `producer_agent`, `verifier_agent`, achados, divergências e decisão
da coordenação. Um artefato sem verificador permanece provisório e não avança.

## Papéis

1. **Coordenação/adjudicação:** congela lote, distribui, compara, resolve conflitos,
   comunica decisões e sempre propõe a próxima etapa.
2. **Arquitetura curricular:** objetivo real, `concept_id`, sistema, disciplina,
   pré-requisitos, Essencial/Importante/Aprofundamento, semestre, integração e 70/30.
3. **Revisão médica/pedagógica primária:** rubrica completa, achados G0–G4 e decisão.
4. **Pesquisa bibliográfica/normativa:** verifica cada afirmação e fonte; não inventa
   substituto para evidência ausente.
5. **Revisão crítica independente:** tenta refutar gabarito e primeira revisão antes
   de conhecer sua decisão final.
6. **Imagem/licenciamento:** necessidade, fidelidade, alt, origem, autoria, licença,
   atribuição e data.
7. **Correção editorial:** só depois da adjudicação; não aprova o próprio trabalho.
8. **Flashcards:** 1–3 apenas para questão aprovada e fonte confirmada.
9. **Livraria:** artigo próprio por conceito validado, não concatenação de explicações.
10. **QA estrutural:** schema, IDs, alternativas, gabarito, vínculos, distribuições e
    70/30; não certifica medicina.

## Fluxo persistente

```text
LEGADO_NAO_AUDITADO
→ MAPEAMENTO_PROPOSTO
→ REVISAO_PRIMARIA_CONCLUIDA
→ FONTES_VERIFICADAS | EVIDENCIA_INSUFICIENTE
→ REVISAO_CRITICA
→ AGUARDANDO_ADJUDICACAO
→ APROVADA | AJUSTE | REVISAO | REESCRITA | EXCLUSAO | ESPECIALISTA
→ CORRECAO_AUTORIZADA
→ REVALIDACAO_MEDICA
→ REVALIDACAO_ESTRUTURAL
→ PRONTA_PARA_BANCO_V2
→ FLASHCARDS/LIVRARIA
→ PRONTA_PARA_PUBLICACAO
```

Banco V2 e publicação são estados diferentes.

Um lote auditado só é considerado entregue depois de correção, verificação da
correção, aplicação no Banco V2 e relatório antes/depois. Diagnóstico isolado é um
estado intermediário, não a entrega final solicitada.

## Ondas paralelas

- **A:** currículo; revisão primária; fontes/imagens.
- **B:** revisão crítica; pesquisa especializada; licença.
- **C após adjudicação:** correção; flashcards aprovados; seção da Livraria.
- **D:** revalidação médica; revisão dos derivados; QA estrutural.

## Locks

Um único escritor por questão, artigo, cartão ou conceito. Revisores escrevem
relatórios separados; o legado nunca é alterado diretamente. Cada lock registra
recurso, lote, agente, finalidade, início, expiração e versão-base. Mudança da base
gera conflito; nunca vale “última gravação vence”.

## Independência

Quem produz não aprova. Correção, flashcard, artigo e revisão primária exigem outra
etapa de validação. G3/G4, imagem, norma, referência, segunda resposta defensável e
alteração de sentido devem ser escalados.

## Quando Arthur decide

Política 70/30, escopo, profundidade versus volume, novos módulos, regra comercial,
grande exclusão e ativação de flashcards. Pesquisa técnica e execução não devem ser
transferidas a ele por conveniência.

## Limites honestos

A rede acelera frentes independentes e preserva contraditório. Ela não substitui
especialista, não publica sozinha, não garante infalibilidade, não prova originalidade
absoluta e não executa indefinidamente sem novas rodadas coordenadas.

## Tamanho dos lotes

O piloto histórico de 20 serviu apenas para calibrar a rubrica. Os lotes de produção
terão **100 a 200 questões**. O padrão inicial será 100; poderá subir a 150 ou 200
quando a dupla produtor–verificador demonstrar consistência sem queda de qualidade.
Internamente os agentes podem dividir leitura, mas a entrega ao Arthur será o lote
completo, não vinte questões por vez.

## Próxima aplicação

Executar o primeiro lote produtivo de 100 com um agente revisor e outro agente
verificador dedicado; adjudicar; medir concordância, tempo e gargalos; depois
escalar para 150–200 quando for seguro.
