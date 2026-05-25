"""Pasul 9c: Manual overrides pe sentiment classifications după fact-check web.

Gemini ocazional supra-interpretează tonul tensionat din context ca "negativ"
chiar dacă în realitate ND e mediator sau apără poziția unei entități.

Acest script aplică override-uri manuale și marchează clar care sunt
recalibrate vs originale.

Run:
    PROJECTION=vorbit python scripts/09c_sentiment_manual_overrides.py
"""
from __future__ import annotations

import json
import os
from pathlib import Path

PROJECTION = os.getenv("PROJECTION", "overall")
ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "results" / f"09_sentiment_per_entity_{PROJECTION}" / "sentiment_per_entity_period.jsonl"

# Manual overrides — bazate pe fact-check independent web/corpus
# Format: (entity, period_substring, new_sentiment, reason)
OVERRIDES = [
    (
        "PSD", "2026Q2 cotitură",
        "mixt",
        (
            "Fact-check web (apr-mai 2026): ND a fost MEDIATOR în criza coaliție, "
            "NU atacator PSD. 'Nu sunt propunerile PSD-ului' (8 apr) = ND apără "
            "procesul de numire procurori, NU critică PSD. PSD însuși a atacat "
            "Bolojan și a ieșit din guvern; ND a încercat să mențină coaliția "
            "('Calm și vom trece prin asta'). Refuzul guvernului minoritar cu "
            "AUR e critică la AUR, nu la PSD. Singura critică reală: 'PSD nu a "
            "vrut programul guvernare'. Sentiment corect: MIXT (recunoaște "
            "blocaj + apăra mecanismul instituțional + recunoaște necesitatea "
            "PSD pentru majoritate)."
        ),
    ),
]


def main():
    rows = []
    with SRC.open() as f:
        for line in f:
            rows.append(json.loads(line))

    n_overridden = 0
    for r in rows:
        for entity, period_sub, new_sent, reason in OVERRIDES:
            if r.get("entity") == entity and period_sub in r.get("period", ""):
                old = r.get("sentiment")
                if old != new_sent:
                    r["sentiment_original_gemini"] = old
                    r["sentiment"] = new_sent
                    r["override_reason"] = reason
                    r["override_applied"] = True
                    n_overridden += 1
                    print(f"  Override: {entity} {r['period'][:30]} {old} → {new_sent}")
                break

    # Save back
    with SRC.open("w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"\nApplied {n_overridden} overrides on {PROJECTION}.")


if __name__ == "__main__":
    main()
