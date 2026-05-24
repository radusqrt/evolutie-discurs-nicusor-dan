# Evoluția discursului — Nicușor Dan

Analiză cantitativă a discursului lui **Nicușor Dan** (Președintele României) în perioada **candidatură → primul an de mandat** (decembrie 2024 → mai 2026).

**Subiect și goal**: vezi [`BRIEF.md`](./BRIEF.md). Rezultate sintetice: [`results/SINTEZA.md`](./results/SINTEZA.md).

## TL;DR

- **1,525 documente brute** colectate din **9 surse** (Facebook NicusorDan.ro, 8 canale YouTube)
- **1,114 documente canonice** după dedup (Jaccard ≥ 0.85)
- **~652,961 cuvinte** analizate
- **6 etape de discurs** detectate cu TF-IDF pe perioade
- Arc narativ: *diagnostic critic → mobilizare electorală → tehnocrat → comandant suprem → reformator instituțional → leader regional*

## Pipeline (8 pași)

| # | Pas | Script / Acțiune | Output |
|---|---|---|---|
| 1 | **Discovery** | `scripts/list_candidates.py` (yt-dlp prin proxy Webshare) | `data/index/youtube_candidates.json` (608 candidați) |
| 2 | **Raw collection** | `scripts/fetch_from_candidates.py` (YouTube) + `scripts/fb_apify_collect.py` (Facebook prin Apify) | `data/raw/` (1,525 docs cu YAML frontmatter) |
| 3 | **Dedupe** | `scripts/03_dedupe.py` (Jaccard cu canonical pick prioritar) | `data/1_canonical/` (1,114 docs) + `data/dedupe_report.md` |
| 4 | **Diarize** | `scripts/diarize_heuristic.py` (>>+intros patterns) + manual pentru joint conferences | inline în .md cu etichete `[ND]/[JURNALIST]/[RUTTE]/...` |
| 5 | **Clean** | `scripts/corpus.py:tokenize()` (spaCy `ro_core_news_sm` + `stopwordsiso`) | runtime |
| 6 | **Project** | `scripts/corpus.py:strip_speaker_tags_to_nd()` (filtrare voce ND) | runtime |
| 7 | **Analyze** | `scripts/01_basic_analysis.py` (stats + wordclouds + top-N) + `scripts/02_tfidf_temporal.py` (TF-IDF + bigrame + perioade) | `results/01_basic/`, `results/02_tfidf/` |
| 8 | **Interpret** | manual | `results/SINTEZA.md` |

## Surse de date

### Video / YouTube (462 docs)

| Canal | Docs |
|---|---:|
| Euronews Romania | 132 |
| Digi24 HD | 125 |
| Antena 3 CNN | 95 |
| B1 TV | 61 |
| Privesc.Eu România | 41 |
| Administrația Prezidențială | 4 |
| Canal personal NicusorDan | 2 |
| Kanal D Romania | 2 |

### Facebook (1,054 docs)

- Pagina `NicusorDan.ro`
- Perioada 20 feb 2025 → 21 mai 2026
- Colectat prin actor Apify `apify/facebook-posts-scraper`
- Metadata: post_id, aprecieri, comentarii, distribuiri

### Manual curated (9 docs)

7 discursuri-ancoră transcrise/verificate manual (anunț candidatură, lansare campanie, dezbatere TV vs. Simion, victorie, învestitură, conferința Cotroceni, autoevaluare 100 zile, mesaj Anul Nou).

## Metodologia de dedup

**Necesitate**: același eveniment (ex. o conferință de presă) e adesea acoperit de mai multe canale TV cu clipuri diferite + re-uploads pe același canal. Filename-level dedup (același `video_id`) prinde doar duplicate evidente. Pentru near-duplicate (același conținut, diferit upload), folosim similaritate textuală.

**Algoritm** (`scripts/03_dedupe.py`):

1. **Grupare pe dată** — doar documentele din aceeași zi sunt candidate la dedup (limitează O(n²) și e logic: clipuri ale aceluiași eveniment sunt din aceeași zi)
2. **Pairwise similarity** — Jaccard pe seturi de tokens între fiecare pereche în grup
3. **Clustering** — Union-Find pe graful unde muchiile sunt perechi cu Jaccard ≥ **0.85** (prag empiric: 1.0 = re-upload identic, 0.85 = >85% overlap content, 0.4 = teme diferite din același eveniment, < 0.2 = unrelated)
4. **Canonical pick** per cluster, în această ordine de prioritate:
   1. **Canal** (Adm. Prezidențială > Privesc.Eu > Canal personal > Manual > Digi24 > Euronews > Antena 3 > B1 > Kanal D)
   2. **Lungime** (cel mai lung text = cea mai completă acoperire)
   3. **Vizionări** (signal de popularitate)
5. **Output** — copie a fișierelor canonice către `data/1_canonical/` păstrând structura de foldere; report cu toate clusterele și ce a fost dropped în `data/dedupe_report.md`

**Rezultat actual**: 1,525 → 1,114 docs (411 dropped, 392 clustere cu duplicate).

**De ce 0.85?**
- 1.0 (exact) prinde doar re-uploads cu același transcript byte-for-byte. Captions auto-generate YouTube **nu sunt deterministe** (poate varia cu 1-2 cuvinte).
- 0.95-0.99 ar fi prea strict — pierde re-uploads cu mici diferențe.
- 0.85 e dezbătut în literatura de dedup ca threshold "near-duplicate" — văzut de noi că surprinde corect re-uploads pe același canal (Jaccard 1.00 când e exact, ~0.92 când e versiune ușor diferită) și NU prinde fals clipuri tematice cross-channel (Jaccard 0.07-0.15 între B1/Antena 3/Digi24 pe același eveniment = conținut diferit).
- 0.7-0.8 ar fi prea slab — încep să se piardă clipuri tematice valide.

## Metodologia de diarizare

Transcripturile YouTube auto-generate au două formate frecvente:

1. **`>>` markers** (post iulie 2025 pe canalul Privesc.Eu): YouTube marchează schimbarea vorbitorului cu `>>`. Diarize-ul nostru:
   - Phase 1 (opening): toate segmentele înainte de trigger phrase ("sunt gata pentru întrebări") = `[ND]`
   - Phase 2 (Q&A): alternare `[JURNALIST]` ↔ `[ND]` la fiecare `>>`, cu override la pattern de intro jurnalist
2. **Intro patterns** (iunie 2025): jurnaliștii se identifică prin pattern-uri ca "Bună ziua, domnule președinte". Detectate cu regex.

**Joint conferences** (cu Sandu, Zelensky, Rutte) — heuristicul falsifică (etichetează partenerul ca jurnalist). Pentru ele: diarizare manuală (1 fișier completat — Rutte; 2 rămase nediarizate).

**FB posts**: implicit monolog, fără diarizare.

## Cum se rulează

```bash
# Setup (one-time)
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download ro_core_news_sm

# Credentials (.env)
WEBSHARE_PROXY_USERNAME=...
WEBSHARE_PROXY_PASSWORD=...
APIFY_TOKEN=apify_api_...

# Colectare (incrementală — dedupe la fetch evită re-fetch)
python scripts/list_candidates.py
python scripts/fetch_from_candidates.py
python scripts/fb_apify_collect.py --page NicusorDan.ro --limit 1000
python scripts/fb_pull_dataset.py  # re-pull dacă scraper-ul a fost abortat

# Dedup
python scripts/03_dedupe.py

# Diarizare
python scripts/diarize_heuristic.py

# Analiză
python scripts/01_basic_analysis.py            # wordclouds + stats
python scripts/02_tfidf_temporal.py            # TF-IDF + bigrame + perioade
```

## Structura repo

```
data/
├── raw/                     # 1,525 docs brute (immutable corpus)
├── 1_canonical/             # 1,114 docs după dedup (sursa de adevăr pentru analiză)
├── index/
│   ├── youtube_candidates.json
│   └── wikipedia_chronology.md
└── dedupe_report.md         # clustere + drops

scripts/
├── corpus.py                # loader: spaCy ro_core_news_sm + stopwordsiso
├── proxy.py                 # Webshare rotation random 1-200
├── list_candidates.py       # discovery YouTube
├── fetch_from_candidates.py # download via proxy
├── youtube_collect.py       # all-in-one YouTube collection (alternativ)
├── fb_apify_collect.py      # Facebook via Apify
├── fb_pull_dataset.py       # pull Apify dataset existing
├── enrich_metadata.py       # backfill metadata yt-dlp
├── diarize_heuristic.py     # >>+intros diarization
├── 01_basic_analysis.py     # wordclouds + top-N + stats
├── 02_tfidf_temporal.py     # TF-IDF distinctive + bigrame + perioade
└── 03_dedupe.py             # Jaccard ≥0.85 clustering

results/
├── 01_basic/                # wordcloud + top-20 bar chart × 1,114 docs + combinate
├── 02_tfidf/                # TF-IDF distinctive (per doc + per perioadă) + bigrame
└── SINTEZA.md               # narațiunea finală a evoluției

BRIEF.md                     # project brief: subiect, goal, reguli metodologice
requirements.txt             # Python deps
.env.example                 # template credentiale (.env gitignored)
```

## Limitări cunoscute

- **Transcripturile YouTube auto-generate** au erori minore: cuvinte concatenate (rar), lipsă diacritice (rar), entități multi-token concatenate de spaCy lemmatizer (ex: `stateleunitealeamericii`).
- **2 joint conferences** (Sandu 2025-06-10, Zelensky 2026-03-13) sunt nediarizate — partenerul lor de vorbit ar fi fost etichetat fals ca jurnalist de heuristic.
- **Facebook nu acoperă** perioada precandidatură (dec 2024 - feb 2025) sub 32 posturi/lună — actor Apify a stopat scraping-ul la $5 credit limit.
- **TF-IDF surprinde distincții** între perioade, NU cuvinte cele mai folosite. Pentru rangul absolut de frecvență vezi `results/01_basic/`.
- **Apply de etape definite manual** (6 perioade politice) — următorul pas e topic modeling (BERTopic) care descoperă teme automat.

## Continuare

Pașii naturali de făcut acum (ordinea recomandată):

1. **Topic modeling (BERTopic)** — descoperă teme automat, fără perioade impuse din afară
2. **FB vs YouTube comparativ** — stil scris vs vorbit
3. **Sentiment per perioadă** (RoBERT readerbench/ro-sentiment) — arc emoțional
4. **Frame analysis** — cum încadrează ND temele majore (corupție, UE, reformă, Rusia)
