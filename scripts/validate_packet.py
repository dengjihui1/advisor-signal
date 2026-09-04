#!/usr/bin/env python3
"""Validate a reviewable AdvisorSignal packet without network access."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional


URL_RE = re.compile(r"^https?://[^\s]+$")
PLACEHOLDERS = ("tbd", "todo", "your name", "your email", "example.com", "lorem ipsum")


def _errors(packet: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    for key in ("schema_version", "applicant", "supervisor", "fit", "papers", "deliverables", "unknowns"):
        if key not in packet:
            errors.append(f"missing top-level key: {key}")
    if errors:
        return errors
    for role in ("applicant", "supervisor"):
        value = packet[role]
        if not isinstance(value, dict):
            errors.append(f"{role} must be an object")
            continue
        sources = value.get("profile_sources" if role == "applicant" else "sources", [])
        if not sources or not all(isinstance(url, str) and URL_RE.match(url) for url in sources):
            errors.append(f"{role} needs at least one HTTP(S) source")
    fit = packet["fit"]
    if not isinstance(fit, dict) or not isinstance(fit.get("score"), (int, float)) or not 0 <= fit["score"] <= 100:
        errors.append("fit.score must be between 0 and 100")
    if fit.get("confidence") not in {"high", "medium", "low"}:
        errors.append("fit.confidence must be high, medium, or low")
    if len(packet["papers"]) > 2:
        errors.append("at most two papers are allowed")
    for index, paper in enumerate(packet["papers"], 1):
        if not isinstance(paper, dict) or not URL_RE.match(str(paper.get("url", ""))):
            errors.append(f"paper {index} needs an HTTP(S) URL")
    deliverables = packet["deliverables"]
    if not isinstance(deliverables, dict) or not deliverables.get("email"):
        errors.append("deliverables.email is required")
    else:
        email = str(deliverables["email"]).lower()
        if "subject:" not in email or not any(word in email for word in ("phd", "doctoral", "supervision", "opportunity")):
            errors.append("email needs a subject and a concrete doctoral opportunity ask")
        for placeholder in PLACEHOLDERS:
            if placeholder in email:
                errors.append(f"email contains placeholder: {placeholder}")
    return errors


def main(argv: Optional[List[str]] = None) -> int:
    if not argv:
        argv = sys.argv[1:]
    if len(argv) != 1:
        print("Usage: validate_packet.py PACKET.json")
        return 2
    path = Path(argv[0])
    try:
        packet = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Cannot read packet: {exc}")
        return 2
    errors = _errors(packet)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALID — AdvisorSignal packet passed structural and placeholder checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
