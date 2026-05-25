"""Pasul 4f: Manual overrides pe clasificarea Promise Tracker după fact-check web.

Pattern identic cu scripts/09c_sentiment_manual_overrides.py — păstrează
clasificarea originală LLM, adaugă marcaj transparent pentru override-uri.

Run:
    python scripts/04f_promise_overrides.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "results" / "04_promises" / "promise_status.jsonl"

# Override-uri manuale după fact-check web
# Match pe source_doc_id (cel mai sigur identifier)
OVERRIDES = [
    {
        "match_doc_id": "2025-05-20_nicusor-dan-despre-planurile-pentru-romania-stiri-b1tv-20-ma",
        "new_status": "REFRAMED",
        "new_confidence": "high",
        "override_reason": (
            "Fact-check web (mai 2025, 7+ surse): cronologia reală arată o "
            "REVIZUIRE conștientă a poziției, nu contradicție directă.\n\n"
            "20 mai 2025: ND zice 'Vigheciu (PSD) va fi primar interimar' "
            "— recunoaște regula constituțională (CGMB îl desemnase pe Vigheciu "
            "în ianuarie ca primul în ordine).\n"
            "20-23 mai: ND își schimbă poziția public — 'nu vrea primar de la "
            "PSD' (Digi24).\n"
            "23 mai: CGMB modifică ordinea, Stelian Bujduveanu (PNL) devine "
            "primar interimar (în loc de Vigheciu).\n\n"
            "SPIRITUL promisiunii ('viceprimar = primar interimar') A FOST "
            "RESPECTAT — Bujduveanu E viceprimar. PERSOANA s-a schimbat "
            "conștient și anunțat public motivul. Asta e REFRAMED (revizuire "
            "anunțată), NU CONTRADICTED (acțiune ascunsă, opusă).\n\n"
            "Surse: AGERPRES, Digi24, Europa Liberă, Euronews, G4Media, "
            "HotNews, ProTV. Plus alegerile parțiale dec 2025: Ciprian Ciucu "
            "(PNL) ales primar — bucureștenii au votat, regulă constituțională "
            "respectată."
        ),
    },
]


def main():
    rows = []
    with SRC.open() as f:
        for line in f:
            rows.append(json.loads(line))

    n_overridden = 0
    for r in rows:
        for ov in OVERRIDES:
            if r.get("source_doc_id") == ov["match_doc_id"]:
                old = r.get("status_status")
                new = ov["new_status"]
                if old != new:
                    r["status_status_original_llm"] = old
                    r["status_status"] = new
                    r["status_confidence"] = ov["new_confidence"]
                    r["override_reason"] = ov["override_reason"]
                    r["override_applied"] = True
                    n_overridden += 1
                    print(f"  Override: {r['source_doc_id'][:60]}: {old} → {new}")
                break

    with SRC.open("w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"\nApplied {n_overridden} overrides on promise_status.jsonl.")


if __name__ == "__main__":
    main()
