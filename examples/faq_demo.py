"""A transparent, no-API-key FAQ demo. No personal or confidential data.

This *rule-based* public example is NOT a paid client case study.
"""
from __future__ import annotations

import re


FAQ = {
    "What does an automated weekly report include?": (
        "A scheduled report can include selected KPIs, validation failures, "
        "new records and export links. The scope depends on client needs."
    ),
    "Can a workflow import spreadsheet data?": (
        "Yes. A scoped workflow may import CSV or Excel exports after checking "
        "the column names, formats and file access requirements."
    ),
    "How are customer data and API keys handled?": (
        "Private data and API keys should not be sent through public forms. "
        "An integration requires a separately agreed secure access process."
    ),
}


def tokens(value: str) -> set[str]:
    return {
        x for x in re.findall(r"[a-z0-9]{3,}", str(value or "").lower())
        if x not in {"the", "and", "what", "does", "are", "can", "how"}
    }


def answer(question: str) -> dict:
    if not question or len(question) > 800:
        return {"answer": "Please ask a concise question.", "matched_question": None}
    query = tokens(question)
    hits = sorted(
        ((len(query & tokens(known)), known) for known in FAQ),
        key=lambda x: x[0],
        reverse=True,
    )
    if not query or not hits or hits[0][0] < 2:
        return {
            "answer": "I don't have a verified answer in this public FAQ demo.",
            "matched_question": None,
        }
    key = hits[0][1]
    return {"answer": FAQ[key], "matched_question": key}


if __name__ == "__main__":
    import sys
    print(answer(" ".join(sys.argv[1:]) or "weekly report"))
