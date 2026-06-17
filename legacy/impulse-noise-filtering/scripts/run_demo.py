from __future__ import annotations

from pathlib import Path

import argparse
import sys

import cv2

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.median_filter import add_salt_pepper_noise, median_filter


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Add salt-and-pepper noise and apply median filtering.")
    parser.add_argument("--input", type=Path, default=PROJECT_ROOT / "cat" / "cat.jpg")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "outputs")
    parser.add_argument("--amount", type=float, default=0.1)
    parser.add_argument("--kernel-size", type=int, default=3)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    image = cv2.imread(str(args.input))
    if image is None:
        raise FileNotFoundError(f"Could not read image: {args.input}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    noisy = add_salt_pepper_noise(image, amount=args.amount, seed=args.seed)
    filtered = median_filter(noisy, kernel_size=args.kernel_size)

    cv2.imwrite(str(args.output_dir / "original.jpg"), image)
    cv2.imwrite(str(args.output_dir / "noisy.jpg"), noisy)
    cv2.imwrite(str(args.output_dir / "median_filtered.jpg"), filtered)
    print(f"Saved results to {args.output_dir}")


if __name__ == "__main__":
    main()
