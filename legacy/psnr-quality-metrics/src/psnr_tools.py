from __future__ import annotations

from typing import Optional

import cv2
import math
import numpy as np


def to_grayscale(image: np.ndarray) -> np.ndarray:
    if image.ndim == 2:
        return image
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def add_gaussian_noise(gray_image: np.ndarray, sigma: float = 25.0, seed: Optional[int] = 42) -> np.ndarray:
    rng = np.random.default_rng(seed)
    noise = rng.normal(0, sigma, gray_image.shape)
    noisy = gray_image.astype(np.float32) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)


def median_filter(gray_image: np.ndarray, kernel_size: int = 3) -> np.ndarray:
    if kernel_size < 3 or kernel_size % 2 == 0:
        raise ValueError("kernel_size must be an odd integer >= 3.")
    return cv2.medianBlur(gray_image, kernel_size)


def calculate_psnr(reference: np.ndarray, target: np.ndarray, max_pixel: float = 255.0) -> float:
    if reference.shape != target.shape:
        raise ValueError("reference and target must have the same shape.")
    mse = np.mean((reference.astype(np.float32) - target.astype(np.float32)) ** 2)
    if mse == 0:
        return math.inf
    return 20 * math.log10(max_pixel / math.sqrt(float(mse)))
