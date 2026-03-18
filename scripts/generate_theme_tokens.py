#!/usr/bin/env python3

"""Generate a starter semantic color palette for an iOS app."""

from __future__ import annotations

import argparse
import colorsys
import json
from pathlib import Path
from typing import Dict, Tuple

RGB = Tuple[int, int, int]

MOOD_PRESETS = {
    "trust": {"accent": "#2F6BFF", "neutral": "cool"},
    "calm": {"accent": "#0F9D8A", "neutral": "warm"},
    "energetic": {"accent": "#F97316", "neutral": "warm"},
    "premium": {"accent": "#0B6E4F", "neutral": "warm"},
    "playful": {"accent": "#E94E77", "neutral": "cool"},
    "minimal": {"accent": "#2563EB", "neutral": "cool"},
}

NEUTRAL_HUES = {
    "cool": 220.0,
    "warm": 35.0,
}


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def parse_hex(value: str) -> RGB:
    stripped = value.strip().lstrip("#")
    if len(stripped) != 6:
        raise ValueError(f"Expected a 6-digit hex color, got: {value}")
    return tuple(int(stripped[index:index + 2], 16) for index in (0, 2, 4))  # type: ignore[return-value]


def rgb_to_hex(rgb: RGB) -> str:
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def rgb_to_hsl(rgb: RGB) -> Tuple[float, float, float]:
    red, green, blue = (component / 255 for component in rgb)
    hue, lightness, saturation = colorsys.rgb_to_hls(red, green, blue)
    return hue * 360, saturation * 100, lightness * 100


def hsl_to_rgb(hue: float, saturation: float, lightness: float) -> RGB:
    red, green, blue = colorsys.hls_to_rgb(
        (hue % 360) / 360,
        clamp(lightness, 0, 100) / 100,
        clamp(saturation, 0, 100) / 100,
    )
    return (
        round(red * 255),
        round(green * 255),
        round(blue * 255),
    )


def hsl_to_hex(hue: float, saturation: float, lightness: float) -> str:
    return rgb_to_hex(hsl_to_rgb(hue, saturation, lightness))


def make_tokens(accent_hex: str, neutral_family: str) -> Dict[str, Dict[str, str]]:
    accent_hue, accent_saturation, accent_lightness = rgb_to_hsl(parse_hex(accent_hex))
    neutral_hue = NEUTRAL_HUES[neutral_family]
    neutral_sat = 10 if neutral_family == "cool" else 14

    light = {
        "background": hsl_to_hex(neutral_hue, neutral_sat, 98),
        "surface": hsl_to_hex(neutral_hue, neutral_sat, 95),
        "surfaceElevated": hsl_to_hex(neutral_hue, neutral_sat, 92),
        "textPrimary": hsl_to_hex(neutral_hue, neutral_sat + 4, 12),
        "textSecondary": hsl_to_hex(neutral_hue, neutral_sat + 2, 36),
        "border": hsl_to_hex(neutral_hue, neutral_sat, 84),
        "accent": hsl_to_hex(accent_hue, max(55, accent_saturation), clamp(accent_lightness, 42, 56)),
        "accentSoft": hsl_to_hex(accent_hue, max(28, accent_saturation - 28), 92),
        "success": hsl_to_hex(150, 58, 40),
        "warning": hsl_to_hex(35, 90, 50),
        "danger": hsl_to_hex(4, 72, 52),
    }

    dark = {
        "background": hsl_to_hex(neutral_hue, neutral_sat, 8),
        "surface": hsl_to_hex(neutral_hue, neutral_sat, 12),
        "surfaceElevated": hsl_to_hex(neutral_hue, neutral_sat, 16),
        "textPrimary": hsl_to_hex(neutral_hue, neutral_sat, 94),
        "textSecondary": hsl_to_hex(neutral_hue, neutral_sat, 72),
        "border": hsl_to_hex(neutral_hue, neutral_sat, 24),
        "accent": hsl_to_hex(accent_hue, max(58, accent_saturation), max(62, accent_lightness)),
        "accentSoft": hsl_to_hex(accent_hue, max(34, accent_saturation - 24), 24),
        "success": hsl_to_hex(150, 54, 62),
        "warning": hsl_to_hex(35, 90, 64),
        "danger": hsl_to_hex(4, 78, 66),
    }

    return {"light": light, "dark": dark}


def render_markdown(payload: Dict[str, object]) -> str:
    lines = [
        "# Theme Tokens",
        "",
        f"- mood: `{payload['mood']}`",
        f"- neutral: `{payload['neutral']}`",
        f"- accent: `{payload['accent']}`",
        "",
    ]
    tokens = payload["tokens"]
    assert isinstance(tokens, dict)
    for mode in ("light", "dark"):
        mode_tokens = tokens[mode]
        assert isinstance(mode_tokens, dict)
        lines.append(f"## {mode.capitalize()}")
        lines.append("")
        for name, value in mode_tokens.items():
            lines.append(f"- `{name}`: `{value}`")
        lines.append("")
    lines.append("Review these tokens on real screens in light mode, dark mode, and larger text sizes before locking the palette.")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate starter semantic color tokens for an iOS app.")
    parser.add_argument(
        "--mood",
        choices=sorted(MOOD_PRESETS.keys()),
        default="trust",
        help="Palette archetype to use when an explicit accent is not supplied.",
    )
    parser.add_argument(
        "--accent",
        help="Optional 6-digit hex brand accent. Overrides the preset accent for the selected mood.",
    )
    parser.add_argument(
        "--neutral",
        choices=sorted(NEUTRAL_HUES.keys()),
        help="Optional neutral family override.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format.",
    )
    parser.add_argument(
        "--output",
        help="Optional path to write the output. Prints to stdout when omitted.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    preset = MOOD_PRESETS[args.mood]
    accent = args.accent or preset["accent"]
    neutral = args.neutral or preset["neutral"]
    parse_hex(accent)
    tokens = make_tokens(accent, neutral)
    payload = {
        "mood": args.mood,
        "neutral": neutral,
        "accent": rgb_to_hex(parse_hex(accent)),
        "tokens": tokens,
    }

    if args.format == "json":
        rendered = json.dumps(payload, indent=2)
    else:
        rendered = render_markdown(payload)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
