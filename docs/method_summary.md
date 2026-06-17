# Method Summary

This project benchmarks restoration and enhancement methods under controlled conditions.

## Degradation Models

Gaussian noise simulates sensor noise and low-light acquisition artifacts. Salt-and-pepper noise simulates impulse corruption where individual pixels are forced to black or white.

## Restoration Methods

Median filtering is well suited for impulse noise because it replaces each pixel with the median value from its local neighborhood. Gaussian blur can reduce random noise, but it may soften edges. Bilateral filtering preserves more edge structure by considering both spatial distance and intensity similarity.

## Contrast Enhancement

Piecewise intensity mapping uses explicit control points to remap grayscale values. CLAHE improves local contrast by applying histogram equalization in small tiles with clipping to avoid over-amplification.

## Metrics

PSNR is useful for pixel-level fidelity when a clean reference is available. MAE and MSE provide direct error summaries. The project also includes a lightweight global SSIM approximation to capture structural similarity without adding heavy dependencies.

For more formal reporting, pair these metrics with visual inspection because high PSNR does not always mean the most perceptually useful image.

