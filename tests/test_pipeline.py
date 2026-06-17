from __future__ import annotations

from image_restoration_benchmark.noise import salt_pepper_noise

import numpy as np


def test_salt_pepper_noise_is_reproducible() -> None:
    image = np.full((32, 32), 128, dtype=np.uint8)
    first = salt_pepper_noise(image, amount=0.1, seed=123)
    second = salt_pepper_noise(image, amount=0.1, seed=123)
    assert np.array_equal(first, second)
