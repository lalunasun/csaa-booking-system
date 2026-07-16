# OpenAI Comment Summary Prompt Template

You are helping a coding school summarize teacher comments.

Extract the following information:

1. mastered skills
2. needs review
3. next step
4. parent-friendly summary

Return valid JSON only.

Teacher comment:

```text
Emma understands sensor input and worked well with her partner. She still needs more practice debugging robot movement.
```

Expected JSON shape:

```json
{
  "mastered": [],
  "needs_review": [],
  "next_step": "",
  "parent_summary": ""
}
```
