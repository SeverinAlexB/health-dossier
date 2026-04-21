#!/usr/bin/env python3
"""Generate a single-page landscape A4 daily schedule PDF.

Usage: generate_schedule_pdf.py <json_config> <output_path>

The JSON config defines the schedule content. See SKILL.md for the schema.
"""

import json
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas

# ── Color palette ──────────────────────────────────────────────────────────
COLUMN_THEMES = [
    {"header": HexColor("#2B6CB0"), "bg": HexColor("#EBF4FA")},   # blue
    {"header": HexColor("#276749"), "bg": HexColor("#F0FFF4")},   # green
    {"header": HexColor("#9C4221"), "bg": HexColor("#FFFAF0")},   # orange
]
BANNER_COLOR = HexColor("#553C9A")
BANNER_BG = HexColor("#FAF5FF")
GRAY_BG = HexColor("#F7FAFC")
GRAY_BORDER = HexColor("#CBD5E0")
DARK = HexColor("#1A202C")
SUBTLE = HexColor("#718096")
WHITE = HexColor("#FFFFFF")

W, H = landscape(A4)
MARGIN = 12 * mm
COL_GAP = 6 * mm


def draw_rounded_rect(c, x, y, w, h, r, fill_color, stroke_color=None):
    c.saveState()
    c.setFillColor(fill_color)
    if stroke_color:
        c.setStrokeColor(stroke_color)
        c.setLineWidth(0.5)
        c.roundRect(x, y, w, h, r, stroke=1, fill=1)
    else:
        c.roundRect(x, y, w, h, r, stroke=0, fill=1)
    c.restoreState()


def draw_column(c, x, y_top, col_w, title, time_label, items, theme, font_size):
    """Draw one column section with header bar and bullet items."""
    section_h = y_top - 28 * mm
    draw_rounded_rect(c, x, 28 * mm, col_w, section_h, 3, theme["bg"])

    # Header bar
    header_h = 16
    header_y = y_top - header_h
    c.saveState()
    c.setFillColor(theme["header"])
    c.roundRect(x, header_y, col_w, header_h, 3, stroke=0, fill=1)
    c.restoreState()

    # Header text
    c.saveState()
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(x + 6, header_y + 4.5, title.upper())
    c.setFont("Helvetica", 7.5)
    c.drawRightString(x + col_w - 6, header_y + 4.5, time_label)
    c.restoreState()

    # Items
    c.saveState()
    c.setFillColor(DARK)
    line_h = font_size + 3.2
    iy = header_y - 12
    for i, item in enumerate(items):
        if i % 2 == 0:
            c.saveState()
            c.setFillColor(WHITE)
            c.rect(x + 2, iy - 2, col_w - 4, line_h, stroke=0, fill=1)
            c.restoreState()
            c.setFillColor(DARK)
        c.setFont("Helvetica", 5)
        c.drawString(x + 7, iy + 1.5, "\u25CF")
        c.setFont("Helvetica", font_size)
        c.drawString(x + 15, iy, item)
        iy -= line_h
    c.restoreState()
    return iy


def generate_pdf(config, output_path):
    c = canvas.Canvas(output_path, pagesize=landscape(A4))
    c.setTitle(config["title"])

    top = H - 10 * mm

    # ── Title ──────────────────────────────────────────────────────────────
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(DARK)
    c.drawString(MARGIN, top, config["title"])

    if config.get("subtitle"):
        c.setFont("Helvetica", 8)
        c.setFillColor(SUBTLE)
        c.drawString(MARGIN, top - 13, config["subtitle"])

    # Separator line
    c.setStrokeColor(GRAY_BORDER)
    c.setLineWidth(0.5)
    c.line(MARGIN, top - 18, W - MARGIN, top - 18)

    # ── Optional banner ────────────────────────────────────────────────────
    content_top = top - 23
    banner = config.get("banner")
    if banner:
        banner_y = top - 34
        banner_h = 13
        draw_rounded_rect(c, MARGIN, banner_y, W - 2 * MARGIN, banner_h, 3, BANNER_BG, BANNER_COLOR)
        c.setFont("Helvetica-Bold", 7.5)
        c.setFillColor(BANNER_COLOR)
        c.drawString(MARGIN + 6, banner_y + 3.5, banner["label"])
        c.setFont("Helvetica", 7.5)
        c.drawString(MARGIN + 195, banner_y + 3.5, banner["text"])
        content_top = banner_y - 5

    # ── Columns ────────────────────────────────────────────────────────────
    sections = config["sections"]
    num_cols = len(sections)
    col_w = (W - 2 * MARGIN - (num_cols - 1) * COL_GAP) / num_cols

    # Auto-size font: scale down if the longest column has many items
    max_items = max(len(s["items"]) for s in sections)
    if max_items > 18:
        font_size = 7.0
    elif max_items > 14:
        font_size = 7.5
    else:
        font_size = 8.0

    for i, section in enumerate(sections):
        x = MARGIN + i * (col_w + COL_GAP)
        theme = COLUMN_THEMES[i % len(COLUMN_THEMES)]
        draw_column(c, x, content_top, col_w, section["title"],
                    section.get("time", ""), section["items"], theme, font_size)

    # ── Gap labels between columns ─────────────────────────────────────────
    gap_labels = config.get("gap_labels", [])
    gap_y = content_top - 105
    c.setFont("Helvetica-Bold", 6)
    c.setFillColor(SUBTLE)
    for i, label in enumerate(gap_labels):
        if i >= num_cols - 1:
            break
        gx = MARGIN + (i + 1) * col_w + i * COL_GAP
        c.saveState()
        c.translate(gx + COL_GAP / 2, gap_y)
        c.rotate(90)
        c.drawCentredString(0, 0, label)
        c.restoreState()

    # ── Key rules footer ───────────────────────────────────────────────────
    rules = config.get("rules", [])
    if rules:
        rules_y = 8 * mm
        rules_h = 18 * mm
        draw_rounded_rect(c, MARGIN, rules_y, W - 2 * MARGIN, rules_h, 3, GRAY_BG, GRAY_BORDER)

        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(DARK)
        c.drawString(MARGIN + 6, rules_y + rules_h - 10, config.get("rules_title", "KEY RULES"))

        c.setFont("Helvetica", 7.2)
        rx = MARGIN + 6
        ry = rules_y + rules_h - 22
        half = (len(rules) + 1) // 2
        for i, rule in enumerate(rules):
            if i < half:
                c.drawString(rx, ry - i * 10, f"{i+1}.  {rule}")
            else:
                c.drawString(rx + (W - 2 * MARGIN) / 2, ry - (i - half) * 10, f"{i+1}.  {rule}")

    c.save()
    print(f"PDF saved to: {output_path}")


def main():
    if len(sys.argv) != 3:
        print("Usage: generate_schedule_pdf.py <json_config> <output_path>", file=sys.stderr)
        sys.exit(1)
    with open(sys.argv[1]) as f:
        config = json.load(f)
    generate_pdf(config, sys.argv[2])


if __name__ == "__main__":
    main()
