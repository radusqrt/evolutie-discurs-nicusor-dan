"""Pasul 4c+4d: Match canonical promises against mandate corpus + classify status.

Strategie:
1. Split docs din perioada mandat (date > 2025-05-25) în paragrafe.
2. Embed all paragraphs cu paraphrase-multilingual-mpnet.
3. Pentru fiecare canonical promise, retrieve top-10 paragrafe via cosine.
4. LLM classify: KEPT / IN_PROGRESS / REFRAMED / ABANDONED / CONTRADICTED / NO_MENTION
   + evidence snippets + reasoning.

Output:
  results/04_promises/promise_status.jsonl  (one row per promise)
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

import frontmatter
import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
SRC_CORPUS = ROOT / "data" / "3_nd_overall"
SRC_PROMISES = ROOT / "results" / "04_promises" / "promises_canonical.jsonl"
DST = ROOT / "results" / "04_promises" / "promise_status.jsonl"

MANDATE_START = date(2025, 5, 26)
EMBED_MODEL = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
LLM_MODEL = "gemini-2.5-flash"
TOP_K = 8

CLASSIFY_PROMPT = """Ești un fact-checker care evaluează dacă o promisiune de campanie a fost respectată după mandat.

PROMISIUNE (făcută în campanie, înainte de 26 mai 2025):
{promise}

Topic: {topic}
Specificity: {specificity}

EVIDENCE (extrase din discursul lui ND după investitură):
{evidence}

CLASIFICĂ statusul promisiunii cu UNA din etichetele:
- KEPT — Există declarații care confirmă acțiuni concrete făcute / în execuție directă a promisiunii
- IN_PROGRESS — Promisiunea e menționată ca obiectiv urmărit, dar fără acțiune finalizată
- REFRAMED — Promisiunea apare cu mod diferit / scope schimbat / condiționalități adăugate
- ABANDONED — Promisiunea e contrazisă sau menționată ca nemai-relevantă
- CONTRADICTED — ND a făcut declarații care contrazic clar promisiunea
- NO_MENTION — Niciuna din evidence nu menționează promisiunea sau topic-ul ei specific

OUTPUT — JSON object:
{{
  "status": "KEPT | IN_PROGRESS | REFRAMED | ABANDONED | CONTRADICTED | NO_MENTION",
  "confidence": "high | medium | low",
  "reasoning": "2-3 propoziții de justificare",
  "supporting_evidence": ["citat scurt 1 (max 200 caractere)", "citat scurt 2"]
}}

Returnează DOAR JSON. Niciun preambul, comentariu, sau cod block."""


def get_client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or "your-" in api_key:
        print("ERROR: GEMINI_API_KEY missing", file=sys.stderr)
        sys.exit(1)
    from google import genai
    from google.genai import types
    client = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=180_000))
    return client, types


def parse_date(s: str) -> date | None:
    try:
        return date.fromisoformat(s[:10])
    except (ValueError, TypeError):
        return None


def split_paragraphs(text: str, min_words: int = 8, max_words: int = 120) -> list[str]:
    """Split text into paragraphs. Glue short ones, split long ones."""
    paras = [p.strip() for p in re.split(r"\n\n+", text) if p.strip()]
    out: list[str] = []
    buf: list[str] = []
    buf_wc = 0
    for p in paras:
        wc = len(p.split())
        if wc >= max_words:
            # flush current buffer, then split long paragraph on sentences
            if buf:
                out.append(" ".join(buf))
                buf, buf_wc = [], 0
            sents = re.split(r"(?<=[.!?])\s+", p)
            cur, cur_wc = [], 0
            for s in sents:
                sw = len(s.split())
                if cur_wc + sw > max_words and cur:
                    out.append(" ".join(cur))
                    cur, cur_wc = [], 0
                cur.append(s)
                cur_wc += sw
            if cur:
                out.append(" ".join(cur))
        elif buf_wc + wc < min_words:
            buf.append(p)
            buf_wc += wc
        else:
            buf.append(p)
            buf_wc += wc
            if buf_wc >= min_words:
                out.append(" ".join(buf))
                buf, buf_wc = [], 0
    if buf:
        out.append(" ".join(buf))
    return [p for p in out if len(p.split()) >= 4]


def load_mandate_paragraphs() -> tuple[list[str], list[dict]]:
    """Returns (paragraph texts, metadata list parallel)."""
    paragraphs: list[str] = []
    meta: list[dict] = []
    for path in sorted(SRC_CORPUS.rglob("*.md")):
        if "/excluded/" in str(path):
            continue
        post = frontmatter.load(path)
        d = parse_date(str(post.get("data", "")))
        if not d or d < MANDATE_START:
            continue
        content = post.content.strip()
        if not content:
            continue
        for para in split_paragraphs(content):
            paragraphs.append(para)
            meta.append({
                "doc_id": path.stem,
                "date": str(d),
                "tip": str(post.get("tip", "")),
            })
    return paragraphs, meta


def load_promises() -> list[dict]:
    out = []
    with SRC_PROMISES.open() as f:
        for line in f:
            out.append(json.loads(line))
    return out


def classify_one(promise: dict, top_evidence: list[tuple[float, str, dict]],
                  client, types) -> dict:
    """LLM call to classify one promise."""
    evidence_text = ""
    for sim, text, m in top_evidence:
        evidence_text += f"\n[doc={m['doc_id']} | date={m['date']} | sim={sim:.2f}]\n{text}\n"

    prompt = CLASSIFY_PROMPT.format(
        promise=promise["promise_text"],
        topic=promise["topic"],
        specificity=promise.get("specificity", "?"),
        evidence=evidence_text,
    )
    try:
        resp = client.models.generate_content(
            model=LLM_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.1,
                thinking_config=types.ThinkingConfig(thinking_budget=0),
                response_mime_type="application/json",
            ),
        )
        raw = resp.text.strip()
        result = json.loads(raw)
        return result
    except json.JSONDecodeError as e:
        return {"status": "ERROR", "confidence": "low",
                "reasoning": f"JSON parse error: {str(e)[:80]}",
                "supporting_evidence": []}
    except Exception as e:
        return {"status": "ERROR", "confidence": "low",
                "reasoning": f"{type(e).__name__}: {str(e)[:80]}",
                "supporting_evidence": []}


def main():
    print(f"Loading mandate paragraphs (date >= {MANDATE_START})...")
    paragraphs, meta = load_mandate_paragraphs()
    print(f"  {len(paragraphs)} paragraphs from {len(set(m['doc_id'] for m in meta))} docs")

    print(f"\nEmbedding mandate paragraphs with {EMBED_MODEL}...")
    model = SentenceTransformer(EMBED_MODEL)
    para_embeddings = model.encode(paragraphs, show_progress_bar=True,
                                     normalize_embeddings=True, batch_size=32)

    print("\nLoading canonical promises...")
    promises = load_promises()
    print(f"  {len(promises)} canonical promises")

    print("Embedding promises...")
    promise_texts = [p["promise_text"] for p in promises]
    promise_embeddings = model.encode(promise_texts, show_progress_bar=True,
                                        normalize_embeddings=True)

    print(f"\nClassifying {len(promises)} promises with {LLM_MODEL}...")
    client, types = get_client()
    t0 = time.time()

    def process_one(idx: int) -> dict:
        promise = promises[idx]
        p_emb = promise_embeddings[idx:idx+1]
        sims = cosine_similarity(p_emb, para_embeddings)[0]
        top_indices = np.argsort(-sims)[:TOP_K]
        top_evidence = [(float(sims[j]), paragraphs[j], meta[j]) for j in top_indices]
        result = classify_one(promise, top_evidence, client, types)
        out = {**promise, **{f"status_{k}": v for k, v in result.items()}}
        out["top_evidence"] = [{"sim": s, "text": t[:400], "doc_id": m["doc_id"],
                                 "date": m["date"]} for s, t, m in top_evidence[:5]]
        return out

    with DST.open("w") as out_f:
        with ThreadPoolExecutor(max_workers=4) as ex:
            futures = {ex.submit(process_one, i): i for i in range(len(promises))}
            done_count = 0
            status_counts: dict[str, int] = {}
            for fut in as_completed(futures):
                idx = futures[fut]
                try:
                    out = fut.result(timeout=180)
                except Exception as e:
                    print(f"  [{idx}] ERROR: {e}", file=sys.stderr)
                    continue
                out_f.write(json.dumps(out, ensure_ascii=False) + "\n")
                out_f.flush()
                done_count += 1
                status = out.get("status_status", "ERROR")
                status_counts[status] = status_counts.get(status, 0) + 1
                rate = done_count / max(time.time() - t0, 0.1)
                print(f"[{done_count}/{len(promises)}] {status:<14} | "
                      f"{out['promise_text'][:70]:<70} ({rate:.1f}/s)")

    elapsed = time.time() - t0
    print(f"\nDone in {elapsed:.1f}s.")
    print(f"Status distribution:")
    for s in sorted(status_counts, key=lambda k: -status_counts[k]):
        print(f"  {s:>14}: {status_counts[s]}")
    print(f"\nOutput: {DST}")


if __name__ == "__main__":
    main()
