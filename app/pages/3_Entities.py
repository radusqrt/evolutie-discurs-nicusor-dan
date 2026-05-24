"""Page: Entities — NER timeline + sentiment per entity × period."""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).parent.parent))
from data_loaders import load_entity_timeline, load_sentiment_per_entity

ROOT = Path(__file__).resolve().parent.parent.parent

st.set_page_config(page_title="Entities", page_icon="👥", layout="wide")

st.title("Entities & Sentiment")
st.markdown(
    "**NER cu GLiNER multi-v2.1 zero-shot** (persoane politice, țări, instituții) + "
    "**sentiment Gemini 2.5 Flash** pe paragrafele care menționează fiecare entitate."
)

projection = st.sidebar.selectbox(
    "Proiecție", ["overall", "scris", "vorbit"], index=0,
)

timeline = load_entity_timeline(projection)
sentiment = load_sentiment_per_entity(projection)

if timeline.empty:
    st.error(f"Lipsesc rezultatele NER pentru proiecția '{projection}'.")
    st.stop()

# Top entities timeline
st.subheader(f"Top 25 entități × perioadă ({projection})")
st.markdown("**Counts**: cât de des apare fiecare entitate în discursul ND per trimestru.")

top_n_show = st.slider("Top N entități", 5, 25, 15)
display_timeline = timeline.head(top_n_show)
st.dataframe(display_timeline, use_container_width=True)

# Heatmap visualization
fig, ax = plt.subplots(figsize=(10, max(4, 0.35 * len(display_timeline))))
im = ax.imshow(display_timeline.values, aspect="auto", cmap="YlOrRd")
ax.set_xticks(range(len(display_timeline.columns)))
ax.set_xticklabels(display_timeline.columns, rotation=30, ha="right")
ax.set_yticks(range(len(display_timeline.index)))
ax.set_yticklabels(display_timeline.index, fontsize=10)
plt.colorbar(im, ax=ax, label="Mentions")
for i in range(display_timeline.shape[0]):
    for j in range(display_timeline.shape[1]):
        v = display_timeline.values[i, j]
        if v > 0:
            ax.text(j, i, str(int(v)), ha="center", va="center", fontsize=8,
                    color="white" if v > display_timeline.values.max() * 0.4 else "black")
ax.set_title(f"Entity mentions × period ({projection})")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.markdown("---")

# Sentiment
st.subheader("Sentiment per entitate × perioadă")
st.markdown("**Sentiment**: clasificat cu Gemini 2.5 Flash pe paragrafele care menționează entitatea. -1 (negativ) → +1 (pozitiv).")

if sentiment.empty:
    st.info(f"Sentiment per entitate nu e încă calculat pentru proiecția '{projection}'.")
else:
    sentiment_path = ROOT / "results" / f"09_sentiment_per_entity_{projection}" / "sentiment_heatmap.png"
    if sentiment_path.exists():
        st.image(str(sentiment_path), use_container_width=True)

    st.markdown("**Tabel detaliat** (filterable):")

    # Pretty up dataframe
    sent_display = sentiment[["entity", "period", "n_passages", "n_docs",
                                "sentiment", "confidence", "rationale"]].copy()
    sent_display["period_short"] = sent_display["period"].str.split(" ").str[0]
    sent_display = sent_display.drop(columns=["period"]).rename(
        columns={"period_short": "period"})

    # Filter
    entity_filter = st.multiselect(
        "Filter entitate", options=sorted(sent_display["entity"].unique()),
        default=[]
    )
    if entity_filter:
        sent_display = sent_display[sent_display["entity"].isin(entity_filter)]

    sentiment_filter = st.multiselect(
        "Filter sentiment",
        options=sorted(sent_display["sentiment"].unique()),
        default=[]
    )
    if sentiment_filter:
        sent_display = sent_display[sent_display["sentiment"].isin(sentiment_filter)]

    st.dataframe(sent_display, use_container_width=True, hide_index=True)
