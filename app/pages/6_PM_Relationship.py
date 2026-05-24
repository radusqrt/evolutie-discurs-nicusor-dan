"""Page: Relația ND-Bolojan — timeline mențiuni + analiza per perioadă + fact-check."""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).parent.parent))

ROOT = Path(__file__).resolve().parent.parent.parent
SRC_BOLOJAN = ROOT / "results" / "10_nd_bolojan" / "bolojan_mentions.jsonl"
SRC_CIOLACU = ROOT / "results" / "10_nd_bolojan" / "ciolacu_mentions.jsonl"
SRC_PERIODS = ROOT / "results" / "10_nd_bolojan" / "period_analyses.jsonl"
SRC_OVERALL = ROOT / "results" / "10_nd_bolojan" / "overall_synthesis.json"
SRC_RAPORT = ROOT / "results" / "10_nd_bolojan" / "RAPORT.md"
SRC_FACTCHECK = ROOT / "results" / "10_nd_bolojan" / "FACT_CHECK.md"

st.set_page_config(page_title="Raportul ND-Bolojan", page_icon="🤝", layout="wide")

st.title("Raportul Nicușor Dan – Ilie Bolojan")
st.markdown(
    "Analiza tuturor mențiunilor lui Bolojan/premier/prim-ministru în discursul lui ND, "
    "clasificate per perioadă cu Gemini, plus fact-check independent pe toate 6 perioade."
)


@st.cache_data
def load_mentions(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    rows = []
    with path.open() as f:
        for line in f:
            rows.append(json.loads(line))
    return pd.DataFrame(rows)


@st.cache_data
def load_period_analyses() -> list[dict]:
    if not SRC_PERIODS.exists():
        return []
    rows = []
    with SRC_PERIODS.open() as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


bolojan = load_mentions(SRC_BOLOJAN)
ciolacu = load_mentions(SRC_CIOLACU)
periods = load_period_analyses()

# Top stats
col1, col2, col3, col4 = st.columns(4)
col1.metric("Spans Bolojan/premier", len(bolojan))
col2.metric("Docs unice Bolojan", bolojan["doc_id"].nunique() if not bolojan.empty else 0)
col3.metric("Spans Ciolacu (comparativ)", len(ciolacu))
col4.metric("Ratio Bolojan/Ciolacu",
              f"{len(bolojan)/max(len(ciolacu),1):.1f}×")

# Mențiuni per perioadă — bar chart side by side
st.markdown("---")
st.subheader("Mențiuni per perioadă")

all_periods = sorted(set(bolojan["period"].unique()) | set(ciolacu["period"].unique()))
b_counts = bolojan["period"].value_counts().reindex(all_periods, fill_value=0)
c_counts = ciolacu["period"].value_counts().reindex(all_periods, fill_value=0)

df_chart = pd.DataFrame({
    "Bolojan/premier": b_counts.values,
    "Ciolacu": c_counts.values,
}, index=[p.split(" ", 1)[0] for p in all_periods])
st.bar_chart(df_chart)

st.markdown("---")

# Period analyses (Gemini)
st.subheader("Analiza ton relațional per perioadă (Gemini)")
st.caption("Clasificare automată cu LLM pe baza paragrafelor unde ND îl menționează pe Bolojan/premier.")

tone_emoji = {
    "distant": "❄️",
    "mixt": "🟡",
    "colaborativ": "🟢",
    "deferent": "🤝",
    "critic": "🟠",
    "tensionat": "🔴",
}

for p in periods:
    period = p["period"]
    tone = str(p.get("relationship_tone", "?"))
    # Pick first emoji match
    emoji = "•"
    for k, e in tone_emoji.items():
        if k in tone.lower():
            emoji = e
            break

    with st.expander(
        f"{emoji} **{period}** — ton: `{tone}` ({p.get('n_mentions', '?')} spans, {p.get('n_docs', '?')} docs)",
        expanded=("tensionat" in tone.lower() or "distant" in tone.lower()),
    ):
        ca, cb = st.columns(2)
        ca.metric("Power dynamic", str(p.get("power_dynamic", "n/a")))
        cb.metric("Tensiuni vizibile", str(p.get("tensions_visible", "n/a")))

        if p.get("key_themes"):
            st.markdown(f"**Teme cheie**: {', '.join(p['key_themes'])}")

        st.markdown(f"**Raționament**: {p.get('rationale', '')}")

        if p.get("notable_quotes"):
            st.markdown("**Citate notabile**:")
            for q in p["notable_quotes"][:3]:
                st.markdown(f"> *\"{q}\"*")

st.markdown("---")

# Mentions browser
st.subheader("Explorator mențiuni Bolojan în corpus")

if not bolojan.empty:
    period_filter = st.multiselect(
        "Filtru perioadă",
        options=all_periods,
        default=[]
    )

    df_view = bolojan.copy()
    if period_filter:
        df_view = df_view[df_view["period"].isin(period_filter)]

    df_view = df_view.sort_values("date", ascending=False)
    st.caption(f"{len(df_view)} spans afișate.")

    for _, r in df_view.head(20).iterrows():
        with st.expander(f"{r['date']} — `{r['doc_id'][:70]}` ({r['match']})", expanded=False):
            st.markdown(f"**Tip**: {r['tip']} | **Perioadă**: {r['period']}")
            st.markdown(f"**Match-uri**: `{r['match']}`")
            st.markdown(f"**Context**:")
            st.markdown(r["context"])

st.markdown("---")

# Fact-check section
st.subheader("Fact-check independent (web)")
st.markdown(
    "Toate 6 perioade au fost validate cu surse externe (Digi24, AGERPRES, Europa Liberă, "
    "HotNews, ProTV, Recorder, Capital, Veridica, Profit, etc.). Calitate Gemini: 83% spot-on, "
    "100% direcțional corect."
)

if SRC_FACTCHECK.exists():
    with st.expander("Vezi fact-check complet (FACT_CHECK.md)", expanded=False):
        st.markdown(SRC_FACTCHECK.read_text())
