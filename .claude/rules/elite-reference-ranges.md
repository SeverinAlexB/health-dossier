# Elite Reference Ranges

Standard lab reference ranges are population-based — the 95% CI of "apparently
healthy" people, which includes the subclinically sick. "Normal" is not
"optimal." This patient is aiming for elite, not average.

## What counts as an elite range

An elite range is one derived from **peer-reviewed outcome studies** — PubMed
or MDPI research correlating biomarker values with hard outcomes (all-cause
mortality, disease incidence, longevity, performance).

Not elite:
- Practitioner opinion (Attia, Patrick, functional-medicine consensus) without
  an outcome study behind it
- Reddit/Twitter biohacker consensus
- "Feels better at" anecdotes

If the tightest available source is practitioner opinion, the marker does
**not** have an established elite range — treat it as missing (see below).

## When to flag the gap

Flag only when a value falls **between the standard range and the elite
target** — i.e., the lab calls it normal but outcome studies show worse
results at this level.

Example gap flag:

> Ferritin: 220 ng/mL. Lab range 30–400 ("normal"). NHANES (n=29,166,
> 18.8yr follow-up) shows Q4 ferritin carries HR 1.13 all-cause / 1.19
> CVD / 1.25 cancer mortality vs Q1 ([Iron Metabolic Biomarkers and the
> Mortality Risk in the General Population (PMID 38623382)][PMID38623382]).
> Above elite.
>
> [PMID38623382]: https://pubmed.ncbi.nlm.nih.gov/38623382/

Stay silent when:
- The value is already inside the elite range
- The value is clearly abnormal — standard clinical interpretation handles it
- No elite range is established for the marker

## When no elite range exists

Skip the marker. Do **not** infer a tight target from related biomarkers,
mechanism, or practitioner opinion. A fabricated-but-rigorous-looking target
is worse than no target.

## Citation

Every elite range cited requires a PMID or MDPI DOI in reference-style links
per `.claude/rules/references.md`. "Ferritin elite 70–150" without a citation
fails this rule.
