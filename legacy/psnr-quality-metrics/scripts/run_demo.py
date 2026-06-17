from __future__ import annotations

from pathlib import Path

import argparse
import json
import sys

import cv2

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.psnr_tools import add_gaussian_noise, calculate_psnr, median_filter, to_grayscale


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Calculate PSNR before and after denoising.")
    parser.add_argument("--input", type=Path, default=PROJECT_ROOT / "file" / "1.jpg")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "outputs")
    parser.add_argument("--sigma", type=float, default=25.0)
    parser.add_argument("--kernel-size", type=int, default=3)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    image = cv2.imread(str(args.input))
    if image is None:
        raise FileNotFoundError(f"Could not read image: {args.input}")

    reference = to_grayscale(image)
    noisy = add_gaussian_noise(reference, sigma=args.sigma, seed=args.seed)
    filtered = median_filter(noisy, kernel_size=args.kernel_size)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(args.output_dir / "reference_gray.jpg"), reference)
    cv2.imwrite(str(args.output_dir / "noisy.jpg"), noisy)
    cv2.imwrite(str(args.output_dir / "median_filtered.jpg"), filtered)

    metrics = {
        "psnr_noisy": calculate_psnr(reference, noisy),
        "psnr_filtered": calculate_psnr(reference, filtered),
    }
    (args.output_dir / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
