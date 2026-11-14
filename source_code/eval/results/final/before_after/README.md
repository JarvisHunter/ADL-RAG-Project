# Before / after the strict-mode fixes (qwen3.5:0.8b)

Same 27 questions, same model, two runs per pipeline, every answer labelled by hand
(`label` and `notes` columns in `results.csv`).

| Folder | Pipeline | Answerable correct | Correct refusals |
|---|---|---|---|
| `original_run1/` | before the fixes (threshold 0.3, no rule reminder, no refusal gate) | 14/23 | 1/4 |
| `original_run2/` | before the fixes | 14/23 | 1/4 |
| `../` (main run, qwen3.5:0.8b rows) | after the fixes | 12/23 | 4/4 |
| `fixed_run2/` | after the fixes | 13/23 | 4/4 |

The "original" runs used `rag/pipeline.py` and `rag/prompts.py` from commit `d25f652` with
`RAG_SCORE_THRESHOLD=0.3`. See Section 6 of the report.
