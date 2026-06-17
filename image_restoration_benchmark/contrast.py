from __future__ import annotations

import cv2
import numpy as np


def build_piecewise_lut(r1: int = 70, s1: int = 30, r2: int = 180, s2: int = 230) -> np.ndarray:
    if not (0 <= r1 < r2 <= 255):
        raise ValueError("Expected 0 <= r1 < r2 <= 255.")
    if not (0 <= s1 <= 255 and 0 <= s2 <= 255):
        raise ValueError("Expected 0 <= s1,s2 <= 255.")
    x_points = np.array([0, r1, r2, 255], dtype=np.float32)
    y_points = np.array([0, s1, s2, 255], dtype=np.float32)
    return np.interp(np.arange(256), x_points, y_points).clip(0, 255).astype(np.uint8)


def piecewise_mapping(gray_image: np.ndarray, r1: int = 70, s1: int = 30, r2: int = 180, s2: int = 230) -> np.ndarray:
    if gray_image.ndim != 2:
        raise ValueError("piecewise_mapping expects a grayscale image.")
    return build_piecewise_lut(r1, s1, r2, s2)[gray_image]


def clahe(gray_image: np.ndarray, clip_limit: float = 2.0, tile_grid_size: tuple[int, int] = (8, 8)) -> np.ndarray:
    if gray_image.ndim != 2:
        raise ValueError("clahe expects a grayscale image.")
    enhancer = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    return enhancer.apply(gray_image)

