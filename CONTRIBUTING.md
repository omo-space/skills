# Contributing to Omo Skills

Thank you for helping improve the library. Omo Skills are provider-agnostic
workflow contracts: contributions should make a workflow clearer, safer, more
useful, or easier to run independently.

## Changes to a skill

- Keep `SKILL.md` self-contained and explicit about inputs, validation,
  uncertainty, privacy, and outputs.
- Preserve the skill's provider-agnostic contract. Provider-specific setup
  belongs in the self-hosting notes, not in the core behavior unless the skill
  requires it.
- Use original, reviewable examples. Do not copy proprietary curriculum,
  copyrighted characters, or private data.
- Keep the skill's folder `README.md` in the two-door format: run it on Omo or
  run the contract yourself.
- Update the root index and `CHANGELOG.md` when adding a skill.

## Before opening a change

Check that every skill folder contains both `SKILL.md` and `README.md`, that
links resolve within the repository, and that examples do not overclaim
diagnostic, clinical, curriculum-alignment, or pronunciation certainty.

Please open focused pull requests with a clear description of the workflow
behavior changed and the checks you performed. By participating, you agree to
follow the [Code of Conduct](CODE_OF_CONDUCT.md).
