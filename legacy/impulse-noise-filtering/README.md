# Impulse Noise Filtering Legacy Notebook

Legacy source material for the `image-restoration-benchmark` project. This folder preserves the original salt-and-pepper noise and median-filtering notebook.

The current project implementation lives in:

```text
../../image_restoration_benchmark/noise.py
../../image_restoration_benchmark/filters.py
../../scripts/run_benchmark.py
```

## Features

- Add configurable salt-and-pepper noise.
- Apply a manual median filter implementation.
- Compare original, noisy, and filtered outputs.
- Save reproducible results with a random seed.

## Project Structure

```text
legacy/impulse-noise-filtering/
  cat/
    cat.jpg
  notebooks/
    impulse_noise_filtering_exploration.ipynb
  src/
    median_filter.py
  scripts/
    run_demo.py
  requirements.txt
```

## Quick Start

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python scripts/run_demo.py
```

Generated legacy files are saved to `outputs/`.

## Example With Custom Parameters

```powershell
python scripts/run_demo.py --input cat\cat.jpg --amount 0.15 --kernel-size 5
```

## What I Learned

- How impulse noise affects local image neighborhoods.
- Why median filtering is effective for salt-and-pepper noise.
- How kernel size changes denoising strength and edge preservation.

## Migration Notes

- Current benchmark code compares restoration methods at the project root.
- Keep this folder as historical context unless a notebook-specific experiment needs to be reproduced.
- Create new outputs through `../../scripts/run_benchmark.py`.
