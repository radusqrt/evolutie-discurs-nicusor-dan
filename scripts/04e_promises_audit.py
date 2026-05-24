"""Pasul 4e: Audit manual al clasificării promisiunilor.

Sample stratificat 20 promisiuni (mix de status), pentru fiecare:
1. Afișează promisiunea + statusul + reasoning-ul + supporting evidence
2. Caută INDEPENDENT în corpus mandat după keywords cheie din promisiune
3. Generează raport markdown human-reviewable cu colateral evidence

Output: results/04_promises/AUDIT.md
"""
from __future__ import annotations

import json
import os
import random
import re
from collections import defaultdict
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
SRC_STATUS = ROOT / "results" / "04_promises" / "promise_status.jsonl"
SRC_CORPUS = ROOT / "data" / "3_nd_overall"
OUT = ROOT / "results" / "04_promises" / f"AUDIT_seed{int(os.environ.get('AUDIT_SEED', 42))}.md"

MANDATE_START = "2025-05-26"
SEED = int(os.environ.get("AUDIT_SEED", 42))
N_PER_STATUS = 5  # 5 KEPT + 5 IN_PROGRESS + 5 NO_MENTION + 1 CONTRADICTED = 16 + a few extras

# Cuvinte funcționale + foarte comune să excludem din keyword search
SKIP_WORDS = {
    "voi", "vom", "să", "fi", "va", "avea", "face", "fac", "facem", "vor", "putea",
    "trebuie", "este", "sunt", "am", "ai", "ar", "fie", "dacă", "dar", "și", "sau",
    "în", "din", "pe", "la", "cu", "de", "pentru", "după", "înainte",
    "un", "o", "doi", "trei", "acest", "acea", "aceasta", "acela",
    "care", "ce", "cine", "cum", "când", "unde",
    "mai", "doar", "foarte", "tot", "toți", "toate", "atunci", "așa", "deja",
    "ca", "că", "căci", "deci", "așadar", "însă",
    "an", "ani", "lună", "luni", "zi", "zile", "data", "moment", "loc", "lucru",
    "om", "oameni", "fel",
    "românia", "român", "români", "țară", "stat", "statul",
    "important", "necesar", "concret", "specific",
    "calitate", "rol", "funcție",
    "preşedinte", "președinte", "candidat", "primar",
    "mă", "îmi", "îi", "îl", "se",
}


def keyword_extract(text: str, top_n: int = 5) -> list[str]:
    """Extract distinctive keywords from a promise text."""
    words = re.findall(r"[a-zăâîșțA-ZĂÂÎȘȚ]+", text.lower())
    # Keep only longer words, exclude common
    words = [w for w in words if len(w) >= 5 and w not in SKIP_WORDS]
    # Dedup keeping order
    seen = set()
    out = []
    for w in words:
        if w not in seen:
            seen.add(w)
            out.append(w)
    return out[:top_n]


def search_corpus(keywords: list[str], min_matches: int = 2) -> list[dict]:
    """Find mandate docs that mention at least min_matches of the keywords."""
    hits = []
    for path in sorted(SRC_CORPUS.rglob("*.md")):
        if "/excluded/" in str(path):
            continue
        post = frontmatter.load(path)
        d = str(post.get("data", ""))[:10]
        if d < MANDATE_START:
            continue
        content = post.content.lower()
        matches = sum(1 for kw in keywords if kw in content)
        if matches >= min_matches:
            # Get a snippet around the first keyword found
            snippet = ""
            for kw in keywords:
                idx = content.find(kw)
                if idx >= 0:
                    start = max(0, idx - 100)
                    end = min(len(content), idx + 200)
                    snippet = post.content[start:end]
                    break
            hits.append({
                "doc_id": path.stem,
                "date": d,
                "matches": matches,
                "snippet": snippet.strip(),
            })
    hits.sort(key=lambda h: (-h["matches"], h["date"]))
    return hits


def main():
    random.seed(SEED)
    rows = []
    with SRC_STATUS.open() as f:
        for line in f:
            rows.append(json.loads(line))

    # Group by status
    by_status: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_status[r.get("status_status", "ERROR")].append(r)

    print("Status distribution:")
    for s, items in by_status.items():
        print(f"  {s}: {len(items)}")

    # Stratified sample
    samples = []
    for status in ["KEPT", "IN_PROGRESS", "NO_MENTION", "CONTRADICTED"]:
        n = min(N_PER_STATUS, len(by_status.get(status, [])))
        sample = random.sample(by_status.get(status, []), n)
        for s in sample:
            s["_audit_section"] = status
            samples.append(s)

    print(f"\nSampled {len(samples)} promises for audit (seed={SEED}).")

    md = [f"# Audit manual Pasul 4 — random sample 20 promisiuni (seed={SEED})\n"]
    md.append(f"Sample stratificat: {N_PER_STATUS} per status pentru KEPT, IN_PROGRESS, NO_MENTION + max {N_PER_STATUS} CONTRADICTED.\n")
    md.append("Pentru fiecare promisiune: (1) statusul + reasoning LLM, (2) supporting evidence din classifier, (3) keyword search INDEPENDENT în corpus mandat — pentru a vedea dacă există alte mențiuni pe care classifier-ul le-a ratat.\n")
    md.append("**Verdict manual** = adnotare ulterioară de mine după review.\n")

    current_section = None
    for i, s in enumerate(samples, 1):
        if s["_audit_section"] != current_section:
            current_section = s["_audit_section"]
            md.append(f"\n---\n## Status: {current_section}\n")

        promise_text = s["promise_text"]
        verbatim = s.get("verbatim_quote", "")
        keywords = keyword_extract(promise_text)
        independent_hits = search_corpus(keywords, min_matches=2)

        md.append(f"\n### {i}. [{s['topic']} / {s.get('specificity', '?')}] — sursa: {s.get('source_date', '?')}")
        md.append(f"\n**Promisiune:** {promise_text}")
        md.append(f"\n**Quote verbatim:** *\"{verbatim[:300]}\"*")
        md.append(f"\n**Status LLM:** `{s.get('status_status', '?')}` (confidence: {s.get('status_confidence', '?')})")
        md.append(f"\n**Raționament:** {s.get('status_reasoning', '')[:500]}")

        evs = s.get("status_supporting_evidence", [])
        if evs:
            md.append(f"\n**Supporting evidence din LLM:**")
            for e in evs[:3]:
                md.append(f"- *\"{e[:250]}\"*")

        md.append(f"\n**Keywords pentru independent search:** `{', '.join(keywords)}`")
        md.append(f"\n**Mențiuni independente în mandat ({len(independent_hits)} docs cu ≥2 keywords):**")
        if not independent_hits:
            md.append("- (none)")
        else:
            for h in independent_hits[:3]:
                md.append(f"- `{h['doc_id'][:70]}` ({h['date']}, {h['matches']} kw)")
                md.append(f"  - *\"{h['snippet'][:250]}\"*")
            if len(independent_hits) > 3:
                md.append(f"- _(și încă {len(independent_hits)-3} docs)_")

        md.append(f"\n**Verdict manual:** _ TODO _\n")

    OUT.write_text("\n".join(md))
    print(f"Output: {OUT}")
    print(f"  {len(samples)} sample-uri, gata de review manual.")


if __name__ == "__main__":
    main()
