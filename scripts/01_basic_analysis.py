"""Step 1: Basic stats + word clouds + top-N words per speech.

Outputs land in results/01_basic/:
  - summary.md           — corpus overview + top-20 words per speech
  - stats.csv            — per-speech stats
  - wordcloud_<id>.png   — one wordcloud per speech
  - wordcloud_all.png    — combined wordcloud across corpus
  - top20_<id>.png       — bar chart top 20 words per speech
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

from corpus import Speech, get_stopwords, load_corpus, tokenize

OUT = Path(__file__).resolve().parent.parent / "results" / "01_basic"
OUT.mkdir(parents=True, exist_ok=True)


def per_speech_stats(s: Speech) -> dict:
    raw_tokens = tokenize(s.nd_only_text, lemmatize=False, remove_stopwords=False)
    clean_lemmas = tokenize(s.nd_only_text, lemmatize=True, remove_stopwords=True)
    return {
        "id": s.id,
        "data": s.date,
        "tip": s.tip,
        "n_words_raw": len(raw_tokens),
        "n_lemmas_clean": len(clean_lemmas),
        "n_unique_lemmas": len(set(clean_lemmas)),
        "ttr_lemma": round(len(set(clean_lemmas)) / max(len(clean_lemmas), 1), 3),
        "n_sentences": s.nd_only_text.count(".") + s.nd_only_text.count("!") + s.nd_only_text.count("?"),
    }


def top_n(tokens: list[str], n: int = 20) -> list[tuple[str, int]]:
    return Counter(tokens).most_common(n)


def make_wordcloud(tokens: list[str], outpath: Path, title: str) -> None:
    freq = Counter(tokens)
    if not freq:
        return
    wc = WordCloud(
        width=1400,
        height=800,
        background_color="white",
        colormap="viridis",
        prefer_horizontal=0.9,
        max_words=120,
        random_state=42,
    ).generate_from_frequencies(freq)
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    ax.set_title(title, fontsize=16, pad=12)
    fig.tight_layout()
    fig.savefig(outpath, dpi=120, bbox_inches="tight")
    plt.close(fig)


def make_bar_top20(top: list[tuple[str, int]], outpath: Path, title: str) -> None:
    if not top:
        return
    words = [w for w, _ in top][::-1]
    counts = [c for _, c in top][::-1]
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.barh(words, counts, color="#3a86ff")
    ax.set_title(title, fontsize=14, pad=10)
    ax.set_xlabel("frecvență")
    for i, v in enumerate(counts):
        ax.text(v + 0.05, i, str(v), va="center", fontsize=9)
    fig.tight_layout()
    fig.savefig(outpath, dpi=120, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--only-verified", action="store_true",
                    help="Run only on files with verificat=true (pure ND voice).")
    args = ap.parse_args()

    speeches = load_corpus()
    if args.only_verified:
        speeches = [s for s in speeches if s.verificat]
        suffix = "_verified"
    else:
        suffix = ""
    print(f"Loaded {len(speeches)} speeches{' (verified only)' if args.only_verified else ''}.\n")
    global OUT
    if args.only_verified:
        OUT = OUT.parent / f"01_basic_verified"
        OUT.mkdir(parents=True, exist_ok=True)

    # Per-speech stats
    rows = [per_speech_stats(s) for s in speeches]
    df = pd.DataFrame(rows)
    df.to_csv(OUT / "stats.csv", index=False)
    print(df.to_string(index=False))

    # Per-speech top-20 + wordclouds
    per_speech_top: dict[str, list[tuple[str, int]]] = {}
    all_tokens: list[str] = []
    for s in speeches:
        tokens = tokenize(s.nd_only_text, lemmatize=True, remove_stopwords=True)
        all_tokens.extend(tokens)
        top = top_n(tokens, 20)
        per_speech_top[s.id] = top
        title = f"{s.date} · {s.tip}"
        make_wordcloud(tokens, OUT / f"wordcloud_{s.id}.png", title)
        make_bar_top20(top, OUT / f"top20_{s.id}.png", f"Top 20 — {title}")

    # Combined wordcloud
    make_wordcloud(all_tokens, OUT / "wordcloud_all.png", "Corpus integral — wordcloud combinat")
    combined_top = top_n(all_tokens, 30)
    make_bar_top20(combined_top, OUT / "top20_all.png", "Top 30 — corpus integral")

    # Markdown summary
    lines: list[str] = []
    lines.append("# Pasul 1 — Statistici de bază + word clouds\n")
    lines.append("## Sumar corpus\n")
    lines.append(df.to_markdown(index=False))
    lines.append("\n## Top 20 cuvinte per discurs\n")
    for s in speeches:
        lines.append(f"### {s.date} — {s.tip}\n")
        top = per_speech_top[s.id]
        tbl = pd.DataFrame(top, columns=["cuvânt", "frecvență"])
        lines.append(tbl.to_markdown(index=False))
        lines.append("")
    lines.append("\n## Top 30 cuvinte — corpus integral\n")
    lines.append(pd.DataFrame(combined_top, columns=["cuvânt", "frecvență"]).to_markdown(index=False))
    lines.append("\n## Stopwords folosite\n")
    sw = get_stopwords()
    lines.append(f"Listă **stopwordsiso RO** ({len(sw)} cuvinte) + domain extras (cardinali, "
                 "câteva auxiliare nestockate).\n")
    lines.append("\n## Note metodologice\n")
    lines.append("- **Tokenizare + lemmatizare**: spaCy `ro_core_news_sm`. Token-ele sunt reduse la "
                 "lemma (formă canonică): `românia/româniei/român/români` → `românia`/`român`, "
                 "`anunț/anunțul` → `anunța`, `săptămânile` → `săptămână`.")
    lines.append("- **Stopwords**: `stopwordsiso` (RO) + extensii pentru cardinali și conjuncții "
                 "scurte.")
    lines.append("- **Numerele și punctuația** sunt eliminate; diacriticele cedilă (ş, ţ) sunt "
                 "normalizate la virgulă-below (ș, ț).")
    lines.append("- **TTR** (type-token ratio) e biased de lungime — discursurile scurte au TTR "
                 "mai mare. Util doar comparativ pe lungimi similare.")

    (OUT / "summary.md").write_text("\n".join(lines))
    print(f"\nOutputs in: {OUT}/")


if __name__ == "__main__":
    main()
