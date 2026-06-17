# Image Restoration Benchmark

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white&style=flat-square)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?logo=opencv&logoColor=white&style=flat-square)
![NumPy](https://img.shields.io/badge/NumPy-2.x-013243?logo=numpy&logoColor=white&style=flat-square)
![Tests](https://img.shields.io/badge/tests-pytest-0A9EDC?logo=pytest&logoColor=white&style=flat-square)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)

Benchmark code for controlled image degradation, restoration, contrast enhancement, and quality evaluation. It includes package code, a CLI, sample assets, notes, and tests; older notebook work is kept under `legacy/`.

![Restoration preview](assets/example_outputs/hero.png)

## What It Does

- Generates Gaussian noise and salt-and-pepper impulse noise.
- Restores degraded images with median, Gaussian, and bilateral filters.
- Enhances contrast with piecewise intensity mapping and CLAHE.
- Evaluates outputs with MAE, MSE, PSNR, and a lightweight global SSIM.
- Exports metric tables, individual output images, and a montage.
- Ships an open-source sample image so the repo runs without private data.

## Results

Benchmark on the bundled open-source sample (`assets/samples/coffee.png`, from scikit-image):

| Case | Method | PSNR | SSIM |
| --- | --- | ---: | ---: |
| salt_pepper | noisy_input | 16.24 | 0.800 |
| salt_pepper | median_3x3 | 31.06 | 0.992 |
| gaussian | noisy_input | 20.54 | 0.919 |
| gaussian | bilateral_filter | 27.93 | 0.984 |
| contrast | clahe | 20.13 | 0.915 |

![Restoration montage](assets/example_outputs/restoration_montage.png)

## Layout

```text
Image-Restoration-Benchmark/
  app/                          CLI entry point
  image_restoration_benchmark/  noise, filters, contrast, metrics, pipeline
  scripts/                      benchmark command
  assets/                       sample image and example outputs
  docs/                         method notes
  tests/                        pytest checks
  legacy/                       older notebook work
```

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -U pip
python -m pip install -e .[dev]
```

## Usage

Regenerate the example outputs shown above:

```powershell
python scripts/run_benchmark.py --input assets\samples\coffee.png --output-dir assets\example_outputs
```

Run a custom experiment:

```powershell
python scripts/run_benchmark.py --input path\to\image.png --output-dir experiments\custom --seed 42 --salt-pepper-amount 0.08 --gaussian-sigma 25
```

Run the tests:

```powershell
python -m pytest -q
```

## Method Overview

```text
reference image
  -> controlled degradation
  -> restoration candidates
  -> contrast enhancement
  -> metric evaluation
  -> CSV, JSON, images, montage
```

## Notes

- The demo uses a single open-source natural image; results illustrate the pipeline rather than dataset-wide performance.
- Global SSIM is a lightweight, dependency-free approximation of windowed SSIM.
- PSNR and SSIM do not always match human visual preference, especially after contrast enhancement.

## License

Released under the [MIT License](LICENSE). Sample images keep their own licenses; see [`assets/samples/SOURCES.md`](assets/samples/SOURCES.md) and the `SOURCES.md` files under `legacy/*/sample/`.
