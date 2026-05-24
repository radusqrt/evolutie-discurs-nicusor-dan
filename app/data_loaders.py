"""Shared cached loaders for Streamlit app.

Toate funcțiile sunt cached cu @st.cache_data sau @st.cache_resource
pentru a evita re-loading la fiecare interacțiune.
"""
from __future__ import annotations

import json
from pathlib import Path

import frontmatter
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent


@st.cache_data
def load_corpus_docs(projection: str = "overall") -> pd.DataFrame:
    """Load all docs from a projection with metadata."""
    src = ROOT / "data" / f"3_nd_{projection}"
    rows = []
    for path in sorted(src.rglob("*.md")):
        if "/excluded/" in str(path):
            continue
        post = frontmatter.load(path)
        content = post.content.strip()
        if not content:
            continue
        rows.append({
            "id": path.stem,
            "date": str(post.get("data", ""))[:10],
            "tip": str(post.get("tip", "")),
            "sursa": str(post.get("sursa", "")),
            "sursa_canal": str(post.get("sursa_canal", "")),
            "sursa_titlu": str(post.get("sursa_titlu", "")),
            "locatie": str(post.get("locatie", "")),
            "text": content,
            "word_count": len(content.split()),
        })
    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df.dropna(subset=["date"]).sort_values("date")


def period_for(date_str: str) -> str:
    if not date_str or pd.isna(date_str):
        return "outside-scope"
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


@st.cache_data
def load_topics(projection: str = "overall") -> pd.DataFrame:
    """Load BERTopic doc-topic assignments."""
    p = ROOT / "results" / f"03_bertopic_{projection}" / "topics.csv"
    if not p.exists():
        return pd.DataFrame()
    df = pd.read_csv(p)
    return df


@st.cache_data
def load_topic_info(projection: str = "overall") -> pd.DataFrame:
    """Load BERTopic topic descriptions (id → name + count)."""
    df = load_topics(projection)
    if df.empty:
        return pd.DataFrame()
    info = df.groupby(["topic_id", "topic_label"]).size().reset_index(name="count")
    info = info.sort_values("count", ascending=False)
    return info


@st.cache_data
def load_promises() -> pd.DataFrame:
    """Load all 131 canonical promises with classification."""
    p = ROOT / "results" / "04_promises" / "promise_status.jsonl"
    rows = []
    with p.open() as f:
        for line in f:
            r = json.loads(line)
            rows.append({
                "promise_text": r.get("promise_text", ""),
                "verbatim_quote": r.get("verbatim_quote", ""),
                "topic": r.get("topic", ""),
                "specificity": r.get("specificity", ""),
                "source_date": r.get("source_date", ""),
                "source_doc_id": r.get("source_doc_id", ""),
                "status": r.get("status_status", ""),
                "confidence": r.get("status_confidence", ""),
                "reasoning": r.get("status_reasoning", ""),
                "cluster_size": r.get("cluster_size", 1),
            })
    return pd.DataFrame(rows)


@st.cache_data
def load_entity_timeline(projection: str = "overall") -> pd.DataFrame:
    """Load NER entity × period timeline."""
    p = ROOT / "results" / f"08_ner_{projection}" / "entity_timeline_clean.csv"
    if not p.exists():
        return pd.DataFrame()
    return pd.read_csv(p, index_col=0)


@st.cache_data
def load_sentiment_per_entity(projection: str = "overall") -> pd.DataFrame:
    """Load sentiment per entity × period."""
    p = ROOT / "results" / f"09_sentiment_per_entity_{projection}" / "sentiment_per_entity_period.jsonl"
    if not p.exists():
        return pd.DataFrame()
    rows = []
    with p.open() as f:
        for line in f:
            rows.append(json.loads(line))
    return pd.DataFrame(rows)


@st.cache_data
def load_complexity(projection: str = "overall") -> pd.DataFrame:
    """Load per-doc discourse complexity metrics."""
    p = ROOT / "results" / f"05_complexity_{projection}" / "complexity_per_doc.csv"
    if not p.exists():
        return pd.DataFrame()
    return pd.read_csv(p)


@st.cache_data
def load_hedging(projection: str = "overall") -> pd.DataFrame:
    """Load per-doc hedging metrics."""
    p = ROOT / "results" / f"06_hedging_{projection}" / "hedging_per_doc.csv"
    if not p.exists():
        return pd.DataFrame()
    return pd.read_csv(p)


def corpus_stats() -> dict:
    """Quick stats for all 3 projections."""
    out = {}
    for proj in ["overall", "scris", "vorbit"]:
        df = load_corpus_docs(proj)
        out[proj] = {
            "n_docs": len(df),
            "n_words": int(df["word_count"].sum()),
            "date_min": str(df["date"].min().date()) if not df.empty else "?",
            "date_max": str(df["date"].max().date()) if not df.empty else "?",
        }
    return out
