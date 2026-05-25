"""Robust entity disambiguation pentru extracție bazată pe regex + verificare LLM.

Problema rezolvată: regex-based matching pe termeni generici (ex. "premier",
"prim-ministru") capturează contexte care nu sunt despre entitatea țintă (ex.
"premierul Ciolacu", "Ponta era prim-ministru în 2014", "Trump i-a spus
premierul Nicușor Dan").

Soluția:
- Match-uri STRICTE (cu numele entității în context) → auto-acceptate
- Match-uri GENERICE (doar termenul generic, fără nume în vecinătate) →
  trimise la LLM cu întrebare: "Este acest paragraf efectiv despre {entity}?"

Pentru consistență cu restul pipeline-ului: folosim Gemini 2.5 Flash cu
thinking_budget=0.

Folosire:
    from scripts.utils_entity_disambiguation import extract_disambiguated_mentions

    spans = extract_disambiguated_mentions(
        text=document_text,
        entity_name="Ilie Bolojan",
        aliases=["Bolojan", "Ilie"],
        generic_terms=["premier", "prim ministru", "prim-ministru"],
        client=gemini_client,
        types=genai_types,
    )
    # spans = [{"span_text": "...", "match_type": "strict|disambiguated",
    #          "match_term": "...", "is_about": True}, ...]
"""
from __future__ import annotations

import json
import re
import time
from typing import Optional

CONTEXT_CHARS = 300  # chars around match for context window
NAME_PROXIMITY_CHARS = 150  # if name appears within this distance, match is "strict"


DISAMBIGUATION_PROMPT = """Analizează acest paragraf și răspunde dacă vorbește efectiv despre **{entity}** (entitatea țintă — poate fi persoană, organizație, partid, instituție etc.), sau menționează termenul în alt context.

Paragraf:
\"\"\"
{paragraph}
\"\"\"

Termen găsit în paragraf: "{match}"

ÎNTREBARE: Este acest paragraf vorbind efectiv despre {entity} (chiar dacă subiectul principal e altul, atâta timp cât {entity} este menționat ca actor real)?

Răspunde **false** doar dacă:
- termenul e folosit într-un sens generic sau abstract care nu se referă la {entity}
- e o coincidență de cuvinte (ex. funcție generică ocupată de altă persoană)
- e un context istoric/exemplu care nu e despre {entity}

OUTPUT — JSON object (NU array):
{{
  "is_about_entity": true | false,
  "confidence": "high | medium | low",
  "reasoning": "1 propoziție — de ce da/nu",
  "actual_subject": "dacă false, despre cine/ce e (ex: 'Ciolacu', 'rol generic', 'Ponta în 2014')"
}}

Returnează DOAR JSON. Niciun preambul."""


def _normalize(text: str) -> str:
    """Normalize ș/ț diacritics."""
    return text.replace("ş", "ș").replace("ţ", "ț").replace("Ş", "Ș").replace("Ţ", "Ț").lower()


def _has_name_nearby(span: str, names: list[str], match_pos_in_span: int,
                      proximity: int = NAME_PROXIMITY_CHARS) -> bool:
    """Check if any name from `names` appears within `proximity` chars of match position."""
    span_norm = _normalize(span)
    for name in names:
        name_norm = _normalize(name)
        for m in re.finditer(re.escape(name_norm), span_norm):
            if abs(m.start() - match_pos_in_span) <= proximity:
                return True
    return False


def _classify_with_llm(paragraph: str, entity: str, match: str,
                        client, types, model_name: str = "gemini-2.5-flash",
                        max_retries: int = 3) -> dict:
    """Call LLM to disambiguate. Returns dict with is_about_entity, confidence, reasoning."""
    prompt = DISAMBIGUATION_PROMPT.format(
        entity=entity, paragraph=paragraph[:2000], match=match,
    )
    for attempt in range(max_retries):
        try:
            resp = client.models.generate_content(
                model=model_name, contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.0,
                    thinking_config=types.ThinkingConfig(thinking_budget=0),
                    response_mime_type="application/json",
                ),
            )
            raw = resp.text.strip()
            parsed = json.loads(raw)
            if isinstance(parsed, list) and len(parsed) > 0:
                parsed = parsed[0]
            if isinstance(parsed, dict):
                return parsed
            raise ValueError(f"not dict: {type(parsed).__name__}")
        except Exception as e:
            if attempt == max_retries - 1:
                return {"is_about_entity": None, "confidence": "low",
                        "reasoning": f"LLM error: {str(e)[:100]}",
                        "actual_subject": "unknown"}
            time.sleep(1)
    return {"is_about_entity": None}


def extract_disambiguated_mentions(
    text: str,
    entity_name: str,
    aliases: list[str],
    generic_terms: list[str],
    client=None,
    types=None,
    context_chars: int = CONTEXT_CHARS,
    skip_llm: bool = False,
) -> list[dict]:
    """Extract mentions of `entity_name` from `text` with disambiguation.

    Args:
        text: document text
        entity_name: canonical name (e.g., "Ilie Bolojan")
        aliases: list of names that identify entity strictly
                 (e.g., ["Bolojan", "Ilie"])
        generic_terms: ambiguous patterns that may refer to entity OR others
                       (e.g., ["premier", "prim ministru"])
        client, types: Gemini client + types (genai.Client and genai.types).
                       Required unless skip_llm=True.
        skip_llm: if True, only return strict matches (no LLM disambiguation)

    Returns:
        list of dicts with: span_text, match_type, match_term, is_about_entity,
        reasoning, actual_subject (if not is_about_entity)
    """
    if not skip_llm and (client is None or types is None):
        raise ValueError("client and types required unless skip_llm=True")

    text_norm = _normalize(text)
    all_patterns = aliases + generic_terms  # combined

    # Find all matches
    raw_matches: list[tuple[int, int, str, str]] = []  # (start, end, match_text, term)
    for term in all_patterns:
        term_norm = _normalize(term)
        # Build pattern: split on space/dash and rejoin with flexible separator
        parts = re.split(r"[- ]+", term_norm)
        pattern = r"[- ]+".join(re.escape(p) for p in parts if p)
        regex = rf"\b{pattern}\b"
        for m in re.finditer(regex, text_norm):
            raw_matches.append((m.start(), m.end(), text[m.start():m.end()], term))

    if not raw_matches:
        return []

    # Sort + deduplicate overlapping
    raw_matches.sort()
    dedup: list[tuple[int, int, str, str]] = []
    for s, e, t, term in raw_matches:
        if dedup and s < dedup[-1][1]:
            continue  # overlap, skip
        dedup.append((s, e, t, term))

    # Build spans with context
    spans = []
    for s, e, match_text, term in dedup:
        ctx_start = max(0, s - context_chars)
        ctx_end = min(len(text), e + context_chars)
        span = text[ctx_start:ctx_end].strip()
        match_pos_in_span = s - ctx_start

        # Classify match type
        if term in aliases:
            # Strict alias match — auto-accept
            spans.append({
                "span_text": span,
                "match_term": match_text,
                "match_type": "strict_alias",
                "is_about_entity": True,
                "confidence": "high",
                "reasoning": f"Strict alias match ({term})",
            })
        else:
            # Generic term — check if alias is nearby
            if _has_name_nearby(span, aliases, match_pos_in_span):
                spans.append({
                    "span_text": span,
                    "match_term": match_text,
                    "match_type": "generic_with_name_nearby",
                    "is_about_entity": True,
                    "confidence": "high",
                    "reasoning": f"Generic term '{term}' with alias name in ±{NAME_PROXIMITY_CHARS} chars",
                })
            else:
                # Ambiguous — needs LLM disambiguation
                if skip_llm:
                    spans.append({
                        "span_text": span,
                        "match_term": match_text,
                        "match_type": "generic_ambiguous_skipped",
                        "is_about_entity": False,
                        "confidence": "low",
                        "reasoning": "Generic match without name nearby; LLM skipped",
                    })
                else:
                    llm_result = _classify_with_llm(span, entity_name, match_text,
                                                      client, types)
                    spans.append({
                        "span_text": span,
                        "match_term": match_text,
                        "match_type": "llm_disambiguated",
                        "is_about_entity": llm_result.get("is_about_entity"),
                        "confidence": llm_result.get("confidence", "?"),
                        "reasoning": llm_result.get("reasoning", ""),
                        "actual_subject": llm_result.get("actual_subject"),
                    })

    return spans
