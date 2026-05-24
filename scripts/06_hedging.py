"""Pasul 6: Hedging / epistemic markers — cuantifică stilul deliberativ vs categoric.

Pentru fiecare doc + agregat per perioadă × proiecție:
  - Count markeri de HEDGING (incertitudine, deliberativ)
  - Count markeri de CERTITUDINE (categoric, asertiv)
  - Count "personal attribution" (eu, mi se pare, opinia mea)
  - Hedge rate, certainty rate (per 1000 cuvinte)

Lexicon RO custom (compiled manual din literatura epistemică RO).

Run:
    for p in overall scris vorbit; do PROJECTION=$p python scripts/06_hedging.py; done
"""
from __future__ import annotations

import os
import re
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from corpus import _normalize_diacritics, load_corpus

PROJECTION = os.getenv("PROJECTION", "overall")
OUT = Path(__file__).resolve().parent.parent / "results" / f"06_hedging_{PROJECTION}"
OUT.mkdir(parents=True, exist_ok=True)

# Lexicons (lowercase, diacritice ș/ț)
HEDGING = [
    # Modale + epistemice
    "cred că", "cred ca", "mi se pare", "mi-e", "mi se",
    "în opinia mea", "după părerea mea", "după mine", "personal",
    "probabil", "poate", "posibil", "e posibil", "este posibil",
    "s-ar putea", "ar putea", "s-ar", "ar trebui poate",
    "nu sunt sigur", "nu sunt convins", "nu știu sigur",
    "eventual", "oarecum", "într-un fel", "intr-un fel",
    "mai degrabă", "mai degraba", "parțial", "partial",
    "tinde să", "tinde sa", "îmi închipui", "imi inchipui",
    "presupun", "bănuiesc", "banuiesc", "estim",
    "dacă bine îmi", "din câte știu", "din cate stiu",
    "se pare că", "se pare ca",
    "într-o anumită măsură", "intr-o anumita masura",
    "în general", "in general", "în principiu", "in principiu",
    "putem spune", "as zice", "aș zice",
]

CERTITUDINE = [
    "evident", "clar", "sigur", "fără îndoială", "fara indoiala",
    "în mod cert", "in mod cert", "categoric", "indiscutabil",
    "absolut", "fără doar și poate", "fara doar si poate",
    "negreșit", "negresit", "incontestabil", "neapărat", "neaparat",
    "fără echivoc", "fara echivoc", "neîndoielnic", "neindoielnic",
    "100%", "sută la sută", "suta la suta",
    "în mod sigur", "in mod sigur", "garantat",
    "trebuie", "obligatoriu", "neapărat", "neaparat",
    "ferm", "convins", "convins că", "convins ca",
    "nu există dubiu", "nu exista dubiu", "nu este loc de dubiu",
    "fără nicio îndoială", "fara nicio indoiala",
]

PERSONAL = [
    "eu", "mie", "meu", "mea", "mei", "mele",
    "după mine", "după părerea mea", "dupa parerea mea",
    "personal", "în ce mă privește", "in ce ma priveste",
    "îmi", "imi", "mi se", "mi-",
]


def period_for(date_str: str) -> str:
    y, m = int(date_str[:4]), int(date_str[5:7])
    if y == 2024 or (y == 2025 and m <= 2):
        return "2024Q4-2025Q1 candidatură-precampanie"
    if y == 2025 and m <= 5:
        return "2025Q2 campanie + investitură"
    if y == 2025 and m <= 8:
        return "2025Q3 deficit + reforma economică"
    if y == 2025 and m <= 11:
        return "2025Q4 stabilizare + diplomație"
    if y == 2025 and m == 12 or (y == 2026 and m <= 2):
        return "2025Q4-2026Q1 reformă judiciară"
    if y == 2026 and m <= 5:
        return "2026Q2 cotitură UE + criză guvern"
    return "outside-scope"


def count_markers(text: str, markers: list[str]) -> int:
    """Count occurrences of markers in text. Uses word-boundary regex for short markers."""
    text = _normalize_diacritics(text.lower())
    total = 0
    for m in markers:
        m = _normalize_diacritics(m.lower())
        if " " in m or "-" in m:
            # Multi-word: substring match
            total += text.count(m)
        else:
            # Single word: word boundary
            total += len(re.findall(r"\b" + re.escape(m) + r"\b", text))
    return total


def main():
    speeches = load_corpus()
    print(f"Loaded {len(speeches)} docs (projection={PROJECTION}).")

    rows = []
    for s in speeches:
        text = s.nd_only_text
        n_words = len(text.split())
        if n_words < 30:
            continue
        h = count_markers(text, HEDGING)
        c = count_markers(text, CERTITUDINE)
        p = count_markers(text, PERSONAL)
        rows.append({
            "id": s.id,
            "date": s.date,
            "tip": s.tip,
            "period": period_for(s.date),
            "n_words": n_words,
            "n_hedging": h,
            "n_certitudine": c,
            "n_personal": p,
            "hedge_per_1000w": 1000 * h / n_words,
            "cert_per_1000w": 1000 * c / n_words,
            "personal_per_1000w": 1000 * p / n_words,
            "hedge_cert_ratio": h / (c + 1),  # +1 to avoid div-by-zero
        })

    df = pd.DataFrame(rows)
    df.to_csv(OUT / "hedging_per_doc.csv", index=False)
    print(f"Per-doc CSV: {len(df)} rows")

    # Aggregate per period
    agg = df.groupby("period").agg({
        "id": "count",
        "n_words": "sum",
        "n_hedging": "sum",
        "n_certitudine": "sum",
        "n_personal": "sum",
        "hedge_per_1000w": "mean",
        "cert_per_1000w": "mean",
        "personal_per_1000w": "mean",
        "hedge_cert_ratio": "mean",
    }).round(2).rename(columns={"id": "docs"})
    agg.to_csv(OUT / "hedging_per_period.csv")

    # Markdown
    md = [f"# Pasul 6 — Hedging / epistemic markers ({PROJECTION})\n"]
    md.append(f"**Docs analizate**: {len(df)} (≥30 cuvinte) | total words: {df['n_words'].sum():,}\n")
    md.append("## Métrici globale\n")
    md.append(f"- Hedging markers: **{df['n_hedging'].sum()}** ({df['n_hedging'].sum()/df['n_words'].sum()*1000:.2f}/1000w)")
    md.append(f"- Certitudine markers: **{df['n_certitudine'].sum()}** ({df['n_certitudine'].sum()/df['n_words'].sum()*1000:.2f}/1000w)")
    md.append(f"- Personal attribution: **{df['n_personal'].sum()}** ({df['n_personal'].sum()/df['n_words'].sum()*1000:.2f}/1000w)")
    hedge_cert_ratio_global = df['n_hedging'].sum() / max(df['n_certitudine'].sum(), 1)
    md.append(f"- **Hedge:Cert ratio = {hedge_cert_ratio_global:.2f}** ({'mai mult hedging' if hedge_cert_ratio_global > 1 else 'mai mult certitudine'})\n")

    md.append("## Aggregate per perioadă\n")
    md.append(agg.to_markdown())

    md.append("\n## Lexicon utilizat\n")
    md.append(f"**Hedging ({len(HEDGING)} markeri)**: {', '.join(HEDGING[:10])} ...")
    md.append(f"\n**Certitudine ({len(CERTITUDINE)} markeri)**: {', '.join(CERTITUDINE[:10])} ...")
    md.append(f"\n**Personal ({len(PERSONAL)} markeri)**: {', '.join(PERSONAL[:10])} ...")

    # Plot evolution
    period_order = sorted(df["period"].unique())
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    for ax, metric, color, label in zip(
        axes,
        ["hedge_per_1000w", "cert_per_1000w", "hedge_cert_ratio"],
        ["#3a86ff", "#e74c3c", "#27ae60"],
        ["Hedging / 1000w", "Certitudine / 1000w", "Hedge:Cert ratio"],
    ):
        means = [df[df["period"] == p][metric].mean() for p in period_order]
        ax.bar(range(len(period_order)), means, color=color)
        ax.set_xticks(range(len(period_order)))
        ax.set_xticklabels([p.split(" ", 1)[0] for p in period_order], rotation=30, ha="right")
        ax.set_title(label, fontsize=12)
        ax.grid(alpha=0.3, axis="y")
    fig.suptitle(f"Hedging vs Certitudine — evoluție temporală ({PROJECTION})", fontsize=14)
    fig.tight_layout()
    fig.savefig(OUT / "hedging_evolution.png", dpi=120, bbox_inches="tight")
    plt.close(fig)

    (OUT / "summary.md").write_text("\n".join(md))
    print(f"Output: {OUT}/")


if __name__ == "__main__":
    main()
