#!/usr/bin/env python3
"""Render labeled sticker PNGs and a contact sheet from generated RGBA images.

Requires Pillow. The script does not remove backgrounds or redraw subjects; it
fails when an input is not an image with an actual alpha channel.
"""

from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError as exc:  # pragma: no cover - environment-dependent
    raise SystemExit("Pillow is required: install it in the active runtime.") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--labels-file", type=Path, required=True,
                        help="JSON object mapping input filename stem to exact label")
    parser.add_argument("--font", type=Path, default=None)
    parser.add_argument("--size", type=int, default=1024)
    parser.add_argument("--zip", action="store_true")
    return parser.parse_args()


def load_font(font_path: Path | None, size: int):
    if font_path:
        return ImageFont.truetype(str(font_path), size)
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def add_label(image: Image.Image, label: str, font, size: int) -> Image.Image:
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    image = image.convert("RGBA")
    image.thumbnail((int(size * 0.84), int(size * 0.84)), Image.Resampling.LANCZOS)
    canvas.alpha_composite(image, ((canvas.width - image.width) // 2, 0))
    draw = ImageDraw.Draw(canvas)
    box = draw.textbbox((0, 0), label, font=font, stroke_width=0)
    x = (canvas.width - (box[2] - box[0])) // 2
    y = canvas.height - (box[3] - box[1]) - max(24, int(size * 0.035))
    draw.text((x, y), label, font=font, fill=(20, 20, 20, 255),
              stroke_width=max(4, getattr(font, "size", 48) // 8),
              stroke_fill=(255, 255, 255, 255))
    return canvas


def main() -> int:
    args = parse_args()
    labels = json.loads(args.labels_file.read_text(encoding="utf-8"))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    font = load_font(args.font, max(36, int(args.size * 0.075)))
    outputs: list[Path] = []

    for source in sorted(args.input_dir.iterdir()):
        if source.suffix.lower() not in {".png", ".webp", ".jpg", ".jpeg"}:
            continue
        label = labels.get(source.stem)
        if label is None:
            raise SystemExit(f"Missing label for {source.name}")
        with Image.open(source) as source_image:
            if source_image.mode not in {"RGBA", "LA"}:
                raise SystemExit(f"{source.name} has no alpha channel; fix transparency first")
            rendered = add_label(source_image, str(label), font, args.size)
            target = args.output_dir / f"{source.stem}.png"
            rendered.save(target, "PNG", optimize=True)
            outputs.append(target)

    if not outputs:
        raise SystemExit("No supported input images found")

    columns = min(3, len(outputs))
    cell = args.size // columns
    rows = (len(outputs) + columns - 1) // columns
    sheet = Image.new("RGBA", (columns * cell, rows * cell), (248, 248, 248, 255))
    for index, output in enumerate(outputs):
        with Image.open(output) as image:
            preview = image.convert("RGBA")
            preview.thumbnail((cell, cell), Image.Resampling.LANCZOS)
            x = (index % columns) * cell + (cell - preview.width) // 2
            y = (index // columns) * cell + (cell - preview.height) // 2
            sheet.alpha_composite(preview, (x, y))
    sheet.save(args.output_dir.parent / f"preview-{args.output_dir.name}.png", "PNG")

    if args.zip:
        archive = args.output_dir.parent / f"{args.output_dir.name}.zip"
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
            for output in outputs:
                bundle.write(output, output.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
