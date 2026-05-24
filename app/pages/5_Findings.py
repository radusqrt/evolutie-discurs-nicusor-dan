"""Page: Findings — afișează toate cele 27 findings cu link-uri la artefacte."""
from __future__ import annotations

from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent.parent.parent

st.set_page_config(page_title="Findings", page_icon="🔍", layout="wide")

st.title("27 Findings")
st.markdown(
    "Toate concluziile cantitative ale analizei. Click pe fiecare pentru detalii. "
    "Toate findings sunt susținute de date/cod în repo."
)

findings_path = ROOT / "results" / "FINDINGS.md"

if not findings_path.exists():
    st.error("FINDINGS.md not found.")
    st.stop()

content = findings_path.read_text()

# Render the markdown
st.markdown(content)

st.markdown("---")
st.markdown(
    f"**Raw source**: [`{findings_path.relative_to(ROOT)}`](https://github.com/radusqrt/evolutie-discurs-nicusor-dan/blob/main/results/FINDINGS.md)"
)
