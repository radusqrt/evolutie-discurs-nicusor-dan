"""Page: Browse Corpus — search, filter, view documents."""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).parent.parent))
from data_loaders import load_corpus_docs, period_for

st.set_page_config(page_title="Browse Corpus", page_icon="📚", layout="wide")

st.title("Browse Corpus")
st.markdown(
    "Caută în textul integral al celor 1,062 discursuri ale lui Nicușor Dan. "
    "Filtrează după dată, sursă, proiecție."
)

# --- Sidebar filters ---
st.sidebar.header("Filtre")

projection = st.sidebar.selectbox(
    "Proiecție", ["overall", "scris", "vorbit"], index=0,
    help="overall = toate sursele; scris = FB; vorbit = video"
)

df = load_corpus_docs(projection)
df["period"] = df["date"].astype(str).apply(period_for)

date_min = df["date"].min().to_pydatetime()
date_max = df["date"].max().to_pydatetime()
date_range = st.sidebar.date_input(
    "Interval date", value=(date_min.date(), date_max.date()),
    min_value=date_min.date(), max_value=date_max.date(),
)

# Filter tip
all_tips = sorted(df["tip"].unique())
selected_tips = st.sidebar.multiselect(
    "Tip document", all_tips, default=all_tips,
)

# Filter source channel
all_canals = sorted([c for c in df["sursa_canal"].unique() if c])
selected_canals = st.sidebar.multiselect(
    "Canal sursă", all_canals, default=all_canals,
)

query = st.sidebar.text_input(
    "Caută keyword în text",
    placeholder='ex: "pensii", "Ucraina", "deficit"...',
    help="Case-insensitive, simplu substring (nu regex)."
)

min_words = st.sidebar.slider(
    "Lungime minimă (cuvinte)", 0, 1000, 0, step=50,
)

# --- Apply filters ---
if isinstance(date_range, tuple) and len(date_range) == 2:
    start, end = pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1])
    mask = (df["date"] >= start) & (df["date"] <= end)
else:
    mask = pd.Series([True] * len(df))

if selected_tips:
    mask &= df["tip"].isin(selected_tips)
if selected_canals:
    mask &= df["sursa_canal"].isin(selected_canals)
mask &= df["word_count"] >= min_words

filtered = df[mask].copy()

if query:
    q_lower = query.lower()
    filtered = filtered[filtered["text"].str.lower().str.contains(q_lower, na=False)]

st.markdown(f"**{len(filtered)} / {len(df)} documente** după filtre")

# --- Display ---

if not filtered.empty:
    col1, col2 = st.columns([2, 3])

    with col1:
        st.subheader("Distribuție pe perioade")
        period_counts = filtered["period"].value_counts().sort_index()
        st.bar_chart(period_counts)

    with col2:
        st.subheader("Distribuție pe tip")
        tip_counts = filtered["tip"].value_counts().head(15)
        st.bar_chart(tip_counts)

    st.subheader("Documente")

    # Sort options
    sort_col = st.selectbox("Sortează după", ["date", "word_count"], index=0)
    sort_desc = st.checkbox("Descrescător", value=True)
    filtered = filtered.sort_values(sort_col, ascending=not sort_desc)

    # Display table with selection
    display_df = filtered[["date", "tip", "sursa_canal", "sursa_titlu", "word_count"]].head(50).copy()
    display_df["date"] = display_df["date"].dt.strftime("%Y-%m-%d")
    display_df.columns = ["Data", "Tip", "Canal", "Titlu", "Cuvinte"]

    st.dataframe(display_df, use_container_width=True, hide_index=True)

    if len(filtered) > 50:
        st.info(f"Afișate primele 50 din {len(filtered)} rezultate. Restrânge filtrele pentru mai puține.")

    st.markdown("---")
    st.subheader("Vizualizare document")

    selected_id = st.selectbox(
        "Selectează document",
        options=filtered["id"].head(50).tolist(),
        format_func=lambda x: f"{filtered[filtered['id']==x]['date'].iloc[0].strftime('%Y-%m-%d')} — {filtered[filtered['id']==x]['sursa_titlu'].iloc[0][:80]}"
    )

    if selected_id:
        doc = filtered[filtered["id"] == selected_id].iloc[0]

        cmeta1, cmeta2, cmeta3 = st.columns(3)
        with cmeta1:
            st.metric("Data", doc["date"].strftime("%Y-%m-%d"))
            st.metric("Tip", doc["tip"])
        with cmeta2:
            st.metric("Canal", doc["sursa_canal"][:30] or "—")
            st.metric("Cuvinte", doc["word_count"])
        with cmeta3:
            st.metric("Perioadă", doc["period"][:20])
            if doc["locatie"] and doc["locatie"] != "None":
                st.metric("Locație", doc["locatie"])

        if doc["sursa"]:
            st.markdown(f"**Sursă originală**: {doc['sursa']}")

        st.markdown("---")

        # Highlight query in text if present
        text = doc["text"]
        if query:
            import re
            text = re.sub(
                f"({re.escape(query)})", r"**\1**",
                text, flags=re.IGNORECASE
            )

        st.markdown(text)
else:
    st.warning("Niciun document nu îndeplinește filtrele. Relaxează criteriile.")
