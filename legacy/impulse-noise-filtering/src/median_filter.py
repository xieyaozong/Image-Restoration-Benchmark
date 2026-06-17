from __future__ import annotations

from typing import Optional

import numpy as np

def add_salt_pepper_noise(
    image: np.ndarray,
    amount: float = 0.1,
    salt_vs_pepper: float = 0.5,
    seed: Optional[int] = 42,
) -> np.ndarray:
    if not 0 <= amount <= 1:
        raise ValueError("amount must be between 0 and 1.")
    if not 0 <= salt_vs_pepper <= 1:
        raise ValueError("salt_vs_pepper must be between 0 and 1.")

    rng = np.random.default_rng(seed)
    noisy = image.copy()
    height, width = noisy.shape[:2]
    pixel_count = height * width

    salt_count = int(pixel_count * amount * salt_vs_pepper)
    pepper_count = int(pixel_count * amount * (1 - salt_vs_pepper))

    salt_y = rng.integers(0, height, salt_count)
    salt_x = rng.integers(0, width, salt_count)
    pepper_y = rng.integers(0, height, pepper_count)
    pepper_x = rng.integers(0, width, pepper_count)

    noisy[salt_y, salt_x] = 255
    noisy[pepper_y, pepper_x] = 0
    return noisy


def median_filter(image: np.ndarray, kernel_size: int = 3) -> np.ndarray:
    if kernel_size < 3 or kernel_size % 2 == 0:
        raise ValueError("kernel_size must be an odd integer >= 3.")

    pad = kernel_size // 2
    if image.ndim == 2:
        padded = np.pad(image, ((pad, pad), (pad, pad)), mode="edge")
        output = np.empty_like(image)
        for y in range(image.shape[0]):
            for x in range(image.shape[1]):
                output[y, x] = np.median(padded[y : y + kernel_size, x : x + kernel_size])
        return output

    padded = np.pad(image, ((pad, pad), (pad, pad), (0, 0)), mode="edge")
    output = np.empty_like(image)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            output[y, x] = np.median(padded[y : y + kernel_size, x : x + kernel_size], axis=(0, 1))
    return output
