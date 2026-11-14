# Manually labelled results

Labels: **correct** (accurate, nothing misleading added) · **incomplete** (accurate but key parts missing) · **ambiguous** (contradicts itself, or reproduces garbled/contradictory source text) · **incorrect** (wrong key fact, invented detail, refusing an answerable question, or answering an off-topic one).

## Per model (27 questions: 23 answerable + 4 that should be refused)

| Model | Correct | Incomplete | Ambiguous | Incorrect | Answerable correct | Refused when it should | Mean latency (s) |
|---|---|---|---|---|---|---|---|
| qwen3.5:0.8b | 16 | 1 | 3 | 7 | 12/23 | 4/4 | 9.6 |
| qwen2.5:0.5b-instruct (Q8_0) | 12 | 4 | 2 | 9 | 10/23 | 2/4 | 6.6 |
| llama3.2:3b | 22 | 1 | 2 | 2 | 18/23 | 4/4 | 9.4 |
| qwen2.5:3b | 20 | 0 | 2 | 5 | 16/23 | 4/4 | 7.3 |
| gemma3:4b | 23 | 0 | 2 | 2 | 19/23 | 4/4 | 11.3 |
| qwen3.5:9b | 24 | 0 | 1 | 2 | 20/23 | 4/4 | 17.8 |

Mean latency is over answerable questions only (refusals by the relevance gate take ~1 s). Latency was measured against a shared remote GPU server and is indicative only.

## Per question

| Question | qwen3.5:0.8b | qwen2.5:0.5b-instruct (Q8_0) | llama3.2:3b | qwen2.5:3b | gemma3:4b | qwen3.5:9b |
|---|---|---|---|---|---|---|
| Q01 program requirements | incorrect | correct | correct | correct | correct | correct |
| Q02 program requirements | incorrect | incorrect | incomplete | incorrect | correct | correct |
| Q03 academic policies | incorrect | correct | correct | incorrect | correct | correct |
| Q04 program requirements | correct | incorrect | correct | correct | correct | correct |
| Q05 academic policies | ambiguous | correct | correct | correct | correct | correct |
| Q06 academic policies | correct | correct | correct | correct | correct | correct |
| Q07 academic policies | incorrect | incorrect | incorrect | incorrect | incorrect | incorrect |
| Q08 course offerings | ambiguous | incomplete | correct | correct | correct | correct |
| Q09 course offerings | correct | correct | correct | correct | correct | correct |
| Q10 course offerings | incorrect | ambiguous | ambiguous | correct | ambiguous | correct |
| Q11 course offerings | correct | correct | correct | correct | correct | correct |
| Q12 course offerings | incomplete | incomplete | correct | correct | correct | correct |
| Q13 course offerings | correct | incorrect | correct | correct | correct | correct |
| Q14 course offerings | correct | correct | correct | correct | correct | correct |
| Q15 learning outcomes | correct | correct | correct | correct | correct | correct |
| Q16 learning outcomes | incorrect | incomplete | correct | correct | correct | correct |
| Q17 career | correct | correct | correct | ambiguous | correct | correct |
| Q18 teaching assessment | correct | incomplete | correct | correct | correct | correct |
| Q19 program requirements | correct | incorrect | correct | correct | correct | correct |
| Q20 ambiguous | ambiguous | ambiguous | ambiguous | ambiguous | ambiguous | ambiguous |
| Q21 out of scope | correct | incorrect | correct | correct | correct | correct |
| Q22 other | incorrect | incorrect | incorrect | incorrect | incorrect | incorrect |
| Q23 off topic | correct | correct | correct | correct | correct | correct |
| Q24 off topic | correct | correct | correct | correct | correct | correct |
| Q25 follow up | correct | correct | correct | correct | correct | correct |
| Q26 follow up | correct | incorrect | correct | incorrect | correct | correct |
| Q27 follow up off topic | correct | incorrect | correct | correct | correct | correct |
