[![Omo](../../assets/logo.svg)](https://omo.space) · [All Omo Skills](../../README.md)

# Decodable Sentence Creator

What this does: generates a small set of child-safe practice sentences constrained by selected phonics patterns, length, dialect, and sight-word policy.

Omo price: **$0.30 per run**.

| Run it on Omo (one click, $0.30) | Run it yourself (you'll need these API keys + ~30 min setup) |
| --- | --- |
| Omo handles the hosted workflow, provider access, validation, child-safety checks, structured output, privacy boundary, and billing. | Bring an LLM_API_KEY (or compatible provider key), a small JSON validator, and the workflow contract in this folder. This is not a finished standalone service; ~30 minutes is enough to wire a local proof of concept, while production QA takes longer. |

This is teacher-reviewable instructional material, not a diagnostic or clinical assessment. Review sentence decodability and dialect before classroom use.

## Files

- [SKILL.md](./SKILL.md) — the full provider-agnostic workflow contract.
- [LICENSE](../../LICENSE) — MIT license for the single repository.
- [.gitignore](../../.gitignore) — repository-wide local-secret and generated-file exclusions.
