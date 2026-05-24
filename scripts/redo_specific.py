"""Re-run LLM diarize on specific files (delete from 2_diarized, re-run script)."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
DST = ROOT / "data" / "2_diarized" / "youtube"

# Files identified in audit as having issues (UNKNOWN where OFICIAL should be)
FILES_TO_REDO = [
    "2025-05-15_mirabela-gradinaru-partenera-lui-nicusor-dan-despre-momentel.md",
    "2025-12-21_nicusor-dan-exista-magistrati-care-actioneaza-in-interesul-u.md",
    "2025-05-04_nicusor-dan-sa-ne-raportam-cu-pruden-a-la-rezultatele-exit-p.md",
]

for name in FILES_TO_REDO:
    f = DST / name
    if f.exists():
        f.unlink()
        print(f"Deleted: {name}", file=sys.stderr)
    else:
        print(f"Not found: {name}", file=sys.stderr)

print("\nNow run: python scripts/04d_diarize_llm_v2.py --workers 3", file=sys.stderr)
