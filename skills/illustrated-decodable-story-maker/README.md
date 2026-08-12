[![Omo](../../assets/logo.svg)](https://omo.space) · [All Omo Skills](../../README.md)

# Illustrated Decodable Story Maker

What this does: creates an original illustrated phonics story, editable source, thumbnail, and print-ready PDF from a bounded phonics and reading-level brief.

Omo price: **$0.30 per run**.

| Run it on Omo (one click, $0.30) | Run it yourself (you'll need these API keys + ~30 min setup) |
| --- | --- |
| Omo handles the hosted workflow, provider access, validation, image moderation, editable artifact/PDF delivery, and billing. | Bring an LLM_API_KEY, an approved IMAGE_PROVIDER_API_KEY, private object-storage credentials for artifacts, and a deterministic renderer. This folder contains the workflow contract, not a finished standalone renderer; ~30 minutes is enough to wire a local proof of concept, while production QA takes longer. |

Use original, reviewed content and approved image providers only. This workflow is instructional material, not a diagnostic or clinical assessment.

## Files

- [SKILL.md](./SKILL.md) — the full provider-agnostic workflow contract.
- [LICENSE](../../LICENSE) — MIT license for the single repository.
- [.gitignore](../../.gitignore) — repository-wide local-secret and generated-file exclusions.
