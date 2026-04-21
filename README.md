# health-bot-template

A template for keeping a personal health record that an AI assistant (Claude Code) can read, reason over, and update like a careful clinician would.

Fork it, drop in your own diagnostic data, and use Claude Code as a systems-level health collaborator that cites sources, checks interactions, and keeps your record clean over time.

## What this is (and isn't)

- **Is**: a structured folder layout + a set of `.claude/` rules, skills, and CLI integrations that turn a plain git repo into a usable personal health record.
- **Isn't**: medical advice, a diagnostic tool, or a replacement for a clinician. See [Disclaimer](#disclaimer).

## Repository Structure

```
health-bot-template/
├── patient_file/       # The clinical record — your data, assessments, protocols, tracking
│   ├── 1_data/         # Raw inputs: blood tests, genetics, microbiome, wearables, profile
│   ├── 2_assessments/  # Interpretation of YOUR data ("what does this mean for me?")
│   ├── 3_interventions/# Active, past, and proposed protocols
│   ├── 4_monitoring/   # Daily metrics, symptom tracking, outcomes
│   └── archive/        # Superseded files, kept for history
│
├── research/           # General evidence reviews, not patient-specific
│   ├── nutrients/      # One file per nutrient: dosing, safety, interactions, evidence
│   └── products/       # One file per iHerb product: brand, price, panel, alternatives
│
└── .claude/            # AI assistant configuration (see below)
```

### Data flow

```
1_data → 2_assessments → 3_interventions → 4_monitoring → [iterate]
              ↑
          research/     (general science, shared across patients)
```

## The `.claude/` system

This is what makes the repo more than a folder of markdown.

### Rules (`.claude/rules/`)

Standing instructions the assistant follows on every task:

- **`verify.md`** — every verifiable claim needs a source; no training-data guessing
- **`research-hierarchy.md`** — PubMed > practitioner protocols > anecdotal reports
- **`references.md`** — citation format for PMIDs, iHerb SKUs, FDC IDs, Migros IDs, Reddit threads
- **`read-before-write.md`** — answer questions without editing files unless asked
- **`supplements.md`** / **`supplement-facts.md`** — safety, cofactors, two-tier nutrient/product docs
- **`iherb.md`** / **`migros.md`** / **`fooddata.md`** — preferred supplement/grocery sources
- **`no-prescription-meds.md`** — prefer OTC; flag prescriptions but don't lean on them
- **`monitoring.md`** — when and how to track outcomes
- **`archiving.md`** — how to retire superseded protocols
- **`research.md`** — when to write to `research/` vs `patient_file/2_assessments/`
- **`long_lived_docs.md`** / **`file_size.md`** — write for the next session, split files > 3000 words

### Skills (`.claude/skills/`)

- **`supplement-facts`** — generate nutrient reference docs and product cards in the expected two-tier format
- **`daily-schedule-pdf`** — render a daily supplement/routine schedule as a printable A4 landscape card

### External data integrations

The assistant uses command-line tools (configured separately) to pull live data instead of hallucinating it:

- **PubMed** — literature search and citation
- **iHerb** — supplement availability, pricing, formulation
- **Migros** — Swiss grocery availability and pricing
- **FoodData Central (USDA)** — nutrient profiles for foods
- **Reddit / Twitter** — practitioner protocols and experience reports

## Using this template

### 1. Fork or clone the repo

Get your own copy — this repo is meant to be forked, not contributed back to.

### 2. Replace the example data

`patient_file/1_data/` ships with example files (marked `> Example data.` at the
top) so you can see what each file type looks like. **These are not your data.**
Before you rely on anything the assistant writes, delete or overwrite them.

Start with `patient_profile.md` — it's the entry point the assistant reads
first. Fill in demographics, medical history, current medications, and
allergies. The rest of the folder can be populated as you go.

Typical things that live in `1_data/`:

- **Blood tests** — one file per draw, named by date (`blood_test_YYYYMM.md`)
- **Hair / stool / urine / microbiome tests** — one file per test
- **Genetic data** — raw exports plus any screening analyses

### 3. Convert your PDFs to markdown

Lab reports, genetic test results, and clinic summaries almost always arrive as
PDFs. The patient record works best when every data source is plain markdown —
it keeps files diffable, greppable, and cheap for the assistant to read.

The easiest way to convert them:

1. Drop the PDF into `patient_file/1_data/` (or a temporary folder).
2. Ask Claude Code — or any AI that can read PDFs (Claude.ai, ChatGPT, Gemini)
   — to transcribe it into markdown, using the existing example files as the
   format reference.
3. Review the output, fix any OCR mistakes, save as `.md`, and delete the PDF
   if you don't need it in the repo.

### 4. Start using it

Open the repo in Claude Code and start asking questions: *"what does my latest
blood test suggest?"*, *"what's missing from my supplement stack given these
results?"*, *"write an assessment of my microbiome report."* Review what it
writes. Correct it when it's wrong — the corrections stick, because the record
is the source of truth.

### 5. Let the record grow

Treat the repo as a long-lived clinical file, not a scratchpad. New test? Add
it to `1_data/`. New protocol? `3_interventions/`. Daily tracking? `4_monitoring/`.
The `.claude/` rules will keep the assistant citing sources, archiving
superseded files, and writing things that make sense in the next session.

## Disclaimer

This system is for educational and personal optimization purposes only. It is **not medical advice** and should not replace consultation with qualified healthcare professionals. All health interventions should be discussed with and supervised by appropriate medical practitioners.
