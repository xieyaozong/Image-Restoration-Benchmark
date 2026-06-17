from __future__ import annotations

from pathlib import Path

import argparse
import sys

import cv2

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.piecewise_mapping import apply_piecewise_mapping


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Apply piecewise linear grayscale intensity mapping.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "outputs")
    parser.add_argument("--r1", type=int, default=70)
    parser.add_argument("--s1", type=int, default=30)
    parser.add_argument("--r2", type=int, default=180)
    parser.add_argument("--s2", type=int, default=230)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    image = cv2.imread(str(args.input), cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Could not read image: {args.input}")

    mapped = apply_piecewise_mapping(image, r1=args.r1, s1=args.s1, r2=args.r2, s2=args.s2)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(args.output_dir / "mapped.jpg"), mapped)
    print(f"Saved mapped image to {args.output_dir / 'mapped.jpg'}")


if __name__ == "__main__":
    main()
