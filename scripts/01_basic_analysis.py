"""Step 1: Basic stats + combined wordclouds + per-period wordclouds.

Per-doc PNGs au fost scoase (4000+ fișiere inutile la corpus mare). Acum
generăm doar:
  - stats.csv            — per-doc stats (id, data, tip, word count, TTR)
  - summary.md           — tabel + top 30 cuvinte per perioadă + corpus
  - wordcloud_all.png    — corpus combinat
  - top30_all.png        — bar chart top 30 corpus
  - wordcloud_<period>.png — câte unul per perioadă (6 perioade)
  - top20_<period>.png   — top 20 cuvinte per perioadă

Outputs land in results/01_basic_<PROJECTION>/ (controled by PROJECTION env var
in corpus.py).
"""
from __future__ import annotations

import os
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

from corpus import Speech, get_stopwords, load_corpus, tokenize

OUT = Path(__file__).resolve().parent.parent / "results" / f"01_basic_{os.getenv('PROJECTION', 'overall')}"
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


def per_speech_stats(s: Speech) -> dict:
    raw_tokens = tokenize(s.nd_only_text, lemmatize=False, remove_stopwords=False)
    clean_lemmas = tokenize(s.nd_only_text, lemmatize=True, remove_stopwords=True)
    return {
        "id": s.id,
        "data": s.date,
        "tip": s.tip,
        "period": period_for(s.date),
        "n_words_raw": len(raw_tokens),
        "n_lemmas_clean": len(clean_lemmas),
        "n_unique_lemmas": len(set(clean_lemmas)),
        "ttr_lemma": round(len(set(clean_lemmas)) / max(len(clean_lemmas), 1), 3),
        "n_sentences": s.nd_only_text.count(".") + s.nd_only_text.count("!") + s.nd_only_text.count("?"),
    }


def top_n(tokens: list[str], n: int = 20) -> list[tuple[str, int]]:
    return Counter(tokens).most_common(n)


def slugify(period: str) -> str:
    """Make period name a safe filename."""
    return period.replace(" ", "_").replace("+", "and").replace(",", "").lower()


def make_wordcloud(tokens: list[str], outpath: Path, title: str) -> None:
    freq = Counter(tokens)
    if not freq:
        return
    wc = WordCloud(
        width=1400, height=800, background_color="white", colormap="viridis",
        prefer_horizontal=0.9, max_words=120, random_state=42,
    ).generate_from_frequencies(freq)
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    ax.set_title(title, fontsize=16, pad=12)
    fig.tight_layout()
    fig.savefig(outpath, dpi=120, bbox_inches="tight")
    plt.close(fig)


def make_bar_top(top: list[tuple[str, int]], outpath: Path, title: str) -> None:
    if not top:
        return
    words = [w for w, _ in top][::-1]
    counts = [c for _, c in top][::-1]
    fig, ax = plt.subplots(figsize=(9, max(7, len(words) * 0.3)))
    ax.barh(words, counts, color="#3a86ff")
    ax.set_title(title, fontsize=14, pad=10)
    ax.set_xlabel("frecvență")
    for i, v in enumerate(counts):
        ax.text(v + 0.05, i, str(v), va="center", fontsize=9)
    fig.tight_layout()
    fig.savefig(outpath, dpi=120, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    projection = os.getenv("PROJECTION", "overall")
    speeches = load_corpus()
    print(f"Loaded {len(speeches)} speeches (projection={projection}).\n")

    # Per-speech stats
    rows = [per_speech_stats(s) for s in speeches]
    df = pd.DataFrame(rows)
    df.to_csv(OUT / "stats.csv", index=False)

    # Tokenize once per speech, group by period
    period_tokens: dict[str, list[str]] = {}
    all_tokens: list[str] = []
    for s in speeches:
        tokens = tokenize(s.nd_only_text, lemmatize=True, remove_stopwords=True)
        all_tokens.extend(tokens)
        period_tokens.setdefault(period_for(s.date), []).extend(tokens)

    # Combined corpus wordcloud + top 30
    make_wordcloud(all_tokens, OUT / "wordcloud_all.png",
                   f"Corpus integral ({projection}) — wordcloud combinat")
    combined_top = top_n(all_tokens, 30)
    make_bar_top(combined_top, OUT / "top30_all.png",
                 f"Top 30 — corpus integral ({projection})")

    # Per-period wordcloud + top 20
    period_tops: dict[str, list[tuple[str, int]]] = {}
    for period, toks in sorted(period_tokens.items()):
        slug = slugify(period)
        make_wordcloud(toks, OUT / f"wordcloud_{slug}.png",
                       f"{period} — wordcloud ({projection})")
        top = top_n(toks, 20)
        period_tops[period] = top
        make_bar_top(top, OUT / f"top20_{slug}.png",
                     f"Top 20 — {period} ({projection})")

    # Summary markdown
    lines: list[str] = []
    lines.append(f"# Pasul 1 — Statistici de bază ({projection})\n")
    lines.append(f"**Documente**: {len(speeches)} | **Cuvinte raw**: {df['n_words_raw'].sum():,} | "
                 f"**Lemmas clean**: {df['n_lemmas_clean'].sum():,}\n")
    lines.append("\n## Sumar per perioadă\n")
    period_stats = df.groupby("period").agg(
        docs=("id", "count"),
        words=("n_words_raw", "sum"),
        lemmas=("n_lemmas_clean", "sum"),
        unique_lemmas=("n_unique_lemmas", "sum"),
    )
    lines.append(period_stats.to_markdown())
    lines.append("\n## Top 30 cuvinte — corpus integral\n")
    lines.append(pd.DataFrame(combined_top, columns=["cuvânt", "frecvență"]).to_markdown(index=False))
    lines.append("\n## Top 20 cuvinte per perioadă\n")
    for period, top in period_tops.items():
        n_docs = (df["period"] == period).sum()
        lines.append(f"### {period} ({n_docs} docs)\n")
        lines.append(pd.DataFrame(top, columns=["cuvânt", "frecvență"]).to_markdown(index=False))
        lines.append("")
    lines.append("\n## Note metodologice\n")
    lines.append(f"- **Projection**: `{projection}` (sursă: `data/3_nd_{projection}/`)")
    lines.append("- **Tokenizare + lemmatizare**: spaCy `ro_core_news_sm`, formă canonică.")
    lines.append(f"- **Stopwords**: `stopwordsiso` RO ({len(get_stopwords())} cuvinte) + cardinali.")
    lines.append("- **Numerele și punctuația** eliminate; diacriticele normalizate.")
    lines.append("- **Per-doc PNG-uri NU se generează** la corpus mare — folosește `stats.csv` + "
                 "`results/02_tfidf_<projection>/tfidf_top_per_doc.md` pentru inspecție per doc.")

    (OUT / "summary.md").write_text("\n".join(lines))
    print(f"Outputs in: {OUT}/")
    print(f"  - stats.csv ({len(speeches)} rows)")
    print(f"  - summary.md")
    print(f"  - wordcloud_all.png + top30_all.png")
    print(f"  - wordcloud_<period>.png + top20_<period>.png × {len(period_tokens)}")


if __name__ == "__main__":
    main()
