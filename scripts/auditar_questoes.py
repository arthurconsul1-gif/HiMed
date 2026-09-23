#!/usr/bin/env python3
"""Auditoria estrutural, sem alteração, do banco de questões do HiMed."""

from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path
from typing import Any, Iterable


MISSING = "<ausente>"


def distribution(questions: Iterable[dict[str, Any]], field: str) -> dict[str, int]:
    values = collections.Counter(
        MISSING if field not in question else str(question[field])
        for question in questions
    )
    return dict(sorted(values.items(), key=lambda item: (-item[1], item[0])))


def nonempty_image(question: dict[str, Any]) -> bool:
    return isinstance(question.get("img"), str) and bool(question["img"].strip())


def duplicate_groups(
    questions: Iterable[dict[str, Any]], field: str
) -> list[dict[str, Any]]:
    groups: dict[str, list[str]] = collections.defaultdict(list)
    for index, question in enumerate(questions, start=1):
        value = question.get(field)
        if isinstance(value, str) and value.strip():
            groups[value.strip()].append(str(question.get("id", f"linha {index}")))
    return [
        {"valor": value, "ids": ids}
        for value, ids in groups.items()
        if len(ids) > 1
    ]


def audit(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as source:
        data = json.load(source)
    if not isinstance(data, list):
        raise ValueError("a raiz do JSON deve ser uma lista")
    if not all(isinstance(question, dict) for question in data):
        raise ValueError("cada item da lista deve ser um objeto")

    questions: list[dict[str, Any]] = data
    ids = [question.get("id") for question in questions]
    id_counts = collections.Counter(ids)
    duplicate_ids = {
        str(identifier): count
        for identifier, count in id_counts.items()
        if count > 1
    }
    all_fields = sorted({field for question in questions for field in question})
    field_presence = {
        field: sum(field in question for question in questions) for field in all_fields
    }
    images = [question for question in questions if nonempty_image(question)]
    image_types = collections.Counter()
    for question in images:
        image = question["img"].strip()
        if image.lower().startswith("<svg"):
            image_types["svg_embutido"] += 1
        elif image.lower().startswith(("http://", "https://")):
            image_types["url_remota"] += 1
        else:
            image_types["arquivo_local"] += 1

    problems: dict[str, list[str]] = collections.defaultdict(list)
    for index, question in enumerate(questions, start=1):
        identifier = str(question.get("id", f"linha {index}"))
        alternatives = question.get("alts")
        answer = question.get("gab")
        uw = question.get("uw")
        if not isinstance(question.get("id"), str) or not question["id"].strip():
            problems["id_ausente_ou_invalido"].append(identifier)
        if not isinstance(alternatives, list) or len(alternatives) != 4:
            problems["quantidade_de_alternativas_diferente_de_4"].append(identifier)
        elif any(not isinstance(item, str) or not item.strip() for item in alternatives):
            problems["alternativa_vazia_ou_invalida"].append(identifier)
        if answer not in {"A", "B", "C", "D"}:
            problems["gabarito_invalido"].append(identifier)
        if not isinstance(uw, dict):
            problems["uw_invalido"].append(identifier)
        else:
            if uw.get("correct") != answer:
                problems["uw_correct_diverge_do_gabarito"].append(identifier)
            choices = uw.get("choices")
            if not isinstance(choices, dict) or set(choices) != {"A", "B", "C", "D"}:
                problems["uw_choices_incompleto"].append(identifier)
        if nonempty_image(question) and not str(question.get("imgalt", "")).strip():
            problems["imagem_sem_texto_alternativo"].append(identifier)

    return {
        "arquivo": str(path),
        "tamanho_bytes": path.stat().st_size,
        "json_valido": True,
        "total_questoes": len(questions),
        "ids_unicos": len(set(ids)),
        "ids_duplicados": duplicate_ids,
        "campos": field_presence,
        "distribuicoes": {
            field: distribution(questions, field)
            for field in ("status", "sistema", "area", "esp", "dif")
        },
        "imagens": {
            "questoes_com_imagem": len(images),
            "questoes_sem_imagem": len(questions) - len(images),
            "tipos": dict(sorted(image_types.items())),
            "imagens_distintas": len({question["img"].strip() for question in images}),
            "com_imgalt": sum(bool(question.get("imgalt", "").strip()) for question in images),
            "marcadas_para_revisao": sum(
                bool(question.get("img_revisar", "").strip()) for question in questions
            ),
        },
        "duplicidades_textuais": {
            "enunciados": duplicate_groups(questions, "enun"),
            "explicacoes": duplicate_groups(questions, "exp"),
        },
        "problemas_estruturais": dict(sorted(problems.items())),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("arquivo", nargs="?", type=Path, default=Path("banco_completo.json"))
    parser.add_argument("--compacto", action="store_true", help="imprime JSON sem indentação")
    args = parser.parse_args()
    try:
        report = audit(args.arquivo)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report, ensure_ascii=False, indent=None if args.compacto else 2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
