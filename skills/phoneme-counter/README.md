[![Omo](../../assets/logo.svg)](https://omo.space) · [All Omo Skills](../../README.md)

# Phoneme Counter

What this does: estimates the phoneme count and optional IPA transcription for one English word in a declared dialect, with uncertainty made explicit.

Omo price: **$0.30 per run**.

| Run it on Omo (one click, $0.30) | Run it yourself (you'll need these API keys + ~30 min setup) |
| --- | --- |
| Omo handles the hosted workflow, provider access, input validation, dialect checks, structured output, privacy boundary, and billing. | Bring an LLM_API_KEY (or compatible provider key), a small JSON validator, and the workflow contract in this folder. This is not a finished standalone service; ~30 minutes is enough to wire a local proof of concept, while production QA takes longer. |

Never equate letter count with phoneme count. Pronunciation and dialect can change the result, so review it before teaching.

## Files

- [SKILL.md](./SKILL.md) — the full provider-agnostic workflow contract.
- [LICENSE](../../LICENSE) — MIT license for the single repository.
- [.gitignore](../../.gitignore) — repository-wide local-secret and generated-file exclusions.
