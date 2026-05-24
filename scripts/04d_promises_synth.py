"""Pasul 4d: Sinteza promisiunilor per topic + raport SINTEZA.md.

Reads promise_status.jsonl, agrega per topic, produce raport markdown
human-readable cu citate evidence pentru fiecare categorie de status.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "results" / "04_promises" / "promise_status.jsonl"
OUT_MD = ROOT / "results" / "04_promises" / "SINTEZA.md"
OUT_CSV = ROOT / "results" / "04_promises" / "promise_status.csv"

STATUS_ORDER = ["KEPT", "IN_PROGRESS", "CONTRADICTED", "REFRAMED", "ABANDONED", "NO_MENTION", "ERROR"]
STATUS_EMOJI = {
    "KEPT": "✅",
    "IN_PROGRESS": "🔄",
    "REFRAMED": "🔀",
    "ABANDONED": "❌",
    "CONTRADICTED": "⚠️",
    "NO_MENTION": "❓",
    "ERROR": "💥",
}


def main():
    rows = []
    with SRC.open() as f:
        for line in f:
            rows.append(json.loads(line))
    print(f"Loaded {len(rows)} classified promises.")

    # CSV pentru export tabular
    import csv
    with OUT_CSV.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["status", "confidence", "topic", "specificity", "cluster_size",
                    "promise_text", "verbatim_quote", "source_date", "source_doc_id",
                    "reasoning", "supporting_evidence"])
        for r in rows:
            w.writerow([
                r.get("status_status", "?"),
                r.get("status_confidence", "?"),
                r.get("topic", "?"),
                r.get("specificity", "?"),
                r.get("cluster_size", 1),
                r.get("promise_text", ""),
                r.get("verbatim_quote", ""),
                r.get("source_date", ""),
                r.get("source_doc_id", ""),
                r.get("status_reasoning", ""),
                " | ".join(r.get("status_supporting_evidence", [])),
            ])
    print(f"CSV: {OUT_CSV}")

    # Aggregate counts
    total_status: dict[str, int] = defaultdict(int)
    per_topic: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for r in rows:
        s = r.get("status_status", "ERROR")
        t = r.get("topic", "alt")
        total_status[s] += 1
        per_topic[t][s].append(r)

    # Markdown report
    md = ["# Pasul 4 — Promise Tracker — Sinteză\n"]
    md.append(f"**Corpus:** 131 promisiuni canonice (din 150 raw, după dedup) extrase din ")
    md.append(f"corpusul de campanie (≤ 25 mai 2025). Evaluate vs corpusul de mandat ")
    md.append(f"(≥ 26 mai 2025, ~540 docs).\n")
    md.append("**Metodă:** Gemini 2.5 Flash, retrieval cu paraphrase-multilingual-mpnet, top-8 paragrafe evidence per promisiune.\n")

    md.append("\n## Sumar global\n")
    md.append("| Status | Count | % |")
    md.append("|---|---:|---:|")
    total = sum(total_status.values())
    for s in STATUS_ORDER:
        if total_status.get(s):
            pct = 100 * total_status[s] / total
            md.append(f"| {STATUS_EMOJI.get(s, '')} **{s}** | {total_status[s]} | {pct:.1f}% |")

    md.append("\n## Per topic\n")
    topic_order = sorted(per_topic.keys(),
                          key=lambda k: -sum(len(v) for v in per_topic[k].values()))
    for topic in topic_order:
        topic_total = sum(len(v) for v in per_topic[topic].values())
        md.append(f"\n### {topic} ({topic_total} promisiuni)\n")
        for s in STATUS_ORDER:
            items = per_topic[topic].get(s, [])
            if not items:
                continue
            md.append(f"**{STATUS_EMOJI.get(s, '')} {s}** ({len(items)})\n")
            for it in items[:5]:  # max 5 per status per topic
                spec = it.get("specificity", "?")
                conf = it.get("status_confidence", "?")
                date = it.get("source_date", "?")
                md.append(f"- *[{spec}, conf={conf}, {date}]* {it['promise_text']}")
                reasoning = it.get("status_reasoning", "").strip()
                if reasoning:
                    md.append(f"  - **Raționament:** {reasoning[:300]}")
                evs = it.get("status_supporting_evidence", [])
                if evs:
                    md.append(f"  - **Evidence:** *\"{evs[0][:200]}\"*")
            if len(items) > 5:
                md.append(f"- _(... și {len(items)-5} mai multe)_")

    md.append("\n## Note metodologice\n")
    md.append("- **Definiție promisiune:** angajament EXPLICIT la acțiune viitoare specifică, făcut de ND. Opinii, diagnoze și aspirații vagi excluse.")
    md.append("- **Retrieval evidence:** top-8 paragrafe din corpusul mandat după cosinus pe paraphrase-multilingual-mpnet.")
    md.append("- **Classification:** LLM Gemini 2.5 Flash, temperature=0.1, json output.")
    md.append("- **Limitări:** ")
    md.append("  - NO_MENTION ≠ ABANDONED — poate fi temă nemai-relevantă (alegeri trecute) sau pur și simplu netratată încă.")
    md.append("  - KEPT presupune ND a anunțat ACȚIUNE, nu doar a re-confirmat promisiunea verbal.")
    md.append("  - Corpusul mandat are bias spre teme de mare presă (deficit, justiție); promisiunile locale (PMB) sunt sub-reprezentate.")

    OUT_MD.write_text("\n".join(md))
    print(f"MD:  {OUT_MD}")
    print(f"\nTotal: {total} promisiuni, {len(per_topic)} topice.")


if __name__ == "__main__":
    main()
