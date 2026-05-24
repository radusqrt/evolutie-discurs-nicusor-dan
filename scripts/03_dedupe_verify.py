"""Spot-check verification of dedupe results.

Three checks:
  A. CANONICAL vs DROPPED — for 5 random dropped clusters, show texts
     side-by-side. Drops should look clearly similar.
  B. Just-below-threshold pairs — find same-day pairs with Jaccard ∈ [0.70, 0.85).
     These should look clearly DIFFERENT (content-wise).
  C. Cross-channel same-day pairs that were NOT dropped (low Jaccard) —
     verify they're truly different clips of same event.
"""
from __future__ import annotations

import random
from collections import defaultdict
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
CANON = ROOT / "data" / "1_canonical"
REPORT = ROOT / "data" / "dedupe_report.md"

random.seed(42)


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def load_docs(src: Path) -> list[dict]:
    docs = []
    for f in sorted(src.rglob("*.md")):
        if "/excluded/" in str(f):
            continue
        p = frontmatter.load(f)
        docs.append({
            "path": f,
            "rel": str(f.relative_to(src)),
            "date": str(p.get("data", "")),
            "channel": str(p.get("sursa_canal", "")),
            "title": str(p.get("sursa_titlu", f.name))[:80],
            "content": p.content,
            "tokens": set(p.content.split()),
            "words": len(p.content.split()),
        })
    return docs


def parse_clusters(report_path: Path) -> list[dict]:
    """Parse dedup report into list of clusters with kept + dropped."""
    text = report_path.read_text()
    clusters = []
    current = None
    state = None
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("### "):
            if current:
                clusters.append(current)
            current = {"date": line.replace("### ", ""), "kept": None, "dropped": []}
            state = None
        elif "Kept canonical:" in line:
            state = "kept"
            # filename in ` `
            import re
            m = re.search(r"`([^`]+)`", line)
            if m and current:
                current["kept_file"] = m.group(1)
        elif "Dropped:" in line:
            state = "dropped"
        elif state == "dropped" and line.startswith("- `"):
            import re
            m = re.search(r"`([^`]+)`", line)
            if m and current:
                current["dropped"].append(m.group(1))
    if current:
        clusters.append(current)
    return clusters


def main():
    raw_docs = load_docs(RAW)
    by_rel = {d["rel"]: d for d in raw_docs}
    clusters = parse_clusters(REPORT)
    real_clusters = [c for c in clusters if c.get("kept_file") and c.get("dropped")]
    print(f"Clusters in report: {len(real_clusters)}\n")

    # ─── A. Verify drops are actually similar ─────────────────────────────────
    print("=" * 80)
    print("A. DROPPED PAIRS — should be CLEARLY SIMILAR")
    print("=" * 80)
    sample = random.sample(real_clusters, min(5, len(real_clusters)))
    for c in sample:
        kept = by_rel.get(c["kept_file"])
        if not kept:
            continue
        for drop_rel in c["dropped"][:1]:  # just first dropped
            dropped = by_rel.get(drop_rel)
            if not dropped:
                continue
            j = jaccard(kept["tokens"], dropped["tokens"])
            print(f"\n--- {c['date']} | Jaccard={j:.2f} ---")
            print(f"  KEPT    [{kept['channel'][:25]:<25}] ({kept['words']}w): {kept['title']}")
            print(f"   text:  {kept['content'][:140]}")
            print(f"  DROPPED [{dropped['channel'][:25]:<25}] ({dropped['words']}w): {dropped['title']}")
            print(f"   text:  {dropped['content'][:140]}")

    # ─── B. Just-below-threshold pairs ────────────────────────────────────────
    print("\n" + "=" * 80)
    print("B. NEAR-MISS pairs (Jaccard ∈ [0.5, 0.85)) — should be DIFFERENT content")
    print("=" * 80)
    by_date = defaultdict(list)
    for d in raw_docs:
        by_date[d["date"]].append(d)
    near_misses = []
    for date, lst in by_date.items():
        if len(lst) < 2:
            continue
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                jv = jaccard(lst[i]["tokens"], lst[j]["tokens"])
                if 0.5 <= jv < 0.85:
                    near_misses.append((jv, lst[i], lst[j]))
    print(f"\nFound {len(near_misses)} near-miss pairs total.\n")
    sample = random.sample(near_misses, min(5, len(near_misses)))
    for jv, a, b in sample:
        print(f"\n--- {a['date']} | Jaccard={jv:.2f} ---")
        print(f"  [{a['channel'][:25]:<25}] ({a['words']}w): {a['title']}")
        print(f"   text:  {a['content'][:140]}")
        print(f"  [{b['channel'][:25]:<25}] ({b['words']}w): {b['title']}")
        print(f"   text:  {b['content'][:140]}")

    # ─── C. Cross-channel same-day kept (low Jaccard expected) ────────────────
    print("\n" + "=" * 80)
    print("C. CROSS-CHANNEL same-day pairs NOT dropped (should be diff clips of same event)")
    print("=" * 80)
    cross_ch_kept = []
    for date, lst in by_date.items():
        if len(lst) < 2:
            continue
        # Find pairs with same date, different channels, Jaccard < 0.85
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i]["channel"] == lst[j]["channel"]:
                    continue
                jv = jaccard(lst[i]["tokens"], lst[j]["tokens"])
                if jv < 0.85 and jv > 0.05:  # > 0.05 ensures topical overlap
                    cross_ch_kept.append((jv, lst[i], lst[j]))
    print(f"\nFound {len(cross_ch_kept)} cross-channel pairs (overlap but distinct).\n")
    sample = random.sample(cross_ch_kept, min(3, len(cross_ch_kept)))
    for jv, a, b in sample:
        print(f"\n--- {a['date']} | Jaccard={jv:.2f} ---")
        print(f"  [{a['channel'][:25]:<25}] ({a['words']}w): {a['title']}")
        print(f"   text:  {a['content'][:140]}")
        print(f"  [{b['channel'][:25]:<25}] ({b['words']}w): {b['title']}")
        print(f"   text:  {b['content'][:140]}")

    # ─── Statistics: Jaccard distribution ─────────────────────────────────────
    print("\n" + "=" * 80)
    print("D. JACCARD DISTRIBUTION across all same-date pairs")
    print("=" * 80)
    bins = {"≥0.95": 0, "0.85-0.95": 0, "0.70-0.85": 0, "0.50-0.70": 0, "0.30-0.50": 0,
            "0.10-0.30": 0, "<0.10": 0}
    total_pairs = 0
    for date, lst in by_date.items():
        if len(lst) < 2:
            continue
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                total_pairs += 1
                jv = jaccard(lst[i]["tokens"], lst[j]["tokens"])
                if jv >= 0.95: bins["≥0.95"] += 1
                elif jv >= 0.85: bins["0.85-0.95"] += 1
                elif jv >= 0.70: bins["0.70-0.85"] += 1
                elif jv >= 0.50: bins["0.50-0.70"] += 1
                elif jv >= 0.30: bins["0.30-0.50"] += 1
                elif jv >= 0.10: bins["0.10-0.30"] += 1
                else: bins["<0.10"] += 1
    print(f"\nTotal same-date pairs: {total_pairs}\n")
    for label, n in bins.items():
        pct = 100 * n / max(total_pairs, 1)
        bar = "█" * int(pct / 2)
        marker = " ← drops" if label in ("≥0.95", "0.85-0.95") else ""
        print(f"  {label:<10} {n:>5} ({pct:5.1f}%) {bar}{marker}")


if __name__ == "__main__":
    main()
