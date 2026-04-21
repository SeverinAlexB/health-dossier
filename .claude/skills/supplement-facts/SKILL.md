---
name: supplement-facts
description: Create nutrient reference docs and product cards for supplements. Nutrients go to research/nutrients/ (dosing, safety, interactions, evidence). Products go to research/products/ (brand, price, ingredients, alternatives). Use when adding a new supplement, looking up product details, researching nutrient safety/interactions, or when recommending a supplement. Triggers include "create a supplement fact file", "add this supplement", "look up this product", "what are the interactions for X", or any time a new supplement is being introduced. Input can be an iHerb product ID, product name, or ingredient search query.
---

# Supplement Facts Creator

Two-file system: **nutrient docs** (science) in `research/nutrients/` and **product cards** (brand/price) in `research/products/`.

No patient-specific data in either file type. The patient's relationship to supplements lives in `patient_file/3_interventions/`.

## Input

One of:
- iHerb product ID (e.g., `692` or `#692`)
- Product name (e.g., `NOW Foods Magnesium Malate`)
- Ingredient query (e.g., `magnesium glycinate`)

## Workflow

### Phase 1: Identify the Product

**If iHerb ID given** → proceed to Phase 2.

**If search query** → find the product:
```
iherb-cli search "<query>" --limit 5 --sort best-selling --country ch --currency CHF
```
Present options to user and confirm which product before proceeding.

### Phase 2: Check for Existing Nutrient Doc

Check if `research/nutrients/<nutrient>.md` exists.
- Nutrient naming: all lowercase, hyphens. E.g., `magnesium.md`, `vitamin-c.md`, `oregano-oil.md`
- Multi-ingredient products (e.g., D3+K2): check EACH nutrient separately (`vitamin-d.md`, `vitamin-k2.md`)

**If nutrient doc exists** → skip to Phase 4 (product card only).
**If not** → proceed to Phase 3.

### Phase 3: Create Nutrient Doc

Gather PubMed data:
```
pubmed-cli search "<ingredient> safety tolerable upper limit" --human-only --reviews-only --limit 5
pubmed-cli search "<ingredient> bioavailability <form>" --human-only --limit 5
pubmed-cli search "<ingredient> drug interaction" --human-only --reviews-only --limit 3
```

Write file following [references/nutrient-template.md](references/nutrient-template.md):
- Save as `research/nutrients/<nutrient>.md`
- Include Forms section if multiple supplemental forms exist
- Update `research/nutrients/_index.md`

### Phase 4: Create Product Card

Gather iHerb + community data:
```
iherb-cli product <id> --section overview --country ch --currency CHF
iherb-cli product <id> --section ingredients
iherb-cli product <id> --section nutrition
iherb-cli product <id> --section reviews
reddit-cli search "<supplement name> experience side effects" --limit 5
iherb-cli search "<ingredient>" --limit 5 --sort best-selling --country ch --currency CHF
```

Write file following [references/product-template.md](references/product-template.md):
- Save as `products/<brand-kebab>-<product-kebab>.md`
- Link to nutrient doc(s) in frontmatter and header
- Pick 1-2 alternatives from **different brands**
- For minerals: calculate **elemental weight** and **cost per unit of active ingredient**
- Update `products/_index.md`

### Phase 5: Verify

1. **Word count**: `wc -w <file>` — both files must be under 3000 words
2. **PMID check**: Spot-check at least 1 PMID via `pubmed-cli article <pmid> --section abstract`
3. **Cross-link**: Product card must link to nutrient doc; nutrient doc must exist
4. **Elemental weight** (minerals only): Confirm compound vs elemental distinction

## Section Requirements

### Nutrient Doc (`research/nutrients/`)

| Section | Required? | Notes |
|---------|-----------|-------|
| Dosing Guidelines | Yes | RDA, UL, therapeutic range. PMIDs required |
| Safety Profile | Yes | Toxicity, side effects, contraindications. PMIDs required |
| Interactions | Yes | Supplement-supplement, supplement-drug, supplement-food |
| Cofactors | Yes | Required cofactors and common sources |
| Evidence Summary | Yes | Mechanism + 2-4 key PMIDs |
| Forms | Optional | Only when multiple supplemental forms exist |

### Product Card (`research/products/`)

| Section | Required? | Notes |
|---------|-----------|-------|
| Product Overview | Yes | Include cost/serving AND cost per active ingredient unit |
| Active Ingredients | Yes | Minerals MUST show elemental vs compound weight |
| Supplement Facts | Yes | Full panel from iHerb including "Other Ingredients" |
| Form Note | Optional | Brief note + link to nutrient doc Forms section |
| Alternatives | Yes | 1-2 products from different brands with iHerb IDs |
| Community Notes | Optional | Only if Reddit/iHerb reviews yield meaningful insights |

## Rules

- **Strictly one nutrient per file** — no group or family files (e.g., no `b-vitamins.md`). Each nutrient gets its own file: `thiamine.md`, `riboflavin.md`, `niacin.md`, etc. Multi-ingredient products (e.g., a B-complex) link to each individual nutrient file separately.
- Every iHerb reference: `(iHerb #12345)` inline format
- All clinical claims (dosing, safety, toxicity) require PMID references
- No patient-specific data — these are reference docs
- Max file size: 3000 words per file
- Prices in CHF (`--country ch --currency CHF`)
