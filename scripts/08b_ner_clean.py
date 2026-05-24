"""Pasul 8b: Curăță output-ul NER — merge forme flexionale, scoate hashtag/artifacts.

Input:  results/08_ner_{PROJECTION}/entities_per_doc.jsonl
Output: ...clean.jsonl + top_entities_clean.csv + entity_timeline_clean.csv
"""
from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from pathlib import Path

import pandas as pd

PROJECTION = os.getenv("PROJECTION", "overall")
ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "results" / f"08_ner_{PROJECTION}" / "entities_per_doc.jsonl"
OUT_DIR = ROOT / "results" / f"08_ner_{PROJECTION}"

# Hashtag / artifact / ambiguous → SKIP
SKIP_CANONICALS = {
    "nicusorpresedinte", "romaniaonesta", "romaniaputernica",
    "nicusordan", "alegeriprezidentiale", "faravotpierdemtot",
    "nd11", "cmf", "puternici", "fyp",
    # Too generic / ambiguous (ND or another president?)
    "presedinte", "președinte", "președintele", "presedintele",
    "președintelui", "presedintelui", "presedinta",
    # Generic words
    "om", "oameni", "domn", "domnul",
    # Misclassifications
    "pnrr", "psd-ul",  # PNRR is a program; "psd-ul" is bad form
}

# Map inflectional/aliased forms → canonical
CANONICAL_MAP = {
    # Țări — RO inflectional forms
    "românia": "ROMÂNIA", "româniei": "ROMÂNIA", "românie": "ROMÂNIA",
    "ucraina": "UCRAINA", "ucrainei": "UCRAINA", "ucrainian": "UCRAINA",
    "rusia": "RUSIA", "rusiei": "RUSIA", "rusiei": "RUSIA",
    "sua": "SUA", "statele unite": "SUA", "statelor unite": "SUA",
    "r. moldova": "R. MOLDOVA", "republica moldova": "R. MOLDOVA",
    "republicii moldova": "R. MOLDOVA", "moldova": "R. MOLDOVA",
    "polonia": "POLONIA", "poloniei": "POLONIA",
    "franța": "FRANȚA", "franței": "FRANȚA",
    "germania": "GERMANIA", "germaniei": "GERMANIA",
    "italia": "ITALIA", "italiei": "ITALIA",
    "ungaria": "UNGARIA", "ungariei": "UNGARIA",
    "bulgaria": "BULGARIA", "bulgariei": "BULGARIA",
    "uk": "UK", "marea britanie": "UK", "regatul unit": "UK",
    "china": "CHINA", "chinei": "CHINA",

    # Persoane politice
    "trump": "TRUMP", "donald trump": "TRUMP",
    "putin": "PUTIN", "vladimir putin": "PUTIN",
    "zelenski": "ZELENSKI", "zelensky": "ZELENSKI", "volodimir zelenski": "ZELENSKI",
    "bolojan": "BOLOJAN", "ilie bolojan": "BOLOJAN",
    "ciolacu": "CIOLACU", "marcel ciolacu": "CIOLACU",
    "simion": "SIMION", "george simion": "SIMION",
    "georgescu": "GEORGESCU", "călin georgescu": "GEORGESCU", "calin georgescu": "GEORGESCU",
    "maia sandu": "MAIA SANDU", "sandu": "MAIA SANDU",
    "iohannis": "IOHANNIS", "klaus iohannis": "IOHANNIS",
    "orban": "ORBAN", "viktor orban": "ORBAN", "viktor orbán": "ORBAN",
    "ursula vdl": "URSULA VDL", "von der leyen": "URSULA VDL",
    "ursula von der leyen": "URSULA VDL",
    "macron": "MACRON", "emmanuel macron": "MACRON",
    "ciucu": "CIUCU", "ciprian ciucu": "CIUCU",
    "bujduveanu": "BUJDUVEANU", "stelian bujduveanu": "BUJDUVEANU",
    "ponta": "PONTA", "victor ponta": "PONTA",
    "kallas": "KALLAS", "kaja kallas": "KALLAS",
    "rutte": "RUTTE", "mark rutte": "RUTTE",
    "patriarhul daniel": "PATRIARHUL DANIEL", "daniel": "PATRIARHUL DANIEL",
    "lasconi": "LASCONI", "elena lasconi": "LASCONI",
    "fritz": "FRITZ", "dominic fritz": "FRITZ",

    # Instituții naționale
    "csm": "CSM",
    "ccr": "CCR", "curtea constituțională": "CCR",
    "dna": "DNA",
    "diicot": "DIICOT",
    "parlament": "PARLAMENT", "parlamentul": "PARLAMENT",
    "guvernul": "GUVERN", "guvern": "GUVERN", "guvernului": "GUVERN",
    "statul român": "STATUL ROMÂN",
    "anaf": "ANAF",
    "bnr": "BNR", "banca națională": "BNR", "banca națională a românie": "BNR",
    "presedentia": "ADMINISTRAȚIA PREZIDENȚIALĂ",
    "administrația prezidențială": "ADMINISTRAȚIA PREZIDENȚIALĂ",

    # Instituții internaționale
    "ue": "UE", "uniunea europeană": "UE", "uniunea europeana": "UE",
    "uniunea": "UE", "uniunii europene": "UE",
    "nato": "NATO",
    "ocde": "OCDE", "oecd": "OCDE",
    "onu": "ONU", "organizația națiunilor unite": "ONU",
    "ce": "COMISIA EUROPEANĂ", "comisia europeană": "COMISIA EUROPEANĂ",
    "parlamentul european": "PARLAMENTUL EUROPEAN", "pe": "PARLAMENTUL EUROPEAN",

    # Partide
    "psd": "PSD", "psd-ul": "PSD",
    "pnl": "PNL", "pnl-ul": "PNL",
    "usr": "USR", "usr-ul": "USR",
    "aur": "AUR", "aur-ul": "AUR",
    "udmr": "UDMR",
    "pot": "POT", "sos": "SOS",
}


def normalize(name: str) -> str:
    n = name.strip().lower()
    n = re.sub(r"\s+", " ", n)
    return CANONICAL_MAP.get(n, None)  # None if not in map → likely irrelevant noise


def main():
    if not SRC.exists():
        print(f"ERROR: {SRC} not found")
        return

    docs = []
    with SRC.open() as f:
        for line in f:
            docs.append(json.loads(line))

    cleaned_docs = []
    mention_rows = []
    for d in docs:
        clean_ents: dict[str, dict] = {}  # canonical -> aggregated entity
        for e in d.get("entities", []):
            old_canon = e["canonical"]
            if old_canon in SKIP_CANONICALS:
                continue
            new_canon = normalize(old_canon)
            if new_canon is None:
                continue  # not in our curated map → skip noise
            if new_canon not in clean_ents:
                clean_ents[new_canon] = {
                    "canonical": new_canon,
                    "label": e["label"],
                    "count": 0,
                    "raw_forms": set(),
                    "max_score": 0.0,
                }
            clean_ents[new_canon]["count"] += e["count"]
            for f in e.get("raw_forms", [e.get("canonical", new_canon)]):
                clean_ents[new_canon]["raw_forms"].add(f)
            clean_ents[new_canon]["max_score"] = max(
                clean_ents[new_canon]["max_score"], e["max_score"])
        for ent in clean_ents.values():
            ent["raw_forms"] = sorted(ent["raw_forms"])
            mention_rows.append({
                "doc_id": d["id"], "date": d["date"], "tip": d.get("tip", ""),
                "canonical": ent["canonical"], "label": ent["label"],
                "count": ent["count"], "max_score": round(ent["max_score"], 3),
            })
        cleaned_docs.append({
            "id": d["id"], "date": d["date"], "tip": d.get("tip", ""),
            "entities": list(clean_ents.values()),
        })

    # Save cleaned per-doc
    with (OUT_DIR / "entities_per_doc_clean.jsonl").open("w") as f:
        for d in cleaned_docs:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")

    df = pd.DataFrame(mention_rows)
    df.to_csv(OUT_DIR / "mentions_clean.csv", index=False)
    print(f"Cleaned mentions: {len(df)} rows (was {sum(len(d.get('entities', [])) for d in docs)} unique-per-doc)")

    # Top entities
    top = df.groupby(["canonical", "label"])["count"].sum().reset_index()
    top = top.sort_values("count", ascending=False)
    top.to_csv(OUT_DIR / "top_entities_clean.csv", index=False)
    print("\nTop 30 entities after cleaning:")
    print(top.head(30).to_string(index=False))

    # Add period column
    def period_for(d):
        y, m = int(d[:4]), int(d[5:7])
        if y == 2024 or (y == 2025 and m <= 2): return "2024Q4-2025Q1"
        if y == 2025 and m <= 5: return "2025Q2"
        if y == 2025 and m <= 8: return "2025Q3"
        if y == 2025 and m <= 11: return "2025Q4"
        if y == 2025 and m == 12 or (y == 2026 and m <= 2): return "2026Q1"
        if y == 2026 and m <= 5: return "2026Q2"
        return "outside"
    df["period"] = df["date"].apply(period_for)

    # Entity timeline (top 25)
    top_25 = top.head(25)["canonical"].tolist()
    timeline = df[df["canonical"].isin(top_25)].groupby(
        ["canonical", "period"])["count"].sum().unstack(fill_value=0)
    timeline["_total"] = timeline.sum(axis=1)
    timeline = timeline.sort_values("_total", ascending=False).drop(columns=["_total"])
    timeline.to_csv(OUT_DIR / "entity_timeline_clean.csv")

    print(f"\nEntity timeline saved.")
    print(timeline.head(20).to_string())


if __name__ == "__main__":
    main()
