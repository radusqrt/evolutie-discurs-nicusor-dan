# Sinteză — Evoluția discursului lui Nicușor Dan (Dec 2024 → Mai 2026)

## Date corpus

| metric | valoare |
|---|---:|
| Documente canonice | **389** (după dedup) |
| Documente brute colectate | 470 (81 near-duplicate eliminate, Jaccard ≥ 0.85) |
| Cuvinte totale | ~476,694 |
| Perioadă acoperită | 18 luni (Dec 2024 → Mai 2026) |
| Canale-sursă | 8 (Euronews, Digi24, Antena 3, B1, Privesc.Eu, Adm. Prez., canal personal, Kanal D) |
| Verificat / diarizat | 468 / 470 brute (2 joint conferences rămân nediarizate) |

**Pipeline de procesare** (fiecare pas are folder dedicat sau e materializat ca script):

| Pas | Acțiune | Locație |
|---|---|---|
| 1. DISCOVERY | catalogare candidați | `data/index/youtube_candidates.json` |
| 2. RAW | snapshot brut (immutable) | `data/0_raw/` (470 docs) |
| 3. DEDUPE | clustere Jaccard ≥ 0.85 | `data/1_canonical/` (389 docs) + `data/dedupe_report.md` |
| 4. DIARIZE | etichete `[ND]`/`[JURNALIST]` | inline (heuristic) + 1 manual |
| 5. CLEAN | lemmatizare + stopwords | inline în `corpus.py:tokenize()` |
| 6. PROJECT | filtru pe vocea ND | `corpus.py:strip_speaker_tags_to_nd()` |
| 7. ANALYZE | Pasul 1 + Pasul 2 | `results/01_basic/`, `results/02_tfidf/` |
| 8. INTERPRET | acest document | `results/SINTEZA.md` |

**Distribuție pe perioade canonice** (după dedup):

| Perioadă | Docs canonice | Cuvinte |
|---|---:|---:|
| 2024Q4-2025Q1 candidatură-precampanie | 29 | 53,037 |
| 2025Q2 campanie + investitură | 75 | 89,564 |
| 2025Q3 deficit + reformă economică | 47 | 98,591 |
| 2025Q4 stabilizare + diplomație | 58 | 55,423 |
| 2025Q4-2026Q1 reformă judiciară | **102** | 119,148 |
| 2026Q2 cotitură UE + criză guvern | 78 | 60,927 |

## Cele 6 etape ale discursului

### 1. **2024Q4-2025Q1 — Candidatură-precampanie** (29 docs)

Cuvinte distinctive: `lasconi · candidatură · ciolacu · primărie · tur · NATO · marcel · pantof · proeuropean · UDMR · ciucu · antonescu · cursă · scut`.

**Tonalitate:** poziționare electorală, raportare permanentă la concurenți (Lasconi, Ciolacu, Antonescu) și mediul politic existent (PSD-PNL, UDMR). Vocabularul e cel al unei campanii — "tur", "cursă", "candidatură", "președinție". Apar deja teme externe: NATO, "proeuropean", "scut" (antiBalistic).

### 2. **2025Q2 — Campanie + investitură** (76 docs)

Cuvinte distinctive: `tur · ceremonie · jurământ · antonescu · unitate · ponta · lasconi · ciolacu · opțiune · diasporă · solemn · depunere · victor · barcă · patriarh`.

**Tonalitate:** apex electoral. Două subteme: (a) ultima confruntare directă cu rivalii ("ponta", "victor", "barcă") și (b) ritualuri instituționale ("ceremonie", "jurământ", "depunere", "solemn", "patriarh"). Apariția "diasporă" ca temă majoră (diaspora a contat în turul 2).

### 3. **2025Q3 — Deficit + reformă economică** (47 docs)

Cuvinte distinctive: `pensionară · magistrat · pachet · anastasiu · SNSPA · salariu · violență · ANAF · profesor · victimă · certificat · femeie · iunie · spor · militar`.

**Tonalitate:** discurs tehnic de guvernare în plină criză bugetară. "Pachet" = pachetul fiscal Bolojan. "Anastasiu" / "ANAF" = lupta cu evaziunea fiscală. "Magistrat" / "pensionară" = prima fază a reformei pensiilor speciale. Surprinzător: temele sociale (violență, femeie, victimă, certificat) apar puternic — semn că președintele a făcut declarații pe agendă socială.

### 4. **2025Q4 — Stabilizare + diplomație** (58 docs)

Cuvinte distinctive: `militar · dronă · gheorghiu · alinia · inamic · aerian · SRI · dezinformare · vulnerabilitate · pace · SAFE · Polonia · tehnologic`.

**Tonalitate:** discurs de securitate/apărare devine dominant. "Dronă" + "aerian" + "inamic" = incidentele cu drone rusești pe teritoriul NATO. "SAFE" = mecanismul UE de finanțare a apărării. "Gheorghiu" = scandalul declarațiilor Oanei Gheorghiu. "Dezinformare" + "SRI" = focus pe războiul hibrid. Transformarea de la "primar-președinte" la "comandantul suprem al armatei".

### 5. **2025Q4-2026Q1 — Reformă judiciară** (102 docs — **cea mai prolifică perioadă**)

Cuvinte distinctive: `judecător · magistrat · judiciar · secție · disciplinar · inspecție · promovare · corupt · magistraturii · instanțelor · dosare · examen · Recorder`.

**Tonalitate:** confruntarea-cheie a mandatului — reforma justiției. Discursul devine **specialist-tehnic**: criterii de promovare, secție disciplinară, inspecție judiciară, examenele de magistratură. Apariția "Recorder" sugerează interviuri specifice cu jurnalismul de investigație. Plus "apă" (criza apei potabile din Prahova decembrie 2025) și "Gaza" (poziție internațională).

### 6. **2026Q2 — Cotitură UE + criză guvern** (78 docs)

Cuvinte distinctive: `Polonia · echipament · summit · nuclear · PNRR · moțiune · Iași · polonez · aderare · SAFE · petrol · cercetare · Timișoara · Orientul (Mijlociu)`.

**Tonalitate:** discurs de **leader regional** + criză internă. "Moțiune" + "format" + "scenarie" = căderea guvernului Bolojan și consultările pentru noul executiv. "Polonia / polonez / Iași / Timișoara" = parteneriate bilaterale + B9. "Nuclear" + "petrol" + "Orientul" = atacurile asupra Iranului, securitate energetică. PNRR rămâne preocupare.

## Insight-uri sintetice

### Arcul narativ vizibil

**Diagnostic critic → mobilizare electorală → tehnocrat al guvernării → comandant suprem → reformator instituțional → leader regional**.

Aceeași persoană, dar discursul migrează **de la idealuri către detaliu tehnic** și **de la intern către regional/internațional** pe parcurs.

### Constante (apar în toate perioadele)

- `românia` (cuvântul-pilon, dominant peste tot)
- `interes` (de obicei "interes național")
- `om / oameni` (apel la categorii sociale)
- `trebui` / `putea` / `vrea` (modalitate — el e cineva care **trebuie** să facă lucruri)
- `împreună` (cuvânt-fanion al campaniei și mandatului)

### Transformări frapante

1. **Dispariția polemicii electorale**: După mai 2025, numele rivalilor (Ciolacu, Lasconi, Antonescu, Simion) devin invizibile. Discursul nu mai e despre adversari, ci despre **probleme**.

2. **Reformă judiciară devine "subiectul lui"**: 102 docs în 3 luni — niciun alt subiect nu primește acest volum.

3. **Politică externă crescândă**: Q4 2025 introduce vocabular militar (dronă, aerian, SRI, dezinformare); Q2 2026 introduce vocabular geopolitic (Polonia, NATO, Orientul Mijlociu).

4. **Stilul rămâne**: tot timpul predomină verbe modale ("trebui", "putea", "vrea") și o construcție pragmatică-tehnică. Nu apar metafore puternice sau retorica înflăcărată.

### Limite ale analizei

- Transcripturile YouTube auto-generate au erori minore de transcriere (cuvinte concatenate, lipsă diacritice ocazionale)
- 2 joint conferences (Sandu, Zelensky) sunt încă nediarizate (ND vs alt vorbitor)
- TF-IDF surprinde **distincții** între perioade — nu cuvintele cele mai folosite, ci cele care apar mai mult **într-o perioadă vs altele**
- spaCy lemmatizer ocazional concatenează entități multi-token (ex. "stateleunitealeamericii", "northatlantictreatyorganization")

## Pașii următori posibili

1. **Sentiment per perioadă** — folosind `readerbench/ro-sentiment` (RoBERT)
2. **Topic modeling** cu BERTopic — descoperă teme automat, nu pe perioade predefinite
3. **Frame analysis** — *cum* încadrează corupția, reforma, UE
4. **Comparativ cu predecesori** — Iohannis pe aceleași teme, ce e distinctiv în vocea ND
5. **Network analysis** — co-ocurența de concepte (ex: "reformă" cu ce apare împreună)
6. **Re-diarizare audio-based** pe joint conferences (Sandu, Zelensky)

## Surse de date

Repo organizat în:

- `data/0_raw/` — snapshot imutabil al colecției brute (470 docs)
- `data/1_canonical/` — corpus canonic dedupat (389 docs, sursa de adevăr pentru analiză)
- `data/raw/` — același cu `data/0_raw/`, păstrat pentru compatibilitate
  - `oficial/` — 7 manual-curated (anchor speeches)
  - `interviuri/` — 1 dezbatere
  - `youtube/` — 462 transcripturi YouTube (cu metadata bogată per fișier)
  - `excluded/` — 1 conferință primarie (off-topic)
- `data/index/youtube_candidates.json` — catalog 608 candidați
- `data/index/wikipedia_chronology.md` — index master de evenimente
- `data/dedupe_report.md` — raport detaliat clustere & duplicate eliminate
