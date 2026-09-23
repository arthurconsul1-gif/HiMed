#!/usr/bin/env python3
"""Valida as regras determinísticas de um lote do Banco V2."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

LETTERS = "ABCD"
FORBIDDEN_PADDING = (
    "de acordo com a relação funcional apresentada",
    "como mecanismo central do fenômeno descrito",
    "dentro do contexto clínico ou biológico proposto",
    "com repercussão direta no processo avaliado",
    "considerando o processo biológico em análise",
    "como explicação principal para o achado descrito",
    "no contexto fisiopatológico apresentado",
)


def fail(problems: list[str], question_id: object, message: str) -> None:
    problems.append(f"{question_id or '<sem id>'}: {message}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("arquivo", type=Path)
    parser.add_argument("--esperado", type=int)
    args = parser.parse_args()

    questions = json.loads(args.arquivo.read_text(encoding="utf-8"))
    if not isinstance(questions, list):
        raise SystemExit("A raiz precisa ser uma lista de questões.")

    problems: list[str] = []
    ids = [q.get("id") for q in questions if isinstance(q, dict)]
    duplicates = [key for key, count in Counter(ids).items() if count > 1]
    if args.esperado is not None and len(questions) != args.esperado:
        problems.append(f"total {len(questions)}; esperado {args.esperado}")
    if duplicates:
        problems.append(f"IDs duplicados: {duplicates}")

    correct_is_strict_longest = 0
    clinical = Counter()
    for q in questions:
        if not isinstance(q, dict):
            problems.append("item que não é objeto")
            continue
        qid = q.get("id")
        alternatives = q.get("alts")
        answer = q.get("gab")
        if not isinstance(alternatives, list) or len(alternatives) != 4:
            fail(problems, qid, "deve possuir quatro alternativas")
            continue
        if answer not in LETTERS:
            fail(problems, qid, "gabarito inválido")
            continue
        lengths = [len(str(value).strip()) for value in alternatives]
        padded = [
            letter
            for letter, value in zip(LETTERS, alternatives)
            if any(phrase in str(value).casefold() for phrase in FORBIDDEN_PADDING)
        ]
        if padded:
            fail(problems, qid, f"padding editorial detectado em {','.join(padded)}")
        unbalanced = [
            letter
            for letter, value in zip(LETTERS, alternatives)
            if str(value).count("(") != str(value).count(")")
        ]
        if unbalanced:
            fail(problems, qid, f"parênteses desequilibrados em {','.join(unbalanced)}")
        if min(lengths) == 0:
            fail(problems, qid, "alternativa vazia")
        elif (max(lengths) - min(lengths)) / min(lengths) > 0.15:
            fail(problems, qid, f"alternativas excedem 15%: {lengths}")
        answer_index = LETTERS.index(answer)
        if lengths[answer_index] > max(length for i, length in enumerate(lengths) if i != answer_index):
            correct_is_strict_longest += 1
        uw = q.get("uw")
        if not isinstance(uw, dict) or uw.get("correct") != answer:
            fail(problems, qid, "gab diverge de uw.correct")
        choices = uw.get("choices") if isinstance(uw, dict) else None
        if not isinstance(choices, dict) or any(not str(choices.get(letter, "")).strip() for letter in LETTERS):
            fail(problems, qid, "uw.choices não analisa A, B, C e D")
        if q.get("img") is not None or q.get("imgalt", "") != "":
            fail(problems, qid, "primeira fase V2 deve estar sem imagem")
        if not str(q.get("referencia", "")).strip():
            fail(problems, qid, "sem referência")
        clinical[str(q.get("clinical_classification", "AUSENTE"))] += 1

    expected_longest = len(questions) / 4
    if expected_longest.is_integer() and correct_is_strict_longest != int(expected_longest):
        problems.append(
            f"correta estritamente mais longa em {correct_is_strict_longest}; "
            f"esperado {int(expected_longest)}"
        )

    report = {
        "arquivo": str(args.arquivo),
        "total": len(questions),
        "ids_unicos": len(set(ids)),
        "correta_estritamente_mais_longa": correct_is_strict_longest,
        "classificacao_clinica": dict(sorted(clinical.items())),
        "problemas": problems,
        "conformidade_deterministica": not problems,
        "nota": "Conformidade automática não equivale a aprovação médica/editorial.",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
