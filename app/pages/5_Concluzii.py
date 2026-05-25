"""Pagină: Concluzii — afișează cele 28 concluzii cu link-uri către surse."""
from __future__ import annotations

from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent.parent.parent

st.set_page_config(page_title="Concluzii", page_icon="🔍", layout="wide")

st.title("28 concluzii")
st.markdown(
    "Toate concluziile cantitative ale analizei. Click pe fiecare pentru detalii. "
    "Toate sunt susținute de date și cod în repository."
)

findings_path = ROOT / "results" / "FINDINGS.md"

if not findings_path.exists():
    st.error("Fișierul FINDINGS.md lipsește.")
    st.stop()

content = findings_path.read_text()

st.markdown(content)

st.markdown("---")
st.markdown(
    f"**Sursă brută**: [`{findings_path.relative_to(ROOT)}`](https://github.com/radusqrt/evolutie-discurs-nicusor-dan/blob/main/results/FINDINGS.md)"
)
