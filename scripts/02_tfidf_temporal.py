"""Step 2: TF-IDF distinctive words + bigrams + temporal evolution.

Outputs in results/02_tfidf/:
  - tfidf_top_per_doc.md       — top 15 most distinctive lemmas per document
  - bigrams_top_per_doc.md     — top 10 bigrams per document
  - tfidf_by_period.md         — distinctive lemmas per quarter (temporal evolution)
  - bigrams_by_period.md       — top bigrams per quarter
  - period_stats.csv           — words/lemmas/docs per quarter
"""
from __future__ import annotations

from collections import Counter
import os
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from corpus import Speech, load_corpus, tokenize

OUT = Path(__file__).resolve().parent.parent / "results" / f"02_tfidf_{os.getenv('PROJECTION', 'overall')}"
OUT.mkdir(parents=True, exist_ok=True)


def period_for(date_str: str) -> str:
    """Map YYYY-MM-DD to a coarse period label."""
    y, m = int(date_str[:4]), int(date_str[5:7])
    # Define periods aligned with key political moments
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


def tokenize_for_tfidf(text: str) -> list[str]:
    """spaCy lemmatized + stopwords + min len."""
    return tokenize(text, lemmatize=True, remove_stopwords=True, min_len=3)


def build_docs_df(speeches: list[Speech]) -> pd.DataFrame:
    rows = []
    for s in speeches:
        lemmas = tokenize_for_tfidf(s.nd_only_text)
        rows.append({
            "id": s.id,
            "data": s.date,
            "tip": s.tip,
            "period": period_for(s.date),
            "lemmas": lemmas,
            "joined": " ".join(lemmas),
            "n_words": len(s.nd_only_text.split()),
            "n_lemmas": len(lemmas),
        })
    return pd.DataFrame(rows)


def top_tfidf_per_doc(df: pd.DataFrame, top_n: int = 15) -> dict[str, list[tuple[str, float]]]:
    vec = TfidfVectorizer(min_df=2, max_df=0.85, token_pattern=r"\S+")
    X = vec.fit_transform(df["joined"])
    vocab = vec.get_feature_names_out()
    out: dict[str, list[tuple[str, float]]] = {}
    for i, row in df.iterrows():
        vec_i = X[i].toarray().flatten()
        top_idx = vec_i.argsort()[-top_n:][::-1]
        out[row["id"]] = [(vocab[j], float(vec_i[j])) for j in top_idx if vec_i[j] > 0]
    return out


def get_bigrams(lemmas: list[str], top_n: int = 10) -> list[tuple[str, int]]:
    bigrams = [f"{a} {b}" for a, b in zip(lemmas, lemmas[1:])]
    return Counter(bigrams).most_common(top_n)


def tfidf_by_period(df: pd.DataFrame, top_n: int = 25) -> dict[str, list[tuple[str, float]]]:
    """Aggregate documents per period, then compute TF-IDF across periods."""
    grouped = df.groupby("period")["lemmas"].sum()
    period_docs = grouped.tolist()
    period_names = grouped.index.tolist()
    period_joined = [" ".join(lems) for lems in period_docs]

    vec = TfidfVectorizer(min_df=1, max_df=0.85, token_pattern=r"\S+")
    X = vec.fit_transform(period_joined)
    vocab = vec.get_feature_names_out()
    out: dict[str, list[tuple[str, float]]] = {}
    for i, period in enumerate(period_names):
        vec_i = X[i].toarray().flatten()
        top_idx = vec_i.argsort()[-top_n:][::-1]
        out[period] = [(vocab[j], float(vec_i[j])) for j in top_idx if vec_i[j] > 0]
    return out


def main() -> None:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--only-verified", action="store_true")
    args = ap.parse_args()

    speeches = load_corpus()
    if args.only_verified:
        speeches = [s for s in speeches if s.verificat]
    print(f"Loaded {len(speeches)} speeches.")

    df = build_docs_df(speeches)
    print(f"Periods: {df['period'].value_counts().to_dict()}")

    # Per-doc TF-IDF
    doc_tfidf = top_tfidf_per_doc(df, top_n=15)
    lines = ["# Pasul 2 — TF-IDF distinctive lemmas per document\n"]
    for _, row in df.iterrows():
        lines.append(f"## {row['data']} — {row['tip']}\n")
        lines.append(f"_File: `{row['id']}` · {row['n_lemmas']} clean lemmas_\n")
        top = doc_tfidf.get(row["id"], [])
        if top:
            tbl = pd.DataFrame(top, columns=["lemmă", "TF-IDF"])
            tbl["TF-IDF"] = tbl["TF-IDF"].round(3)
            lines.append(tbl.to_markdown(index=False))
        lines.append("")
    (OUT / "tfidf_top_per_doc.md").write_text("\n".join(lines))

    # Per-doc bigrams
    lines = ["# Top 10 bigrame per document\n"]
    for _, row in df.iterrows():
        lines.append(f"## {row['data']} — {row['tip']}\n")
        bigrams = get_bigrams(row["lemmas"], top_n=10)
        if bigrams:
            tbl = pd.DataFrame(bigrams, columns=["bigramă", "frecvență"])
            lines.append(tbl.to_markdown(index=False))
        lines.append("")
    (OUT / "bigrams_top_per_doc.md").write_text("\n".join(lines))

    # Per-period TF-IDF
    period_tfidf = tfidf_by_period(df, top_n=25)
    lines = ["# Pasul 2 — TF-IDF distinctive lemmas pe perioadă\n"]
    lines.append("Documentele sunt agregate per trimestru; TF-IDF e calculat între perioade pentru a găsi cuvintele specifice fiecărei etape.\n")
    for period, top in period_tfidf.items():
        n_docs = (df["period"] == period).sum()
        lines.append(f"## {period}  ({n_docs} documente)\n")
        if top:
            tbl = pd.DataFrame(top, columns=["lemmă", "TF-IDF"])
            tbl["TF-IDF"] = tbl["TF-IDF"].round(3)
            lines.append(tbl.to_markdown(index=False))
        lines.append("")
    (OUT / "tfidf_by_period.md").write_text("\n".join(lines))

    # Period stats CSV
    period_stats = df.groupby("period").agg(
        n_docs=("id", "count"),
        total_words=("n_words", "sum"),
        total_lemmas=("n_lemmas", "sum"),
    )
    period_stats.to_csv(OUT / "period_stats.csv")
    print("\n=== Period stats ===")
    print(period_stats.to_string())
    print(f"\nOutputs in: {OUT.relative_to(Path.cwd())}/")


if __name__ == "__main__":
    main()
