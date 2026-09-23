#!/usr/bin/env python3
"""Gera inventário curricular somente leitura do banco legado do HiMed."""

from __future__ import annotations

import argparse
import collections
import csv
import json
from pathlib import Path
from typing import Any


SYSTEMS = {
    "CARDIO": "CARDIO", "Cardiovascular": "CARDIO",
    "RESP": "RESP", "Respiratório": "RESP",
    "DIG": "DIG", "Digestivo": "DIG",
    "RENAL": "RENAL", "Renal/Urinário": "RENAL",
    "ENDO": "ENDO", "Endócrino": "ENDO",
    "REPRO": "REPRO", "Reprodutor": "REPRO",
    "NERV": "NERV", "Nervoso": "NERV",
    "LOCO": "LOCO", "Locomotor": "LOCO",
    "HEMATO": "HEMATO", "Hematopoético": "HEMATO",
    "IMUNO": "IMUNO", "Imunológico": "IMUNO",
    "TEG": "TEG", "Tegumentar": "TEG",
}

FIELDS = [
    "question_id", "system_declared", "system_code", "discipline_code",
    "discipline_name", "topic_declared", "subtopic_declared",
    "learning_objective_declared", "keywords", "difficulty_declared",
    "integrative_declared", "integrated_disciplines_declared",
    "clinical_correlation_declared", "has_image", "editorial_status",
    "curricular_mapping_status", "medical_audit_status",
]


def load_questions(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("a raiz deve ser uma lista de objetos")
    return data


def row(question: dict[str, Any]) -> dict[str, Any]:
    uw = question.get("uw") if isinstance(question.get("uw"), dict) else {}
    return {
        "question_id": question.get("id", ""),
        "system_declared": question.get("sistema", ""),
        "system_code": SYSTEMS.get(question.get("sistema"), "NAO_MAPEADO"),
        "discipline_code": question.get("area", ""),
        "discipline_name": question.get("esp", ""),
        "topic_declared": question.get("tema", ""),
        "subtopic_declared": question.get("subtema", ""),
        "learning_objective_declared": uw.get("obj", ""),
        "keywords": " | ".join(question.get("palavras_chave", [])),
        "difficulty_declared": question.get("dif", ""),
        "integrative_declared": question.get("integradora", False),
        "integrated_disciplines_declared": " | ".join(
            question.get("disciplinas_integradas", [])
        ),
        "clinical_correlation_declared": question.get(
            "correlacao_clinica", "NAO_DECLARADA"
        ),
        "has_image": isinstance(question.get("img"), str) and bool(question["img"].strip()),
        "editorial_status": question.get("status", "NAO_DECLARADO"),
        "curricular_mapping_status": "PENDENTE_VALIDACAO_SEMANTICA",
        "medical_audit_status": "LEGADO_NAO_AUDITADO",
    }


def summary(rows: list[dict[str, Any]], source: Path) -> dict[str, Any]:
    def count(field: str) -> dict[str, int]:
        values = collections.Counter(str(item[field]) for item in rows)
        return dict(sorted(values.items(), key=lambda item: (-item[1], item[0])))

    triples = collections.Counter(
        (item["system_code"], item["discipline_code"], item["topic_declared"])
        for item in rows
    )
    return {
        "source": str(source),
        "total_questions": len(rows),
        "mapping_status": "automatic_inventory_only",
        "warning": (
            "Tema, subtema e objetivo foram preservados do legado. "
            "Eles ainda não equivalem a classificação curricular validada."
        ),
        "systems": count("system_code"),
        "disciplines": count("discipline_code"),
        "difficulties": count("difficulty_declared"),
        "unique_declared_topics": len({item["topic_declared"] for item in rows}),
        "unique_declared_subtopics": len({item["subtopic_declared"] for item in rows}),
        "unique_system_discipline_topic_combinations": len(triples),
        "most_common_system_discipline_topics": [
            {"system": key[0], "discipline": key[1], "topic": key[2], "count": value}
            for key, value in triples.most_common(50)
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", type=Path, default=Path("banco_completo.json"))
    parser.add_argument("--csv", type=Path, default=Path("auditoria/inventario_1034.csv"))
    parser.add_argument("--summary", type=Path, default=Path("auditoria/resumo_cobertura.json"))
    args = parser.parse_args()

    questions = load_questions(args.source)
    rows = [row(question) for question in questions]
    args.csv.parent.mkdir(parents=True, exist_ok=True)
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", encoding="utf-8", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    args.summary.write_text(
        json.dumps(summary(rows, args.source), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"{len(rows)} questões inventariadas em {args.csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
