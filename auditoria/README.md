# Inventário curricular do banco legado

## Arquivos

- `inventario_1034.csv`: uma linha por questão, com sistema consolidado, disciplina,
  tema, subtema, objetivo declarado em `uw.obj`, palavras-chave e metadados.
- `resumo_cobertura.json`: contagens reproduzíveis por sistema, disciplina,
  dificuldade e combinações mais frequentes.

Os arquivos são gerados por:

```bash
python scripts/inventariar_curriculo.py banco_completo.json
```

## Limite desta primeira passagem

O inventário preserva o que o banco **declara** e consolida apenas os onze códigos
de sistema. Ele não afirma que tema, disciplina, dificuldade, integração ou objetivo
estejam semanticamente corretos. Por isso, todas as linhas começam com:

```text
curricular_mapping_status = PENDENTE_VALIDACAO_SEMANTICA
medical_audit_status = LEGADO_NAO_AUDITADO
```

Na auditoria humana por lotes, esses campos deverão ser substituídos por decisão
rastreável, sem sobrescrever o arquivo original. O objetivo é comparar o conteúdo
realmente ensinado com `docs/CATALOGO_CURRICULAR_V1.md` e então calcular:

```text
meta curricular
− questões existentes aprovadas
= lacuna real de produção
```

O CSV não deve ser importado no aplicativo nem interpretado como Banco V2 aprovado.
