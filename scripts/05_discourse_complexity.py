"""Pasul 5: Discourse complexity metrics — sentence length, tree depth, lexical diversity.

Pentru fiecare doc + agregat per perioadă × proiecție (overall/scris/vorbit):
  - n sentences, mean/std/p95 sentence length (în token-uri)
  - dependency tree depth (cu spaCy parser)
  - Type-Token Ratio (TTR) + MTLD (lexical diversity robust la length)
  - Mean word length
  - Function word ratio (markeri ai complexității stilistice)

Evoluție: a simplificat sau a complexificat ND discursul post-mandat?

Run (3 proiecții):
    for p in overall scris vorbit; do PROJECTION=$p python scripts/05_discourse_complexity.py; done
"""
from __future__ import annotations

import os
import statistics
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import spacy

from corpus import _normalize_diacritics, load_corpus

PROJECTION = os.getenv("PROJECTION", "overall")
OUT = Path(__file__).resolve().parent.parent / "results" / f"05_complexity_{PROJECTION}"
OUT.mkdir(parents=True, exist_ok=True)


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


def tree_depth(token) -> int:
    """Max depth from token to root."""
    d = 0
    while token.head != token:
        d += 1
        token = token.head
    return d


def compute_mtld(tokens: list[str], threshold: float = 0.72) -> float:
    """MTLD — robust lexical diversity, invariant to text length.

    Cf. McCarthy & Jarvis 2010. Walks forward, counts factors where TTR drops below threshold.
    Returns average factor length (higher = more diverse).
    """
    if len(tokens) < 50:
        return 0.0

    def factors_forward(toks: list[str]) -> float:
        factor_count = 0
        types: set[str] = set()
        token_count = 0
        for t in toks:
            types.add(t)
            token_count += 1
            ttr = len(types) / token_count
            if ttr <= threshold:
                factor_count += 1
                types.clear()
                token_count = 0
        if token_count > 0:
            partial = (1 - ttr) / (1 - threshold)
            factor_count += partial
        return len(toks) / factor_count if factor_count > 0 else len(toks)

    fwd = factors_forward(tokens)
    rev = factors_forward(tokens[::-1])
    return (fwd + rev) / 2


def analyze_doc(text: str, nlp) -> dict:
    text = _normalize_diacritics(text)
    if not text.strip():
        return {}
    doc = nlp(text)
    sentences = list(doc.sents)
    if not sentences:
        return {}

    # Sentence-level
    sent_lengths = [len([t for t in s if not t.is_punct and not t.is_space]) for s in sentences]
    sent_lengths = [n for n in sent_lengths if n > 0]
    if not sent_lengths:
        return {}

    # Token-level
    word_tokens = [t for t in doc if not t.is_punct and not t.is_space and not t.like_num]
    word_lemmas = [_normalize_diacritics(t.lemma_.lower()) for t in word_tokens]
    word_surfaces = [_normalize_diacritics(t.text.lower()) for t in word_tokens]
    word_lengths = [len(t.text) for t in word_tokens]

    # Dependency tree depth per sentence
    depths = []
    for s in sentences:
        if len(s) > 0:
            max_d = max(tree_depth(t) for t in s)
            depths.append(max_d)

    # Function word ratio (function = closed-class POS: ADP, AUX, CCONJ, DET, PART, PRON, SCONJ)
    func_pos = {"ADP", "AUX", "CCONJ", "DET", "PART", "PRON", "SCONJ"}
    n_func = sum(1 for t in word_tokens if t.pos_ in func_pos)
    func_ratio = n_func / max(len(word_tokens), 1)

    ttr = len(set(word_lemmas)) / max(len(word_lemmas), 1)
    mtld = compute_mtld(word_lemmas)

    return {
        "n_sentences": len(sent_lengths),
        "n_words": len(word_tokens),
        "n_unique_lemmas": len(set(word_lemmas)),
        "sent_len_mean": statistics.mean(sent_lengths),
        "sent_len_std": statistics.stdev(sent_lengths) if len(sent_lengths) > 1 else 0,
        "sent_len_p95": sorted(sent_lengths)[int(0.95 * (len(sent_lengths) - 1))],
        "word_len_mean": statistics.mean(word_lengths) if word_lengths else 0,
        "tree_depth_mean": statistics.mean(depths) if depths else 0,
        "tree_depth_max": max(depths) if depths else 0,
        "ttr_lemma": ttr,
        "mtld": mtld,
        "func_ratio": func_ratio,
    }


def main():
    speeches = load_corpus()
    print(f"Loaded {len(speeches)} docs (projection={PROJECTION}).")
    nlp = spacy.load("ro_core_news_sm")
    # Enable parser for dependency tree depth
    if "parser" in nlp.disabled:
        nlp.enable_pipe("parser")

    rows = []
    for i, s in enumerate(speeches):
        if i and i % 100 == 0:
            print(f"  [{i}/{len(speeches)}]")
        metrics = analyze_doc(s.nd_only_text, nlp)
        if not metrics:
            continue
        rows.append({"id": s.id, "date": s.date, "tip": s.tip,
                     "period": period_for(s.date), **metrics})

    df = pd.DataFrame(rows)
    df.to_csv(OUT / "complexity_per_doc.csv", index=False)
    print(f"\nPer-doc CSV: {len(df)} rows")

    # Aggregate per period
    agg = df.groupby("period").agg({
        "n_words": "sum",
        "n_sentences": "sum",
        "sent_len_mean": ["mean", "std"],
        "tree_depth_mean": ["mean", "std"],
        "ttr_lemma": "mean",
        "mtld": "mean",
        "func_ratio": "mean",
        "word_len_mean": "mean",
        "id": "count",
    }).round(3)
    agg.columns = [f"{a}_{b}" if b else a for a, b in agg.columns]
    agg = agg.rename(columns={"id_count": "docs"})
    agg.to_csv(OUT / "complexity_per_period.csv")

    # Markdown summary
    md = [f"# Pasul 5 — Discourse complexity ({PROJECTION})\n"]
    md.append(f"**Docs analizate**: {len(df)} | total words: {df['n_words'].sum():,} | "
              f"total sentences: {df['n_sentences'].sum():,}\n")
    md.append("## Aggregate per perioadă\n")
    md.append(agg.to_markdown())

    md.append("\n## Métrici explicate\n")
    md.append("- **sent_len_mean**: lungime medie a propoziției (token-uri non-punctuație)")
    md.append("- **tree_depth_mean**: adâncimea medie a arborelui de dependență (proxy de complexitate sintactică)")
    md.append("- **ttr_lemma**: type-token ratio pe leme (0-1, mai mare = vocabular mai divers)")
    md.append("- **mtld**: Measure of Textual Lexical Diversity (robust la length, valori tipice 50-150)")
    md.append("- **func_ratio**: proporție de cuvinte funcționale (proxy pentru stil simplu — mai sus = mai simplu)")
    md.append("- **word_len_mean**: lungime medie cuvânt (caractere)")

    # Plot evolution
    df["period_short"] = df["period"].str.extract(r"^(\S+)")[0]
    period_order = sorted(df["period"].unique())
    metrics_to_plot = ["sent_len_mean", "tree_depth_mean", "mtld", "ttr_lemma"]
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    for ax, metric in zip(axes.flat, metrics_to_plot):
        means = [df[df["period"] == p][metric].mean() for p in period_order]
        stds = [df[df["period"] == p][metric].std() for p in period_order]
        x = list(range(len(period_order)))
        ax.errorbar(x, means, yerr=stds, fmt="o-", capsize=4, color="#3a86ff")
        ax.set_xticks(x)
        ax.set_xticklabels([p.split(" ", 1)[0] for p in period_order], rotation=30, ha="right")
        ax.set_title(metric, fontsize=12)
        ax.grid(alpha=0.3)
    fig.suptitle(f"Evoluție complexitate discurs ({PROJECTION})", fontsize=14)
    fig.tight_layout()
    fig.savefig(OUT / "complexity_evolution.png", dpi=120, bbox_inches="tight")
    plt.close(fig)

    (OUT / "summary.md").write_text("\n".join(md))
    print(f"\nOutput: {OUT}/")
    print(f"  - complexity_per_doc.csv ({len(df)} rows)")
    print(f"  - complexity_per_period.csv")
    print(f"  - complexity_evolution.png")
    print(f"  - summary.md")


if __name__ == "__main__":
    main()
