# PSNR Quality Metrics Legacy Notebook

Legacy source material for the `image-restoration-benchmark` project. This folder preserves the original PSNR calculation notebook.

The current project implementation lives in:

```text
../../image_restoration_benchmark/metrics.py
../../scripts/run_benchmark.py
```

## Features

- Convert an image to grayscale.
- Add Gaussian noise.
- Apply median filtering.
- Calculate PSNR between the reference and noisy/filtered outputs.

## Project Structure

```text
legacy/psnr-quality-metrics/
  file/
    1.jpg
  notebooks/
    psnr_quality_metrics_exploration.ipynb
  src/
    psnr_tools.py
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

Generated files are saved to `outputs/`, and PSNR values are printed in the terminal.

## Example

```powershell
python scripts/run_demo.py --input file\1.jpg --sigma 25 --kernel-size 5
```

## What I Learned

- How PSNR quantifies pixel-level reconstruction quality.
- Why denoising can improve PSNR but may also blur detail.
- How noise level and filter kernel size affect image quality.

## Migration Notes

- Current metric code lives at the project root under `image_restoration_benchmark/metrics.py`.
- The benchmark now reports MAE, MSE, PSNR, and global SSIM together.
- New outputs should be generated through `../../scripts/run_benchmark.py`.
