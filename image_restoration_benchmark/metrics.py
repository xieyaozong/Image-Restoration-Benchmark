from __future__ import annotations

from typing import Union

import math

import numpy as np


def mean_absolute_error(reference: np.ndarray, target: np.ndarray) -> float:
    _validate_pair(reference, target)
    return float(np.mean(np.abs(reference.astype(np.float32) - target.astype(np.float32))))


def mean_squared_error(reference: np.ndarray, target: np.ndarray) -> float:
    _validate_pair(reference, target)
    diff = reference.astype(np.float32) - target.astype(np.float32)
    return float(np.mean(diff * diff))


def psnr(reference: np.ndarray, target: np.ndarray, max_pixel: float = 255.0) -> float:
    mse = mean_squared_error(reference, target)
    if mse == 0:
        return math.inf
    return 20.0 * math.log10(max_pixel / math.sqrt(mse))


def ssim_global(reference: np.ndarray, target: np.ndarray, max_pixel: float = 255.0) -> float:
    _validate_pair(reference, target)
    x = reference.astype(np.float64)
    y = target.astype(np.float64)
    c1 = (0.01 * max_pixel) ** 2
    c2 = (0.03 * max_pixel) ** 2

    mu_x = x.mean()
    mu_y = y.mean()
    sigma_x = x.var()
    sigma_y = y.var()
    sigma_xy = ((x - mu_x) * (y - mu_y)).mean()

    numerator = (2 * mu_x * mu_y + c1) * (2 * sigma_xy + c2)
    denominator = (mu_x * mu_x + mu_y * mu_y + c1) * (sigma_x + sigma_y + c2)
    return float(numerator / denominator)


def metric_row(reference: np.ndarray, target: np.ndarray, case: str, method: str, output: str) -> dict[str, Union[float, str]]:
    return {
        "case": case,
        "method": method,
        "mae": mean_absolute_error(reference, target),
        "mse": mean_squared_error(reference, target),
        "psnr": psnr(reference, target),
        "ssim_global": ssim_global(reference, target),
        "output": output,
    }


def _validate_pair(reference: np.ndarray, target: np.ndarray) -> None:
    if reference.shape != target.shape:
        raise ValueError("reference and target images must have the same shape.")
