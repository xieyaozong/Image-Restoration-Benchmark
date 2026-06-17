from __future__ import annotations

from pathlib import Path
from typing import List, Union

import cv2
import numpy as np


def save_montage(path: Union[str, Path], items: List[tuple[str, np.ndarray]], columns: int = 3) -> Path:
    if not items:
        raise ValueError("items must not be empty.")

    tile_height = 220
    tile_width = 260
    label_height = 34
    rows = int(np.ceil(len(items) / columns))
    canvas = np.full((rows * (tile_height + label_height), columns * tile_width), 255, dtype=np.uint8)

    for index, (label, image) in enumerate(items):
        row = index // columns
        col = index % columns
        y0 = row * (tile_height + label_height)
        x0 = col * tile_width

        resized = _resize_to_tile(image, tile_width, tile_height)
        canvas[y0 : y0 + tile_height, x0 : x0 + tile_width] = resized
        cv2.putText(
            canvas,
            label[:28],
            (x0 + 8, y0 + tile_height + 23),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            30,
            1,
            cv2.LINE_AA,
        )

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(path), canvas)
    return path


def _resize_to_tile(image: np.ndarray, width: int, height: int) -> np.ndarray:
    gray = image if image.ndim == 2 else cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    scale = min(width / gray.shape[1], height / gray.shape[0])
    new_w = max(1, int(gray.shape[1] * scale))
    new_h = max(1, int(gray.shape[0] * scale))
    resized = cv2.resize(gray, (new_w, new_h), interpolation=cv2.INTER_AREA)
    tile = np.full((height, width), 245, dtype=np.uint8)
    y = (height - new_h) // 2
    x = (width - new_w) // 2
    tile[y : y + new_h, x : x + new_w] = resized
    return tile
