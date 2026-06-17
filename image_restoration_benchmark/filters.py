from __future__ import annotations

import cv2
import numpy as np


def median_filter(image: np.ndarray, kernel_size: int = 3) -> np.ndarray:
    if kernel_size < 3 or kernel_size % 2 == 0:
        raise ValueError("kernel_size must be an odd integer >= 3.")
    return cv2.medianBlur(image, kernel_size)


def gaussian_filter(image: np.ndarray, kernel_size: int = 5, sigma: float = 0.0) -> np.ndarray:
    if kernel_size < 3 or kernel_size % 2 == 0:
        raise ValueError("kernel_size must be an odd integer >= 3.")
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)


def bilateral_filter(image: np.ndarray, diameter: int = 7, sigma_color: float = 50.0, sigma_space: float = 50.0) -> np.ndarray:
    return cv2.bilateralFilter(image, diameter, sigma_color, sigma_space)

