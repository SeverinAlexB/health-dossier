# Supplements Reference System

Two-tier system for supplement documentation:

- **`research/nutrients/`** — Nutrient-level science (dosing, safety, interactions, cofactors, evidence, forms, upper limits). Strictly one file per nutrient — no group or family files. General reference, not patient-specific.
- **`research/products/`** — Product cards (brand, price, ingredients panel, alternatives, community notes). One file per iHerb product. Links to its nutrient doc(s).

## Key Principles

- **No patient-specific data** in either location (no status, no patient doses, no protocol links)
- **Intervention files link here** — `dossier/3_interventions/` files should reference product cards for product details rather than duplicating them
- When recommending a new supplement, check if a product card already exists in `research/products/` and a nutrient doc exists in `research/nutrients/`

## Creating New Files / Updating Files

Use the `/supplement-facts` skill
