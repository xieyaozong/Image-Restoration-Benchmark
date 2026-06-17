# Piecewise Contrast Mapping Legacy Notebook

Legacy source material for the `image-restoration-benchmark` project. This folder preserves the original piecewise grayscale intensity-mapping notebook.

The current project implementation lives in:

```text
../../image_restoration_benchmark/contrast.py
../../scripts/run_benchmark.py
```

## Features

- Convert images to grayscale.
- Build a piecewise linear lookup table.
- Stretch or compress low, mid, and high intensity ranges.
- Save the enhanced output image.

## Project Structure

```text
legacy/piecewise-contrast-mapping/
  notebooks/
    piecewise_contrast_mapping_exploration.ipynb
  src/
    piecewise_mapping.py
  scripts/
    run_demo.py
  requirements.txt
```

## Quick Start

Provide your own image:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python scripts/run_demo.py --input path\to\image.jpg
```

The mapped image is saved to `outputs/mapped.jpg`.

## Mapping Parameters

The default control points are:

```text
(0, 0), (r1=70, s1=30), (r2=180, s2=230), (255, 255)
```

You can tune them:

```powershell
python scripts/run_demo.py --input path\to\image.jpg --r1 60 --s1 20 --r2 190 --s2 240
```

## What I Learned

- How grayscale intensity transformations change image contrast.
- How lookup tables make pixel-wise transforms fast and reproducible.
- How control points affect dark, midtone, and bright regions.

## Migration Notes

- Current contrast code lives at the project root under `image_restoration_benchmark/contrast.py`.
- Keep this folder as historical context unless a notebook-specific experiment needs to be reproduced.
- Create new outputs through `../../scripts/run_benchmark.py`.
