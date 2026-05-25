# Stylometry formală — Burrows' Delta + PCA + RF

**Corpus**: 718 documente (≥50 cuvinte fiecare)
- Scris (Facebook): 392
- Vorbit (video): 326

**Metodă**: top 100 function words (POS: ADP/AUX/CCONJ/DET/PART/PRON/SCONJ), frecvențe relative z-normalizate.

## Rezultat 1 — Burrows' Delta

**Distanță centroidă scris ↔ vorbit**: `0.297`

**Accuracy nearest-centroid clasificare** (la care centroid e mai aproape fiecare doc): **78.1%**

Dacă FB și video ar fi indistinguibile stilometric, accuracy ar fi ~50% (random). Cu cât mai mare, cu atât mai distincte sunt cele 2 register-uri.

## Rezultat 2 — PCA

**Variance explicată**: PC1 = 5.7%, PC2 = 2.2%

Vezi `pca_scatter.png`. Dacă cele 2 grupuri se separă clar pe PC1-PC2, sunt registre stilometrice distincte.

## Rezultat 3 — Random Forest

**5-fold CV accuracy**: **92.1% ± 1.7%**

**Held-out 30% test confusion matrix**:
```
             pred_scris  pred_vorbit
true_scris          116           2
true_vorbit           9          89
```

Dacă un model simplu distinge FB de video cu >90% acuratețe **doar din 100 function words** (cuvinte ca: și, sau, în, la, dar, etc.), atunci cele 2 register-uri au amprente stilometrice distincte.

## Top 20 function words care discriminează FB vs video

Cuvinte unde frecvența diferă cel mai mult între cele 2 canale:

| Cuvânt | Importance | Mediu FB | Mediu video | Raport vorbit/scris |
|---|---:|---:|---:|---:|
| `acesta` | 0.1280 | 0.0042 | 0.0204 | 4.87× |
| `fi` | 0.0757 | 0.0463 | 0.0768 | 1.66× |
| `că` | 0.0694 | 0.0116 | 0.0354 | 3.06× |
| `deci` | 0.0539 | 0.0002 | 0.0055 | 25.71× |
| `și` | 0.0408 | 0.0911 | 0.0586 | 0.64× |
| `niște` | 0.0353 | 0.0000 | 0.0044 | 259.26× |
| `o` | 0.0326 | 0.0001 | 0.0047 | 55.62× |
| `al` | 0.0307 | 0.0372 | 0.0141 | 0.38× |
| `ăă` | 0.0282 | 0.0000 | 0.0041 | 41.06× |
| `crede` | 0.0281 | 0.0003 | 0.0044 | 14.27× |
| `nu` | 0.0267 | 0.0129 | 0.0265 | 2.05× |
| `într` | 0.0213 | 0.0000 | 0.0028 | 28.11× |
| `să` | 0.0197 | 0.0379 | 0.0568 | 1.50× |
| `pentru` | 0.0172 | 0.0394 | 0.0257 | 0.65× |
| `la` | 0.0168 | 0.0349 | 0.0230 | 0.66× |
| `spune` | 0.0147 | 0.0006 | 0.0038 | 6.84× |
| `ă` | 0.0147 | 0.0000 | 0.0022 | 22.14× |
| `care` | 0.0143 | 0.0346 | 0.0444 | 1.28× |
| `de` | 0.0138 | 0.1058 | 0.0745 | 0.70× |
| `sine` | 0.0129 | 0.0167 | 0.0125 | 0.75× |

## Interpretare

**Concluzie**: cele 2 registre sunt **moderat distincte stilometric** (78% accuracy).
Diferența e clară dar nu dramatică. Ar putea fi diferențe naturale gen scris vs vorbit.

## Limitări

- Folosim doar 100 function words; analize stilometrice profesionale folosesc 200-500.
- spaCy ro_core_news_sm are accuracy POS-tag moderată — pot fi erori sistematice.
- Nu avem **baseline politic comparativ** (Iohannis, etc.) — nu știm dacă pattern-ul observat e specific ND sau general.
- Random Forest tinde să exploateze și features non-stilometrice (lungime, repetiții) — accuracy poate fi inflated.