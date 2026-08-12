[![Omo](../../assets/logo.svg)](https://omo.space) · [All Omo Skills](../../README.md)

# Story Idea Generator

What this does: generates a bounded set of original, child-safe story ideas from optional genre, character-count, and setting constraints.

Omo price: **$0.30 per run**.

| Run it on Omo (one click, $0.30) | Run it yourself (you'll need these API keys + ~30 min setup) |
| --- | --- |
| Omo handles the hosted workflow, provider access, safety checks, constraint validation, structured output, privacy boundary, and billing. | Bring an LLM_API_KEY (or compatible provider key), a small JSON validator, and the workflow contract in this folder. This is not a finished standalone service; ~30 minutes is enough to wire a local proof of concept, while production QA takes longer. |

Ideas are original prompts for student writing or teacher planning. Review age-appropriateness and avoid copyrighted characters, franchises, or close plot imitation.

## Files

- [SKILL.md](./SKILL.md) — the full provider-agnostic workflow contract.
- [LICENSE](../../LICENSE) — MIT license for the single repository.
- [.gitignore](../../.gitignore) — repository-wide local-secret and generated-file exclusions.
