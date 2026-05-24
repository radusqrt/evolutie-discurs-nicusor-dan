"""Diarize transcripts: input = data/1_canonical/ (pur), output = data/2_diarized/.

Algoritm CONSOLIDAT (v3):

  Format A — `>>` markers (YouTube auto-captions post-iul 2025):
    Phase 1: tot înainte de Q&A trigger ("sunt gata pentru întrebări") = [ND]
    Phase 2: alternare [JURNALIST] ↔ [ND] la fiecare ">>"
      cu override pe pattern de jurnalist intro (orice formă)

  Format B — fără markers (transcripts mai vechi):
    Split la pattern jurnalist intro, etichetează segmentul respectiv ca [JURNALIST]
    Restul = [ND]

  Patterns jurnalist intro (consolidat v1 + v2):
    - "Bună (ziua|seara), domnule? președinte" (formal)
    - "Bună (ziua|seara), [Nume Nume], [Canal]" (cu nume + canal)
    - "[Nume Nume], [Canal/TV]" (fără salut)
    - "Domnule? președinte, [text]"
    - "Dacă mi permiteți o (ultimă|altă) întrebare"
    - "Și (o)? ultima întrebare"
    - "Întrebare(a)?:" sau "O întrebare comună"
    - "Repet întrebarea"
    - "Aș vrea să vă întreb"

Joint conferences (cu Sandu/Zelensky/Rutte/etc.) NU sunt diarizate auto —
sunt copiate ca-atare în 2_diarized dacă au deja diarizare manuală în 1_canonical,
sau marcate `verificat: false` dacă nu.

Output e mereu re-derivat de la 0 (nu există patch incremental). Schimbi
algoritmul → re-rulezi → `data/2_diarized/` se regenerează complet.

Run:
    python scripts/04_diarize.py
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "1_canonical"
DST = ROOT / "data" / "2_diarized"

# ───────────────────────────────────────────────────────────────────────────────
# PATTERNS — consolidate (v1 + v2)
# ───────────────────────────────────────────────────────────────────────────────

# Jurnalist intro patterns: orice match la începutul unui segment îl etichetează [JURNALIST]
JOURNALIST_INTRO_PATTERNS = [
    # Formal: "Bună ziua, domnule președinte" + variations
    r"^Bună (ziua|seara|dimineața)[,]?\s+domnule? (preș|presed)edint",
    r"^Domnule? (preș|presed)edint",
    r"^Stimate? domn",
    # Self-intro: "Bună ziua, [Nume Nume], [Canal]"
    r"^Bună (ziua|seara|dimineața)[,]?\s+[A-ZĂÂÎȘȚ][\wÎȘȚăâîșț\-]+\s+[A-ZĂÂÎȘȚ][\wÎȘȚăâîșț\-]+",
    # "[Nume Nume], [TV]" (fără salut)
    r"^[A-ZĂÂÎȘȚ][\wÎȘȚăâîșț\-]+\s+[A-ZĂÂÎȘȚ][\wÎȘȚăâîșț\-]+,\s*(Televiziunea|Antena|Digi|Euronews|Pro\s*TV|B1|Kanal|Observator|Gândul|Hotnews|Recorder|Agerpres(s)?|Mediafax|stiripesurse|TVR|Realitatea)",
    # Follow-up requests
    r"^(Dacă|Daca)\s+(mi|îmi|i)?\s*(permiteți|permit|i|i?d)\s*[,]?\s*(vă rog\s*[,]?)?\s*(o (ultimă|altă)? întrebare|am o întrebare|să vă întreb)",
    r"^Și\s+(o\s+)?(ultima|ultimă|altă|alta)\s+întrebare",
    r"^Ultima întrebare",
    r"^Repet\s+întrebarea",
    r"^Aș vrea să\s+(vă întreb|întreb)",
    # Question signals
    r"^Întreb(are|area)\s*:",
    r"^O\s+întrebare(\s+(comună|legată|pentru|despre))?[,\.]",
    r"^Revin(.{0,30})cu o întrebare",
    # Reporter handoff
    r"^Mulțumesc.{0,80}domnule? președinte",
]
JOURNALIST_RE = re.compile("|".join(JOURNALIST_INTRO_PATTERNS), re.IGNORECASE)

# Q&A trigger: ND signals he's ready for questions
QA_TRIGGER_PATTERNS = [
    r"sunt(em)?\s+gata\s+(pentru|la|să răspund)\s+întreb",
    r"răspund.{0,40}întreb",
    r"sunt disponibil.{0,40}întreb",
    r"aștept(ăm)?\s+întreb",
]
QA_TRIGGER_RE = re.compile("|".join(QA_TRIGGER_PATTERNS), re.IGNORECASE)

# Skip joint conferences (heuristic doesn't handle them; preserve canonical if has manual diarize)
JOINT_KEYWORDS = [
    "maia sandu", "zelensky", "zelenskyy", "zelenschi",
    "secretarul general al nato", "mark rutte",
    "cancelarul german",
]


# ───────────────────────────────────────────────────────────────────────────────
# DIARIZATION ALGORITHM
# ───────────────────────────────────────────────────────────────────────────────

def is_joint_conference(post) -> bool:
    title = (str(post.get("sursa_titlu") or post.get("titlu_video") or "") + " " +
             str(post.get("nota", ""))).lower()
    return any(kw in title for kw in JOINT_KEYWORDS)


def split_markers(text: str) -> list[str]:
    """Split by '>>' markers."""
    return [s.strip() for s in re.split(r">>", text) if s.strip()]


def split_journalist_intros(text: str) -> list[str]:
    """Split paragraphs by journalist intro pattern."""
    paras = re.split(r"\n\n+", text)
    return [p.strip() for p in paras if p.strip()]


def diarize_markers_format(segments: list[str]) -> list[tuple[str, str]]:
    """Phase 1 (ND opening up to Q&A trigger) + Phase 2 (alternating JURNALIST↔ND)."""
    labeled: list[tuple[str, str]] = []
    trigger_idx = None
    for i, seg in enumerate(segments):
        if QA_TRIGGER_RE.search(seg):
            trigger_idx = i
            break

    if trigger_idx is None:
        # No clear trigger — alternate based on journalist intro pattern detection
        for seg in segments:
            tag = "JURNALIST" if JOURNALIST_RE.match(seg) else "ND"
            labeled.append((tag, seg))
        return labeled

    # Phase 1: all segments up to and including trigger = ND
    for i in range(trigger_idx + 1):
        labeled.append(("ND", segments[i]))
    # Phase 2: alternating JURNALIST → ND, with override on intro pattern
    speaker = "JURNALIST"
    for seg in segments[trigger_idx + 1:]:
        if JOURNALIST_RE.match(seg):
            speaker = "JURNALIST"
        labeled.append((speaker, seg))
        speaker = "ND" if speaker == "JURNALIST" else "JURNALIST"
    return labeled


def diarize_intros_format(segments: list[str]) -> list[tuple[str, str]]:
    """Each paragraph with journalist intro pattern → JURNALIST, rest → ND."""
    return [("JURNALIST" if JOURNALIST_RE.match(seg) else "ND", seg) for seg in segments]


def diarize_text(text: str) -> tuple[list[tuple[str, str]], str]:
    """Return labeled segments + which format was used."""
    if ">>" in text:
        segs = split_markers(text)
        return diarize_markers_format(segs), "markers"
    else:
        segs = split_journalist_intros(text)
        return diarize_intros_format(segs), "intros"


def format_diarized(labeled: list[tuple[str, str]]) -> str:
    return "\n\n".join(f"[{tag}] {content}" for tag, content in labeled)


# ───────────────────────────────────────────────────────────────────────────────
# MAIN
# ───────────────────────────────────────────────────────────────────────────────

def process_file(src: Path, dst: Path) -> dict:
    post = frontmatter.load(src)
    text = post.content

    # Special: if file already has manual multi-speaker tags (e.g., debate, joint conf),
    # copy as-is — those are part of curated source, not auto-applied.
    if re.search(r"\[(SIMION|RUTTE|OFICIAL|MODERATOR)", text):
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        return {"status": "copy-as-is (manual diarized)", "nd_segs": -1, "j_segs": -1}

    # Special: joint conferences with no manual tags → mark unverified, copy
    if is_joint_conference(post):
        post["verificat"] = False
        post["nota"] = (
            "Joint conference (cu Sandu/Zelensky/Rutte/etc.). Heuristic-ul nu poate "
            "distinge corect celălalt vorbitor de jurnalist. Necesită diarizare manuală sau audio-based."
        )
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(frontmatter.dumps(post))
        return {"status": "joint-unverified", "nd_segs": 0, "j_segs": 0}

    # Files that are clearly monologue (no [JURNALIST] expected) — short or marked
    # tip = facebook-post, anunt-candidatura, mesaj-anul-nou, discurs-victorie, etc.
    tip = str(post.get("tip", ""))
    if tip in ("facebook-post", "anunt-candidatura", "lansare-campanie",
               "discurs-victorie", "discurs-investitura", "mesaj-anul-nou",
               "mesaj-ziua-europei"):
        # Monolog by definition — all ND
        post["verificat"] = True
        post["metoda"] = f"monolog implicit (tip={tip})"
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(frontmatter.dumps(post))
        return {"status": "monologue", "nd_segs": 1, "j_segs": 0}

    # Apply diarization
    labeled, fmt = diarize_text(text)
    nd_count = sum(1 for tag, _ in labeled if tag == "ND")
    j_count = sum(1 for tag, _ in labeled if tag == "JURNALIST")

    post.content = format_diarized(labeled)
    post["verificat"] = True
    post["metoda"] = f"diarize.py v3 (format={fmt}, {nd_count} ND segs, {j_count} JURNALIST segs)"

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(frontmatter.dumps(post))
    return {"status": "diarized", "nd_segs": nd_count, "j_segs": j_count}


def main():
    # Clean output (re-derive from scratch)
    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True)

    files = list(SRC.rglob("*.md"))
    stats = {"diarized": 0, "monologue": 0, "joint-unverified": 0,
             "copy-as-is (manual diarized)": 0}
    nd_total = 0
    j_total = 0
    for src in sorted(files):
        rel = src.relative_to(SRC)
        dst = DST / rel
        result = process_file(src, dst)
        key = result["status"]
        stats[key] = stats.get(key, 0) + 1
        if result["nd_segs"] >= 0:
            nd_total += result["nd_segs"]
        if result["j_segs"] >= 0:
            j_total += result["j_segs"]

    print("=" * 70)
    print("DIARIZE — output: data/2_diarized/")
    print("=" * 70)
    for k, v in stats.items():
        print(f"  {k:<35} {v}")
    print(f"\nTotal ND segments produs: {nd_total:,}")
    print(f"Total JURNALIST segments produs: {j_total:,}")
    print(f"\nRule de aur: dacă ai fost vreodată tentat să rulezi acest script INCREMENTAL")
    print(f"sau să PATCH-uiești output-ul, NU face. Schimbi algoritmul aici + re-rulează.")


if __name__ == "__main__":
    main()
