"""Load, clean, and tokenize the speech corpus.

Uses SOTA tools:
- stopwordsiso (maintained Romanian stopword list)
- spaCy ro_core_news_sm (Romanian model: tokenization + lemmatization + POS)
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import frontmatter
import stopwordsiso
import spacy

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"


@dataclass
class Speech:
    id: str
    date: str
    tip: str
    sursa: str
    verificat: bool
    locatie: str | None
    raw_text: str
    nd_only_text: str

    @property
    def word_count(self) -> int:
        return len(tokenize(self.nd_only_text, lemmatize=False, remove_stopwords=False))


@lru_cache(maxsize=1)
def get_stopwords() -> frozenset[str]:
    """Romanian stopwords from stopwordsiso, plus our domain extras."""
    base = stopwordsiso.stopwords("ro")
    extras = {
        # Cardinals not in the list
        "un", "o", "doi", "două", "trei", "patru", "cinci", "șase", "șapte", "opt", "nouă", "zece",
        # Common verb forms that slipped through
        "așa", "aşa", "făra", "fără", "într", "într-", "din", "dintr",
        # Speaker frills
        "așadar", "așa", "deci",
    }
    # Normalize all to ș/ț form
    all_sw = {_normalize_diacritics(w.lower()) for w in (base | extras)}
    return frozenset(all_sw)


@lru_cache(maxsize=1)
def get_nlp() -> spacy.language.Language:
    """Load spaCy Romanian model. Disables parser/NER for speed."""
    return spacy.load("ro_core_news_sm", disable=["parser", "ner"])


def _normalize_diacritics(text: str) -> str:
    """Normalize ş→ș, ţ→ț (cedilla → comma-below)."""
    return text.replace("ş", "ș").replace("ţ", "ț").replace("Ş", "Ș").replace("Ţ", "Ț")


def strip_speaker_tags_to_nd(raw_text: str) -> str:
    """Extract only lines tagged [ND]. If no tags present, return whole text."""
    has_tags = any(tag in raw_text for tag in ("[ND]", "[JURNALIST", "[MODERATOR", "[OTHER"))
    if not has_tags:
        return raw_text
    lines: list[str] = []
    in_nd = False
    for line in raw_text.splitlines():
        m = re.match(r"^\[([^\]]+)\]\s*(.*)$", line)
        if m:
            tag = m.group(1).strip().upper()
            in_nd = tag == "ND" or tag.startswith("ND:")
            if in_nd:
                lines.append(m.group(2))
        elif in_nd:
            lines.append(line)
    return "\n".join(lines)


def load_corpus() -> list[Speech]:
    """Load all .md files from data/raw/**, parse YAML frontmatter.

    Skips data/raw/excluded/ (off-scope content, e.g. mayoral pre-candidacy).
    """
    speeches: list[Speech] = []
    for path in sorted(RAW_DIR.rglob("*.md")):
        if "/excluded/" in str(path):
            continue
        post = frontmatter.load(path)
        raw_text = post.content.strip()
        speeches.append(
            Speech(
                id=path.stem,
                date=str(post.get("data", "")),
                tip=str(post.get("tip", "")),
                sursa=str(post.get("sursa", "")),
                verificat=bool(post.get("verificat", False)),
                locatie=post.get("locatie"),
                raw_text=raw_text,
                nd_only_text=strip_speaker_tags_to_nd(raw_text),
            )
        )
    return speeches


def tokenize(
    text: str,
    lemmatize: bool = True,
    remove_stopwords: bool = True,
    keep_pos: tuple[str, ...] | None = None,
    min_len: int = 2,
) -> list[str]:
    """Tokenize Romanian text using spaCy.

    Args:
        text: Input text.
        lemmatize: If True, return lemmas; else surface forms (lowercased).
        remove_stopwords: Filter stopwords (after lemmatization).
        keep_pos: If set, keep only tokens whose POS is in this tuple.
                  Common: ("NOUN", "PROPN", "ADJ", "VERB").
        min_len: Minimum token length after cleaning.
    """
    text = _normalize_diacritics(text)
    doc = get_nlp()(text)
    tokens: list[str] = []
    sw = get_stopwords() if remove_stopwords else frozenset()
    for tok in doc:
        if tok.is_punct or tok.is_space or tok.like_num:
            continue
        if keep_pos and tok.pos_ not in keep_pos:
            continue
        form = tok.lemma_.lower() if lemmatize else tok.text.lower()
        form = _normalize_diacritics(form)
        form = re.sub(r"[^a-zăâîșț\-]", "", form)
        if len(form) < min_len:
            continue
        if remove_stopwords and form in sw:
            continue
        tokens.append(form)
    return tokens


if __name__ == "__main__":
    speeches = load_corpus()
    print(f"Loaded {len(speeches)} speeches.\n")
    for s in speeches:
        toks_raw = tokenize(s.nd_only_text, lemmatize=False, remove_stopwords=False)
        toks_lem = tokenize(s.nd_only_text, lemmatize=True, remove_stopwords=True)
        print(f"  - {s.id}")
        print(f"      raw tokens: {len(toks_raw)}, lemmas (clean): {len(toks_lem)}")
        print(f"      sample lemmas: {toks_lem[:15]}")
