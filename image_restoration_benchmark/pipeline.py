from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Union
from image_restoration_benchmark.contrast import clahe, piecewise_mapping
from image_restoration_benchmark.filters import bilateral_filter, gaussian_filter, median_filter
from image_restoration_benchmark.io import read_grayscale, write_image
from image_restoration_benchmark.metrics import metric_row
from image_restoration_benchmark.noise import gaussian_noise, salt_pepper_noise
from image_restoration_benchmark.visualization import save_montage

import csv
import json

import numpy as np


@dataclass
class BenchmarkReport:
    rows: List[dict[str, Union[float, str]]]
    metrics_csv: Path
    metrics_json: Path
    montage_path: Path


def run_benchmark(
    input_path: Union[str, Path],
    output_dir: Union[str, Path],
    seed: int = 42,
    salt_pepper_amount: float = 0.08,
    gaussian_sigma: float = 25.0,
) -> BenchmarkReport:
    output_dir = Path(output_dir)
    image_dir = output_dir / "images"
    reference = read_grayscale(input_path)
    write_image(image_dir / "00_reference.png", reference)

    salt_pepper = salt_pepper_noise(reference, amount=salt_pepper_amount, seed=seed)
    gaussian = gaussian_noise(reference, sigma=gaussian_sigma, seed=seed + 1)

    candidates: list[tuple[str, str, np.ndarray, str]] = [
        ("salt_pepper", "noisy_input", salt_pepper, "01_salt_pepper.png"),
        ("salt_pepper", "median_3x3", median_filter(salt_pepper, 3), "02_salt_pepper_median_3x3.png"),
        ("salt_pepper", "median_5x5", median_filter(salt_pepper, 5), "03_salt_pepper_median_5x5.png"),
        ("gaussian", "noisy_input", gaussian, "04_gaussian_noise.png"),
        ("gaussian", "gaussian_blur_5x5", gaussian_filter(gaussian, 5), "05_gaussian_blur_5x5.png"),
        ("gaussian", "bilateral_filter", bilateral_filter(gaussian), "06_bilateral_filter.png"),
        ("contrast", "piecewise_mapping", piecewise_mapping(reference), "07_piecewise_mapping.png"),
        ("contrast", "clahe", clahe(reference), "08_clahe.png"),
    ]

    rows: List[dict[str, Union[float, str]]] = []
    montage_items: List[tuple[str, np.ndarray]] = [("reference", reference)]
    for case, method, image, filename in candidates:
        path = write_image(image_dir / filename, image)
        rows.append(metric_row(reference, image, case=case, method=method, output=str(path)))
        montage_items.append((f"{case}/{method}", image))

    metrics_csv = output_dir / "metrics.csv"
    metrics_json = output_dir / "metrics.json"
    montage_path = output_dir / "restoration_montage.png"
    _write_metrics_csv(metrics_csv, rows)
    metrics_json.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    save_montage(montage_path, montage_items)
    return BenchmarkReport(rows=rows, metrics_csv=metrics_csv, metrics_json=metrics_json, montage_path=montage_path)


def _write_metrics_csv(path: Path, rows: List[dict[str, Union[float, str]]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["case", "method", "mae", "mse", "psnr", "ssim_global", "output"])
        writer.writeheader()
        writer.writerows(rows)
