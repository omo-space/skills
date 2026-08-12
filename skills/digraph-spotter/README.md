[![Omo](../../assets/logo.svg)](https://omo.space) · [All Omo Skills](../../README.md)

# Digraph Spotter

What this does: identifies reviewed consonant and vowel digraphs in bounded English text and returns exact spans plus cautious explanations.

Omo price: **$0.30 per run**.

| Run it on Omo (one click, $0.30) | Run it yourself (you'll need these API keys + ~30 min setup) |
| --- | --- |
| Omo handles the hosted workflow, provider access, input validation, exact-span checks, structured output, privacy boundary, and billing. | Bring an LLM_API_KEY (or compatible provider key), a small JSON validator, and the workflow contract in this folder. This is not a finished standalone service; ~30 minutes is enough to wire a local proof of concept, while production QA takes longer. |

The result describes spelling patterns and evidence; it does not guarantee pronunciation in every word or dialect. Review outputs before classroom use.

## Files

- [SKILL.md](./SKILL.md) — the full provider-agnostic workflow contract.
- [LICENSE](../../LICENSE) — MIT license for the single repository.
- [.gitignore](../../.gitignore) — repository-wide local-secret and generated-file exclusions.
