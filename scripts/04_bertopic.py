"""Pasul 3: Topic modeling cu BERTopic.

Folosește sentence-transformers multilingual pentru embeddings + UMAP + HDBSCAN
pentru clustering + c-TF-IDF pentru etichete de topic.

Output:
  - results/03_topics/topics_summary.md   — toate topicele cu top 10 cuvinte
  - results/03_topics/topics_summary.csv  — tabular
  - results/03_topics/topic_per_doc.csv   — mapping doc → topic
  - results/03_topics/topic_over_time.csv — frecvență per topic per perioadă
  - results/03_topics/topics_over_time.html — vizualizare interactivă
  - results/03_topics/barchart.html        — top words per topic
  - results/03_topics/heatmap.html         — similarități între topice
"""
from __future__ import annotations

from pathlib import Path
from datetime import datetime

import pandas as pd

from corpus import load_corpus, get_stopwords

OUT = Path(__file__).resolve().parent.parent / "results" / "03_topics"
OUT.mkdir(parents=True, exist_ok=True)

# Multilingual sentence transformer — best quality for Romanian
EMBED_MODEL = "paraphrase-multilingual-mpnet-base-v2"
# Min cluster size: lower = more granular topics, higher = fewer broader topics
MIN_TOPIC_SIZE = 10


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


def main():
    from bertopic import BERTopic
    from sentence_transformers import SentenceTransformer
    from sklearn.feature_extraction.text import CountVectorizer

    speeches = load_corpus()
    print(f"Loaded {len(speeches)} docs")

    # Use ND-only voice
    docs = [s.nd_only_text for s in speeches]
    timestamps = [s.date for s in speeches]
    ids = [s.id for s in speeches]
    periods = [period_for(s.date) for s in speeches]

    # Filter out very short docs (< 30 words) — they confuse topic clustering
    keep_idx = [i for i, d in enumerate(docs) if len(d.split()) >= 30]
    docs = [docs[i] for i in keep_idx]
    timestamps = [timestamps[i] for i in keep_idx]
    ids = [ids[i] for i in keep_idx]
    periods = [periods[i] for i in keep_idx]
    print(f"Filtered to {len(docs)} docs (≥30 words)")

    # Embeddings (multilingual mpnet)
    print(f"Loading embedding model: {EMBED_MODEL}")
    embed_model = SentenceTransformer(EMBED_MODEL)

    # Romanian stopwords for c-TF-IDF (topic label generation)
    sw = list(get_stopwords())
    # Custom vectorizer to use our RO stopwords for topic labels
    vectorizer_model = CountVectorizer(
        stop_words=sw,
        min_df=2,
        ngram_range=(1, 2),  # uni + bigrams
        token_pattern=r"[a-zA-ZăâîșțĂÂÎȘȚ]{3,}",
    )

    # BERTopic config
    topic_model = BERTopic(
        embedding_model=embed_model,
        vectorizer_model=vectorizer_model,
        min_topic_size=MIN_TOPIC_SIZE,
        nr_topics="auto",  # let BERTopic auto-reduce
        language="multilingual",
        verbose=True,
        calculate_probabilities=False,
    )

    print("Fitting BERTopic (embeddings + UMAP + HDBSCAN + c-TF-IDF)...")
    topics, _ = topic_model.fit_transform(docs)

    # Topics summary
    info = topic_model.get_topic_info()
    print(f"\nDiscovered {len(info)} topics (incl. outlier topic -1)")
    info.to_csv(OUT / "topics_summary.csv", index=False)

    # Per-doc topic mapping
    doc_df = pd.DataFrame({
        "id": ids,
        "date": timestamps,
        "period": periods,
        "topic": topics,
    })
    doc_df.to_csv(OUT / "topic_per_doc.csv", index=False)

    # Markdown summary of all topics
    lines = ["# Pasul 3 — Topic Modeling (BERTopic)\n"]
    lines.append(f"- **{len(info)} topice descoperite** (incl. outlier topic -1)")
    lines.append(f"- Documente procesate: **{len(docs)}** (filtru ≥30 cuvinte)")
    lines.append(f"- Embedding model: `{EMBED_MODEL}`")
    lines.append(f"- Min cluster size: {MIN_TOPIC_SIZE}\n")

    lines.append("## Toate topicele descoperite\n")
    for _, row in info.iterrows():
        topic_id = row["Topic"]
        count = row["Count"]
        if topic_id == -1:
            label = "OUTLIERS (necategorizate)"
        else:
            top_words = topic_model.get_topic(topic_id)
            label = " · ".join(w for w, _ in top_words[:10])
        lines.append(f"### Topic {topic_id} ({count} docs)")
        lines.append(f"{label}\n")

    # Topic over time — pe perioadele noastre politice
    print("\nComputing topic frequencies per period...")
    period_topic = doc_df.groupby(["period", "topic"]).size().reset_index(name="count")
    period_topic.to_csv(OUT / "topic_over_time.csv", index=False)

    lines.append("\n## Distribuție topice per perioadă politică\n")
    pivot = period_topic.pivot_table(
        index="topic", columns="period", values="count", fill_value=0
    )
    # Add topic label as column
    topic_labels = {}
    for _, row in info.iterrows():
        tid = row["Topic"]
        if tid == -1:
            topic_labels[tid] = "OUTLIERS"
        else:
            tw = topic_model.get_topic(tid)
            topic_labels[tid] = " · ".join(w for w, _ in tw[:4])
    pivot["label"] = pivot.index.map(topic_labels)
    pivot.to_csv(OUT / "topic_period_matrix.csv")

    # For markdown: show top 15 topics by total count
    pivot["total"] = pivot.drop(columns=["label"]).sum(axis=1)
    top_pivot = pivot.sort_values("total", ascending=False).head(20)
    cols = list(top_pivot.columns)
    cols_pretty = [c for c in cols if c not in ("label", "total")] + ["total"]
    rows = []
    for tid, row in top_pivot.iterrows():
        if tid == -1:
            continue
        rows.append((tid, row["label"], *[int(row.get(c, 0)) for c in cols_pretty]))
    df_md = pd.DataFrame(rows, columns=["topic", "label", *cols_pretty])
    lines.append(df_md.to_markdown(index=False))

    # BERTopic-native topics_over_time (for visualization)
    print("\nGenerating BERTopic topics_over_time...")
    timestamps_dt = [datetime.strptime(t, "%Y-%m-%d") for t in timestamps]
    topics_over_time = topic_model.topics_over_time(docs, timestamps_dt, nr_bins=18)
    topics_over_time.to_csv(OUT / "topics_over_time_bertopic.csv", index=False)

    # Interactive visualizations
    print("Generating interactive HTML visualizations...")
    try:
        fig = topic_model.visualize_topics_over_time(topics_over_time, top_n_topics=20)
        fig.write_html(OUT / "topics_over_time.html")
        print(f"  ✓ topics_over_time.html")
    except Exception as e:
        print(f"  ✗ topics_over_time.html: {e}")

    try:
        fig = topic_model.visualize_barchart(top_n_topics=20, n_words=8)
        fig.write_html(OUT / "barchart.html")
        print(f"  ✓ barchart.html")
    except Exception as e:
        print(f"  ✗ barchart.html: {e}")

    try:
        fig = topic_model.visualize_heatmap(top_n_topics=30)
        fig.write_html(OUT / "heatmap.html")
        print(f"  ✓ heatmap.html")
    except Exception as e:
        print(f"  ✗ heatmap.html: {e}")

    try:
        fig = topic_model.visualize_topics()
        fig.write_html(OUT / "topics_2d.html")
        print(f"  ✓ topics_2d.html")
    except Exception as e:
        print(f"  ✗ topics_2d.html: {e}")

    # Save the model itself for future use
    try:
        topic_model.save(str(OUT / "bertopic_model"), serialization="safetensors",
                         save_embedding_model=False)
        print(f"  ✓ bertopic_model/ (model saved)")
    except Exception as e:
        print(f"  ✗ model save: {e}")

    (OUT / "topics_summary.md").write_text("\n".join(lines))
    print(f"\nDone. Outputs in {OUT.relative_to(Path.cwd())}/")


if __name__ == "__main__":
    main()
