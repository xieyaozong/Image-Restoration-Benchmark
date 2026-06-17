from __future__ import annotations

from pathlib import Path
from typing import Union

import cv2
import numpy as np


def read_grayscale(path: Union[str, Path]) -> np.ndarray:
    image = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Could not read image: {path}")
    return image


def write_image(path: Union[str, Path], image: np.ndarray) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    ok = cv2.imwrite(str(path), image)
    if not ok:
        raise OSError(f"Could not write image: {path}")
    return path
