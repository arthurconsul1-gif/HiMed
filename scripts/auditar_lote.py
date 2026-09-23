#!/usr/bin/env python3
"""Calcula métricas editoriais objetivas para um manifesto de lote."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def normalize(text: str) -> str:
    return " ".join(re.findall(r"\w+", text.casefold()))


def audit(question: dict[str, Any]) -> dict[str, Any]:
    alternatives = question["alts"]
    lengths = {letter: len(text.strip()) for letter, text in zip("ABCD", alternatives)}
    shortest = min(lengths.values())
    longest = max(lengths.values())
    answer = question["gab"]
    image = question.get("img")
    image_type = "none"
    if isinstance(image, str) and image.strip():
        value = image.strip().lower()
        image_type = "embedded_svg" if value.startswith("<svg") else (
            "remote_url" if value.startswith(("http://", "https://")) else "other"
        )

    correct_text = normalize(alternatives[ord(answer) - ord("A")])
    visible_image_text = normalize(" ".join(re.findall(r">([^<>]+)<", image or "")))
    correct_terms = {term for term in correct_text.split() if len(term) >= 6}
    visible_terms = set(visible_image_text.split())
    leaked_terms = sorted(correct_terms & visible_terms)
    return {
        "question_id": question["id"],
        "answer": answer,
        "alternative_lengths": lengths,
        "correct_is_strictly_longest": lengths[answer] > max(
            value for key, value in lengths.items() if key != answer
        ),
        "max_min_difference_percent_of_min": (
            round((longest - shortest) / shortest * 100, 2) if shortest else None
        ),
        "within_15_percent": bool(shortest and (longest - shortest) / shortest <= 0.15),
        "image_type": image_type,
        "image_alt": question.get("imgalt", ""),
        "possible_answer_terms_visible_in_svg": leaked_terms,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--bank", type=Path, default=Path("banco_completo.json"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    questions = {
        question["id"]: question
        for question in json.loads(args.bank.read_text(encoding="utf-8"))
    }
    missing = sorted(set(manifest["question_ids"]) - questions.keys())
    if missing:
        parser.error(f"IDs ausentes no banco: {', '.join(missing)}")
    items = [audit(questions[identifier]) for identifier in manifest["question_ids"]]
    report = {
        "lot_id": manifest["lot_id"],
        "total": len(items),
        "method": "character_count_after_outer_whitespace_trim",
        "warning": "A regra de 15% é alerta editorial; não autoriza inflação mecânica.",
        "correct_strictly_longest": sum(item["correct_is_strictly_longest"] for item in items),
        "within_15_percent": sum(item["within_15_percent"] for item in items),
        "with_image": sum(item["image_type"] != "none" for item in items),
        "possible_svg_leakage": sum(
            bool(item["possible_answer_terms_visible_in_svg"]) for item in items
        ),
        "questions": items,
    }
    output = args.output or args.manifest.with_name(f"{manifest['lot_id'].lower()}-metricas.json")
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(items)} questões auditadas em {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
