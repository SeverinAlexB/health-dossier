# Verify Your Work

Do not rely on your training data for verifiable claims. It is often inaccurate. Every verifiable claim needs a source — in chat answers as well as in files.

## What needs verification

Any claim of the form:
- "X causes / treats / is associated with Y" (clinical, mechanism, disease)
- "Dose Z is safe / effective / toxic"
- "Food F contains nutrient N at amount A"
- "Product P is sold at store S at price Q"
- "Supplement S interacts with medication M"

When unsure whether something counts, verify it. Bias toward verifying more, not less.

Exempt: readouts of the patient's own data (e.g., "your hair test showed aluminum at 12 µg/g") — but the patient file being cited must actually exist.

## How to verify

Check the claim against one of:
- **External sources** (per `.claude/rules/research-hierarchy.md`): PubMed, MDPI, iHerb, Migros, FoodData Central, Reddit
- **Internal sources**: patient files in `dossier/`, existing docs in `research/`

Then cite the source inline. In files, use the reference-style links from `.claude/rules/references.md`. In chat, an inline `(PMID 29914147)`, `(iHerb 18791)`, or file path is enough.

## Weak, mixed, or absent evidence

If PubMed/MDPI evidence is weak, mixed, or absent:
- State the uncertainty explicitly
- Name the best-available tier (mechanism, practitioner protocol, anecdotal report) and cite it
- Do not upgrade weak evidence into a confident claim

## In-session repeats

Once a claim is verified in a conversation, citing the same reference again without re-running the tool is fine.

## Verification fixes

Corrections made during verification (e.g., fixing a dose after a PubMed check) do not themselves trigger another round of verification.
