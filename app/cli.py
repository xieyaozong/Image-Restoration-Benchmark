from __future__ import annotations

from pathlib import Path
from image_restoration_benchmark.pipeline import run_benchmark

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the image restoration benchmark pipeline.")
    parser.add_argument("--input", type=Path, required=True, help="Input image path.")
    parser.add_argument("--output-dir", type=Path, default=Path("experiments/latest"))
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--salt-pepper-amount", type=float, default=0.08)
    parser.add_argument("--gaussian-sigma", type=float, default=25.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    report = run_benchmark(
        input_path=args.input,
        output_dir=args.output_dir,
        seed=args.seed,
        salt_pepper_amount=args.salt_pepper_amount,
        gaussian_sigma=args.gaussian_sigma,
    )
    print(f"Wrote {len(report.rows)} metric rows to {report.metrics_csv}")
    print(f"Montage: {report.montage_path}")


if __name__ == "__main__":
    main()
