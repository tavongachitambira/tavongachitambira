"""Render the GitHub contribution card (teal/sand) as a self-contained SVG."""
import json, os, sys, urllib.request
from datetime import date

USER = os.environ.get("GH_USER", "tavongachitambira")
OUT = sys.argv[1] if len(sys.argv) > 1 else "dist/contribution-card.svg"
SRC = sys.argv[2] if len(sys.argv) > 2 else None  # optional local json (testing)

LEVELS = ["#2b6660", "#6f908b", "#a3b9b5", "#d0ddd9", "#F0EDE4"]
CELL, GAP = 11, 3
W, PAD = 900, 28
SANS = "Segoe UI,Helvetica,Arial,sans-serif"
MONO = "Consolas,Menlo,monospace"


def load():
    if SRC:
        return json.load(open(SRC))
    url = f"https://github-contributions-api.jogruber.de/v4/{USER}?y=last"
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)


def main():
    data = load()
    days = data["contributions"]
    total = sum(d["count"] for d in days)

    # Pad the first week so rows line up with weekdays (Sun=0).
    first = date.fromisoformat(days[0]["date"])
    lead = (first.weekday() + 1) % 7
    cells = [None] * lead + days
    weeks = [cells[i : i + 7] for i in range(0, len(cells), 7)]

    grid_w = len(weeks) * (CELL + GAP) - GAP
    grid_h = 7 * (CELL + GAP) - GAP
    panel_x, panel_y = PAD, 152
    panel_w = W - 2 * PAD
    panel_h = grid_h + 40
    gx = panel_x + (panel_w - grid_w) / 2
    gy = panel_y + 20
    H = panel_y + panel_h + 56

    rects = []
    for wi, week in enumerate(weeks):
        for di, d in enumerate(week):
            if d is None:
                continue
            x = gx + wi * (CELL + GAP)
            y = gy + di * (CELL + GAP)
            lvl = max(0, min(4, int(d["level"])))
            rects.append(
                f'<rect x="{x:.1f}" y="{y}" width="{CELL}" height="{CELL}" rx="3" fill="{LEVELS[lvl]}"><title>{d["count"]} contributions on {d["date"]}</title></rect>'
            )

    legend_y = H - 28
    lx = W - PAD - 150
    legend = f'<text x="{lx}" y="{legend_y + 9}" font-family="{SANS}" font-size="12" fill="#F0EDE4" opacity=".7">Less</text>'
    for i, c in enumerate(LEVELS):
        legend += f'<rect x="{lx + 38 + i * 16}" y="{legend_y}" width="11" height="11" rx="3" fill="{c}"/>'
    legend += f'<text x="{lx + 38 + 5 * 16 + 4}" y="{legend_y + 9}" font-family="{SANS}" font-size="12" fill="#F0EDE4" opacity=".7">More</text>'

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#005a52"/><stop offset="1" stop-color="#004741"/></linearGradient></defs>
<rect width="{W}" height="{H}" rx="22" fill="url(#bg)"/>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="21" stroke="#7FD1C7" stroke-opacity=".2"/>
<circle cx="{PAD+18}" cy="{PAD+18}" r="18" fill="#003a35"/>
<path transform="translate({PAD+6} {PAD+6}) scale(1.5)" fill="#F0EDE4" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
<text x="{PAD+48}" y="{PAD+24}" font-family="{MONO}" font-size="16" font-weight="700" fill="#F0EDE4">GitHub</text>
<text x="{PAD}" y="{PAD+82}" font-family="{SANS}" font-size="44" font-weight="700" fill="#F0EDE4">{total}</text>
<text x="{PAD}" y="{PAD+104}" font-family="{MONO}" font-size="12" letter-spacing="1.5" fill="#F0EDE4" opacity=".7">CONTRIBUTIONS IN THE LAST YEAR</text>
<rect x="{panel_x}" y="{panel_y}" width="{panel_w}" height="{panel_h}" rx="16" fill="#003a35"/>
{chr(10).join(rects)}
{legend}
</svg>
'''
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    open(OUT, "w").write(svg)
    print(f"wrote {OUT} ({total} contributions)")


main()
