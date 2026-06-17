from __future__ import annotations

from image_restoration_benchmark.metrics import mean_absolute_error, mean_squared_error, psnr, ssim_global

import math

import numpy as np


def test_identical_images_have_perfect_scores() -> None:
    image = np.full((8, 8), 120, dtype=np.uint8)
    assert mean_absolute_error(image, image) == 0
    assert mean_squared_error(image, image) == 0
    assert math.isinf(psnr(image, image))
    assert ssim_global(image, image) == 1.0


def test_metrics_detect_difference() -> None:
    reference = np.zeros((4, 4), dtype=np.uint8)
    target = np.full((4, 4), 10, dtype=np.uint8)
    assert mean_absolute_error(reference, target) == 10
    assert mean_squared_error(reference, target) == 100
    assert psnr(reference, target) > 0
