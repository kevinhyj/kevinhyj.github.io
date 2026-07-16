from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PHOTO_ROOTS = (
    ROOT / "assets/posts",
    ROOT / "assets/cat",
    ROOT / "assets/shared/portraits",
)
CARD_IMAGES = (
    ROOT / "assets/works/eva/cover.png",
    ROOT / "assets/works/phaseflow/cover.png",
    ROOT / "assets/works/proteo-r1-r2/cover-card.png",
    ROOT / "assets/works/proteocraft/method-overview-cover.png",
    ROOT / "assets/works/rillie/rillie-fluorescent-aptamer-cover.png",
    ROOT / "assets/works/rl-diffusion/ningshan/rl-diffusion-000.png",
)


def output_path(source: Path, width: int) -> Path:
    return source.with_name(f"{source.stem}-{width}.webp")


def source_width(source: Path) -> int:
    result = subprocess.run(
        ["sips", "-g", "pixelWidth", str(source)],
        check=True,
        capture_output=True,
        text=True,
    )
    for line in result.stdout.splitlines():
        if "pixelWidth:" in line:
            return int(line.rsplit(":", 1)[1].strip())
    raise RuntimeError(f"Could not determine width for {source}")


def create_webp(source: Path, width: int, quality: int) -> None:
    target = output_path(source, width)
    if target.exists() and target.stat().st_mtime >= source.stat().st_mtime:
        return
    subprocess.run(
        [
            "cwebp",
            "-quiet",
            "-q",
            str(quality),
            "-m",
            "6",
            "-metadata",
            "none",
            "-resize",
            str(min(width, source_width(source))),
            "0",
            str(source),
            "-o",
            str(target),
        ],
        check=True,
    )


def main() -> None:
    photos = [
        path
        for root in PHOTO_ROOTS
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in {".jpg", ".jpeg"}
    ]

    for source in photos:
        for width in (640, 1280):
            create_webp(source, width, quality=82)

    for source in CARD_IMAGES:
        for width in (480, 960):
            create_webp(source, width, quality=86)

    print(f"Generated responsive WebP assets for {len(photos)} photographs and {len(CARD_IMAGES)} project cards.")


if __name__ == "__main__":
    main()
