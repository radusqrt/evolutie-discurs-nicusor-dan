# Audit sentiment per entitate — false positive check

**Sample**: max 5 passages/bucket pentru entitățile TRUMP, PSD, SIMION, TĂRICEANU, ORBÁN.

**Întrebare LLM**: pentru fiecare passage, e despre entitate sau alt subject?

## Sumar

| Entitate | Perioadă | Total passages | Sampled | Kept | Rejected | FP rate |
|---|---|---:|---:|---:|---:|---:|
| PSD | 2025Q2 campanie + investitură | 15 | 5 | 5 | 0 | **0%** |
| PSD | 2025Q3 deficit + reforma economică | 3 | 3 | 3 | 0 | **0%** |
| PSD | 2025Q4 stabilizare + diplomație | 4 | 4 | 4 | 0 | **0%** |
| PSD | 2025Q4-2026Q1 reformă judiciară | 5 | 5 | 5 | 0 | **0%** |
| PSD | 2026Q2 cotitură UE + criză guvern | 11 | 5 | 5 | 0 | **0%** |
| SIMION | 2025Q2 campanie + investitură | 26 | 5 | 5 | 0 | **0%** |
| SIMION | 2025Q3 deficit + reforma economică | 4 | 4 | 4 | 0 | **0%** |
| TRUMP | 2025Q2 campanie + investitură | 6 | 5 | 5 | 0 | **0%** |
| TRUMP | 2025Q4-2026Q1 reformă judiciară | 7 | 5 | 5 | 0 | **0%** |

**Overall FP rate**: 0/41 (0%)

## Exemple false positives
