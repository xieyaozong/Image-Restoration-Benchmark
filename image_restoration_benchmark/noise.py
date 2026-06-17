from __future__ import annotations

from typing import Optional

import numpy as np

def gaussian_noise(gray_image: np.ndarray, sigma: float = 25.0, seed: Optional[int] = 42) -> np.ndarray:
    rng = np.random.default_rng(seed)
    noise = rng.normal(0.0, sigma, gray_image.shape)
    return np.clip(gray_image.astype(np.float32) + noise, 0, 255).astype(np.uint8)


def salt_pepper_noise(
    gray_image: np.ndarray,
    amount: float = 0.08,
    salt_vs_pepper: float = 0.5,
    seed: Optional[int] = 42,
) -> np.ndarray:
    if not 0 <= amount <= 1:
        raise ValueError("amount must be between 0 and 1.")
    if not 0 <= salt_vs_pepper <= 1:
        raise ValueError("salt_vs_pepper must be between 0 and 1.")

    rng = np.random.default_rng(seed)
    noisy = gray_image.copy()
    height, width = noisy.shape
    pixel_count = height * width
    salt_count = int(pixel_count * amount * salt_vs_pepper)
    pepper_count = int(pixel_count * amount * (1.0 - salt_vs_pepper))

    salt_y = rng.integers(0, height, salt_count)
    salt_x = rng.integers(0, width, salt_count)
    pepper_y = rng.integers(0, height, pepper_count)
    pepper_x = rng.integers(0, width, pepper_count)

    noisy[salt_y, salt_x] = 255
    noisy[pepper_y, pepper_x] = 0
    return noisy
