---
name: daily-schedule-pdf
description: Generate a single-page landscape A4 PDF reference card for daily schedules. Use when the user asks to create a printable daily schedule, routine card, supplement schedule PDF, or any time-based daily plan as a PDF. Triggers include "create a PDF schedule", "printable daily routine", "PDF reference card", "daily schedule PDF".
---

# Daily Schedule PDF

Generate single-page landscape A4 PDFs for daily schedules using `scripts/generate_schedule_pdf.py`.

## Layout

- **Header**: Title + subtitle, horizontal rule
- **Banner** (optional): Full-width purple bar for a pre-section note
- **3 columns**: Color-coded sections (blue, green, orange) with header bar + bullet items
- **Gap labels** (optional): Vertical text between columns
- **Rules footer** (optional): Gray bar at bottom with numbered rules in 2-column layout

## Workflow

1. Gather schedule content from user or source file
2. Write a JSON config to `/tmp/schedule_config.json`
3. Ensure reportlab venv: `python3 -m venv /tmp/pdf_venv && /tmp/pdf_venv/bin/pip install reportlab`
4. Run: `/tmp/pdf_venv/bin/python3 <skill_dir>/scripts/generate_schedule_pdf.py /tmp/schedule_config.json <output_path>`

## JSON Config Schema

```json
{
  "title": "Daily Supplement Schedule",
  "subtitle": "Protocol X | Updated 2026-04-02",
  "banner": {
    "label": "PRE-BREAKFAST (~7:30am):",
    "text": "Biofilm Defense 1 cap → wait 30 min"
  },
  "sections": [
    {
      "title": "Breakfast",
      "time": "~8:00am",
      "items": ["Item 1", "Item 2"]
    },
    {
      "title": "Lunch",
      "time": "~12:30pm",
      "items": ["Item 1"]
    },
    {
      "title": "Dinner",
      "time": "~6:00pm",
      "items": ["Item 1"]
    }
  ],
  "gap_labels": ["5–6h GAP", "5–6h GAP"],
  "rules": ["Rule one", "Rule two"],
  "rules_title": "KEY RULES"
}
```

- `banner`, `gap_labels`, `rules`, `rules_title` are optional
- `sections` supports 2-3 columns (3 recommended)
- Font auto-scales based on longest column: 8pt (≤14 items), 7.5pt (15-18), 7pt (19+)
- Keep items concise — long text overflows column width
