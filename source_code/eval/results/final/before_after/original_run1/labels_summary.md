# Manually labelled results

Labels: **correct** (accurate, nothing misleading added) · **incomplete** (accurate but key parts missing) · **ambiguous** (contradicts itself, or reproduces garbled/contradictory source text) · **incorrect** (wrong key fact, invented detail, refusing an answerable question, or answering an off-topic one).

## Per model (27 questions: 23 answerable + 4 that should be refused)

| Model | Correct | Incomplete | Ambiguous | Incorrect | Answerable correct | Refused when it should | Mean latency (s) |
|---|---|---|---|---|---|---|---|
| qwen3.5:0.8b | 15 | 2 | 3 | 7 | 14/23 | 1/4 | 9.4 |

Mean latency is over answerable questions only (refusals by the relevance gate take ~1 s). Latency was measured against a shared remote GPU server and is indicative only.

## Per question

| Question | qwen3.5:0.8b |
|---|---|
| Q01 program requirements | incorrect |
| Q02 program requirements | incomplete |
| Q03 academic policies | correct |
| Q04 program requirements | correct |
| Q05 academic policies | correct |
| Q06 academic policies | correct |
| Q07 academic policies | incorrect |
| Q08 course offerings | ambiguous |
| Q09 course offerings | correct |
| Q10 course offerings | incorrect |
| Q11 course offerings | correct |
| Q12 course offerings | correct |
| Q13 course offerings | correct |
| Q14 course offerings | correct |
| Q15 learning outcomes | correct |
| Q16 learning outcomes | correct |
| Q17 career | correct |
| Q18 teaching assessment | incomplete |
| Q19 program requirements | correct |
| Q20 ambiguous | ambiguous |
| Q21 out of scope | correct |
| Q22 other | incorrect |
| Q23 out of scope | incorrect |
| Q24 out of scope | incorrect |
| Q25 follow up | correct |
| Q26 follow up | ambiguous |
| Q27 follow up out of scope | incorrect |
