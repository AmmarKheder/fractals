# Burning Ship Fractals

This folder contains multiple high-resolution artistic visualizations of the **Burning Ship fractal**, rendered in 4K using custom techniques.

## Contents

### Scripts
- `script_burning_ship.py` — Complete Python script (parallelized, high-res)

### Outputs (Examples)
| Image | Description |
|-------|-------------|
| `burning_ship_4k.png` | Standard high-resolution rendering |
| `burning_ship_4k_ultra.png` | Ultra-detailed version with extended iterations |
| `burning_ship_bateau_centre_4k.png` | Centered view showcasing the ship shape |
| `burning_ship_inferno.png` | Rendered with the `inferno` colormap for intense contrast |

### Related Fractals (bonus outputs)
| Image | Description |
|-------|-------------|
| `julia.jp2` | Static render from Julia set |
| `julia_pm25_2016_domain.gif` | Julia animated GIF (PM2.5 variation by month) |
| `mandelbrot_distance_4k.png` | Mandelbrot fractal with distance estimation method |

## Features

- 4K and Ultra-HD renders with color gradients and light bloom
- `inferno` palette for contrast-rich effects
- Glow, sparkles, and ambient noise layers
- Parallelized rendering using `multiprocessing.Pool`

## How to Use

To regenerate or experiment with these renders:

1. Install dependencies:
   ```bash
   pip install numpy pillow matplotlib tqdm
