"""Step 3: BERTopic — neural topic modeling pe corpus.

Pipeline:
  1. Embed cu multilingual-e5-large (sau e5-base fallback dacă VRAM mic)
     - prefix "passage: " obligatoriu pentru e5 family
  2. UMAP → 5 dim (păstrează structură semantică)
  3. HDBSCAN clustering (descoperă k automat)
  4. c-TF-IDF labels (cu stopwords RO din corpus.py)
  5. Output: topics.csv, topic_info.md, topics_over_time.png

Run:
    PROJECTION=overall python scripts/03_bertopic.py
    PROJECTION=scris   python scripts/03_bertopic.py
    PROJECTION=vorbit  python scripts/03_bertopic.py
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import torch
from bertopic import BERTopic
from hdbscan import HDBSCAN
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer
from umap import UMAP

from corpus import _normalize_diacritics, get_stopwords, load_corpus

PROJECTION = os.getenv("PROJECTION", "overall")
OUT = Path(__file__).resolve().parent.parent / "results" / f"03_bertopic_{PROJECTION}"
OUT.mkdir(parents=True, exist_ok=True)


def pick_model() -> tuple[str, str]:
    """Choose embedding model based on VRAM. Returns (model_id, label)."""
    if not torch.cuda.is_available():
        return "intfloat/multilingual-e5-base", "e5-base (CPU)"
    free, total = torch.cuda.mem_get_info(0)
    free_gb = free / 1e9
    print(f"GPU: {torch.cuda.get_device_name(0)} | free VRAM: {free_gb:.2f}GB")
    if free_gb >= 2.5:
        return "intfloat/multilingual-e5-large", "e5-large (GPU fp16)"
    return "intfloat/multilingual-e5-base", "e5-base (GPU)"


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


def main() -> None:
    speeches = load_corpus()
    print(f"Loaded {len(speeches)} speeches (projection={PROJECTION}).")

    # E5 family REQUIRES "passage: " prefix on documents
    raw_docs = [_normalize_diacritics(s.nd_only_text) for s in speeches]
    embed_input = [f"passage: {d}" for d in raw_docs]
    ids = [s.id for s in speeches]
    dates = [s.date for s in speeches]
    periods = [period_for(s.date) for s in speeches]

    model_id, label = pick_model()
    print(f"Embedding model: {label} ({model_id})")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    encoder = SentenceTransformer(model_id, device=device)
    if device == "cuda":
        encoder = encoder.half()  # fp16 — savings ~50% VRAM

    print("Encoding documents...")
    embeddings = encoder.encode(
        embed_input,
        batch_size=8,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    print(f"Embeddings shape: {embeddings.shape}")

    # BERTopic config
    sw = list(get_stopwords())
    vectorizer = CountVectorizer(stop_words=sw, ngram_range=(1, 2), min_df=3)
    umap_model = UMAP(n_neighbors=15, n_components=5, min_dist=0.0,
                       metric="cosine", random_state=42)
    hdbscan_model = HDBSCAN(min_cluster_size=8, metric="euclidean",
                             cluster_selection_method="eom", prediction_data=True)

    topic_model = BERTopic(
        embedding_model=encoder,
        umap_model=umap_model,
        hdbscan_model=hdbscan_model,
        vectorizer_model=vectorizer,
        calculate_probabilities=False,
        verbose=True,
    )
    topics, _ = topic_model.fit_transform(raw_docs, embeddings=embeddings)

    info = topic_model.get_topic_info()
    print(f"\nDiscovered {len(info) - 1} topics (+ 1 outlier cluster).")
    print(info.head(20).to_string())

    # Save doc → topic mapping
    df = pd.DataFrame({
        "id": ids,
        "data": dates,
        "period": periods,
        "topic_id": topics,
    })
    topic_labels = {row["Topic"]: row["Name"] for _, row in info.iterrows()}
    df["topic_label"] = df["topic_id"].map(topic_labels)
    df.to_csv(OUT / "topics.csv", index=False)

    # Save topic info markdown
    md_lines = [f"# BERTopic — {PROJECTION} ({len(speeches)} docs)\n"]
    md_lines.append(f"**Model**: {label}")
    md_lines.append(f"**Topics descoperite**: {len(info) - 1} (+ cluster outlier `-1`)")
    md_lines.append(f"**Stopwords c-TF-IDF**: {len(sw)} RO\n")
    md_lines.append("## Toate topicele\n")
    md_lines.append(info[["Topic", "Count", "Name"]].to_markdown(index=False))
    md_lines.append("\n## Top 10 cuvinte per topic\n")
    for topic_id in info["Topic"]:
        if topic_id == -1:
            continue
        words = topic_model.get_topic(topic_id)[:10]
        words_str = ", ".join(f"`{w}` ({s:.3f})" for w, s in words)
        md_lines.append(f"### Topic {topic_id} (n={info[info['Topic']==topic_id]['Count'].values[0]})")
        md_lines.append(f"{words_str}\n")
    (OUT / "topic_info.md").write_text("\n".join(md_lines))

    # Topics over time — group by period
    df_time = df[df["topic_id"] != -1].copy()
    pivot = df_time.groupby(["period", "topic_id"]).size().unstack(fill_value=0)
    pivot = pivot.reindex(sorted(pivot.index))
    # Normalize per period (relative share)
    pivot_norm = pivot.div(pivot.sum(axis=1), axis=0) * 100

    # Plot — heatmap topic × period
    top_topics = info[info["Topic"] != -1].nlargest(15, "Count")["Topic"].tolist()
    pivot_plot = pivot_norm[top_topics]
    pivot_plot.columns = [topic_labels[t][:60] for t in pivot_plot.columns]

    fig, ax = plt.subplots(figsize=(14, 8))
    im = ax.imshow(pivot_plot.values, aspect="auto", cmap="YlOrRd")
    ax.set_xticks(range(len(pivot_plot.columns)))
    ax.set_xticklabels(pivot_plot.columns, rotation=45, ha="right", fontsize=9)
    ax.set_yticks(range(len(pivot_plot.index)))
    ax.set_yticklabels(pivot_plot.index, fontsize=10)
    plt.colorbar(im, ax=ax, label="% docs in period")
    ax.set_title(f"Topic share per perioadă — top 15 topics ({PROJECTION})")
    fig.tight_layout()
    fig.savefig(OUT / "topics_over_time.png", dpi=120, bbox_inches="tight")
    plt.close(fig)

    # Save the trained model for reuse
    topic_model.save(str(OUT / "model"), serialization="safetensors",
                     save_ctfidf=True, save_embedding_model=False)

    print(f"\nOutputs in: {OUT}/")
    print(f"  - topics.csv ({len(df)} rows)")
    print(f"  - topic_info.md")
    print(f"  - topics_over_time.png")
    print(f"  - model/ (BERTopic serialized)")


if __name__ == "__main__":
    main()
