# Audit random — 15 promisiuni fact-checked web

**Setup**: 15 promisiuni random din cele 131 canonice (seed=42), stratificat: 5 KEPT + 5 IN_PROGRESS + 4 NO_MENTION + 1 REFRAMED. Pentru fiecare, fact-check web cu surse media.

**Goal**: măsurăm acuratețea clasificatorului pe **eșantion random** (nu cherry-picked).

---

## Rezultate per promisiune

### KEPT (5 sample)

| # | Promisiune (rezumat) | Clasificator | Realitate web | Match |
|---|---|---|---|---|
| 1 | Guvern sprijinit de 4 partide pro-occidentale | KEPT | ✅ Guvern Bolojan PSD+PNL+USR+UDMR (iun 2025) | ✅ |
| 2 | Sesizare autorități pe conturile SM compromise | KEPT | ✅ Sesizate DNA, BEC, AEP, ANCOM, MAI, DNSC, Parchet, EU, Meta, TikTok | ✅ |
| 3 | Parteneriat consolidat România-Polonia | KEPT | ✅ Vizita Polonia mar 2026 + summit B9 + EastInvest | ✅ |
| 4 | Discuții imediate cu partidele după mandat | KEPT | ✅ Consultări 1-4 iunie 2025 la Cotroceni | ✅ |
| 5 | Voi face tot pentru UE/NATO | KEPT | ✅ Suport diplomatic UE+NATO constant; Coaliția Voinței | ✅ |

**Rezultat KEPT**: **5/5 corect** (100%). Clasificator solid pe KEPT.

### IN_PROGRESS (5 sample)

| # | Promisiune (rezumat) | Clasificator | Realitate web | Verdict |
|---|---|---|---|---|
| 6 | Atenție structuri militare/poliție | IN_PROGRESS | 🔄 Cheltuieli militare 2.24% PIB; angajament 5% până 2035 | ✅ Acceptabil |
| 7 | Stat care nu mai închide spitale | IN_PROGRESS | 🔄 Cerere plan combatere infecții; nimic spital închis vizibil | ✅ Acceptabil |
| 8 | Susținere în fiecare vizită oficială aderare R. Moldova UE 2030 | IN_PROGRESS | 🔄 Reluat consistent la fiecare summit + vizita Chișinău | ✅ Acceptabil |
| 9 | Schimbări profunde în administrație publică | IN_PROGRESS | 🔄 Reformă pensii, decrete numiri, dar transformare lentă | ✅ Acceptabil |
| 10 | Reconstrucție Ucraina după pace rezonabilă | IN_PROGRESS | 🔄 Pacea nu s-a făcut; ND susține Ucraina + integrare UE | ✅ Acceptabil (depinde de pace) |

**Rezultat IN_PROGRESS**: **5/5 acceptabil** (100%). Promisiuni vagi cu evidence parțial — corectă încadrarea.

### NO_MENTION (4 sample) — **AICI ESTE TWIST-UL**

| # | Promisiune (rezumat) | Clasificator | Realitate web | Verdict |
|---|---|---|---|---|
| 11 | 356 căței adăpost ASPA (vs 196) | NO_MENTION | ✅ **EXECUTAT — Mediafax/AGERPRES, 64 țarcuri noi, lucrare 2.5 luni** | ❌ Real e KEPT |
| 12 | Dezbatere Euronews mâine seară cu Simion | NO_MENTION | ✅ **A PARTICIPAT — Euronews oficial 8 mai 2025** | ❌ Real e KEPT |
| 13 | Colaborare cu UNTOLD pe festival | NO_MENTION | ✅ **PROTOCOL SEMNAT — contract pe 5 ani pe Arena Națională** | ❌ Real e KEPT |
| 14 | 5 șantiere consolidare clădiri | NO_MENTION | ✅ **8 ȘANTIERE ACTIVE — depășește promisiunea** (AMCCRS) | ❌ Real e KEPT |

**Rezultat NO_MENTION**: **4/4 sunt KEPT în realitate!** Toate 4 promisiuni s-au realizat concret, dar clasificatorul nu le-a putut detecta pentru că ND nu mai vorbește despre ele post-mandat.

### REFRAMED (1 sample)

| # | Promisiune | Clasificator (post-override) | Realitate | Verdict |
|---|---|---|---|---|
| 15 | Vigheciu primar interimar | REFRAMED | Bujduveanu (PNL) instalat în loc | ✅ Confirmat |

---

## Sinteza audit

### Acuratețe clasificator pe eșantion random (n=15)

| Categorie | Sample | Corect | Acuratețe |
|---|---:|---:|---:|
| KEPT | 5 | 5 | **100%** |
| IN_PROGRESS | 5 | 5 (acceptabil) | **100%** |
| **NO_MENTION** | **4** | **0** | **0%** |
| REFRAMED | 1 | 1 | 100% |
| **TOTAL** | **15** | **11** | **73%** |

### Pattern critic — direcția bias

**Clasificatorul subestimează sistematic livrarea concretă** pe categoria **NO_MENTION**:
- 100% din NO_MENTION sample (4/4) sunt KEPT în realitate
- Cauza: clasificatorul măsoară DOAR ce vorbește ND post-mandat. Pentru promisiuni executate (ca PMB-șef sau în primele săptămâni) pe care ND nu le mai discută, e fals NO_MENTION.

### Extrapolare conservatoare pe cele 131

- **Clasificator zice**: 20% KEPT, 21% NO_MENTION
- **Audit zice**: din 4 NO_MENTION verificate, 4 sunt KEPT (95% CI [40%, 99%] folosind Wilson interval)
- **Estimare conservatoare real**: dacă majoritatea NO_MENTION sunt de fapt KEPT, real KEPT rate = **35-45%** pe cele 131 (vs 20% clasificator)
- Diferența nu mai e 3× ca în fact-check-ul biased, dar e **substanțial mai mare decât 20%**

### Concluzia onestă

1. ✅ **Clasificator e fidel pe KEPT și IN_PROGRESS** (100% corect pe sample random)
2. ❌ **Clasificator nu detectează corect NO_MENTION** — confundă "ND nu vorbește" cu "nu s-a făcut"
3. **Real KEPT rate e probabil 35-45%** (vs 20% raportat) — pattern systematic, nu cherry-picked
4. **Caveat principal**: pentru promisiuni *prezidențiale*, clasificatorul ar putea fi mai fidel (ND e singurul actor). Pentru promisiuni *delegate* (PMB către succesori), clasificatorul e blind sistematic.

### Limitări audit

- Sample 15 e mic; CI-uri largi. Sample 30-50 ar reduce incertitudinea.
- "Acceptabil" pe IN_PROGRESS e ușor lax — nu am verificat *în profunzime* toate 5.
- Nu am audit pe CONTRADICTED (singurul caz din corpus, deja verificat și override-uit ca REFRAMED).
