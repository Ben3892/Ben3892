"""Render README activity SVGs from a GitHub GraphQL contribution calendar."""

import argparse
import json
import math
from html import escape
from pathlib import Path


def render(days, username, dark):
    background, text, muted, grid, line, area = (
        ("#0d1117", "#e6edf3", "#8b949e", "#21262d", "#58a6ff", "#122c49")
        if dark
        else ("#ffffff", "#24292f", "#57606a", "#eaeef2", "#0969da", "#ddf4ff")
    )
    counts = [day["contributionCount"] for day in days]
    ceiling = max(4, math.ceil(max(counts) / 4) * 4)
    points = [
        (56 + index * 874 / max(1, len(days) - 1), 196 - count * 124 / ceiling)
        for index, count in enumerate(counts)
    ]
    title = f"{username}'s GitHub Activity"
    subtitle = (
        f"{sum(counts):,} contributions · {days[0]['date']} — {days[-1]['date']}"
    )
    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="960" height="260" '
        'viewBox="0 0 960 260" role="img" aria-labelledby="title description">',
        f'<title id="title">{escape(title)}</title>',
        f'<desc id="description">{escape(subtitle)}</desc>',
        f'<rect width="960" height="260" rx="12" fill="{background}"/>',
        '<g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif">',
        f'<text x="24" y="30" font-size="18" font-weight="600" '
        f'fill="{text}">{escape(title)}</text>',
        f'<text x="24" y="51" font-size="12" fill="{muted}">'
        f'{escape(subtitle)}</text>',
    ]
    for index in range(5):
        y = 196 - index * 31
        svg.extend([
            f'<path d="M56 {y}H930" stroke="{grid}" fill="none"/>',
            f'<text x="45" y="{y + 4}" text-anchor="end" font-size="11" '
            f'fill="{muted}">{ceiling * index // 4}</text>',
        ])
    coordinates = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    svg.extend([
        f'<polygon points="56,196 {coordinates} {points[-1][0]:.1f},196" '
        f'fill="{area}"/>',
        f'<polyline points="{coordinates}" fill="none" stroke="{line}" '
        'stroke-width="2.5" stroke-linejoin="round"/>',
    ])
    for index, ((x, y), day) in enumerate(zip(points, days)):
        svg.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{line}">'
            f'<title>{day["date"]}: {day["contributionCount"]} contributions</title>'
            '</circle>'
        )
        if index % 7 == 0 or index == len(days) - 1:
            svg.append(
                f'<text x="{x:.1f}" y="219" text-anchor="middle" '
                f'font-size="11" fill="{muted}">{day["date"][5:]}</text>'
            )
    svg.extend([
        f'<text x="24" y="245" font-size="11" fill="{muted}">'
        'Source: GitHub contribution calendar · Updated daily</text>',
        '</g></svg>\n',
    ])
    return "\n".join(svg)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--username", required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("assets"))
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    calendar = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    days = sorted(
        (day for week in calendar["weeks"] for day in week["contributionDays"]),
        key=lambda day: day["date"],
    )[-31:]
    if not days:
        raise ValueError("GitHub returned an empty contribution calendar")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for dark, filename in [(False, "github-activity.svg"), (True, "github-activity-dark.svg")]:
        (args.output_dir / filename).write_text(render(days, args.username, dark), encoding="utf-8")


if __name__ == "__main__":
    main()
