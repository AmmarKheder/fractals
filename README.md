# Fractal Weekends

Each weekend, I share a new type of fractal: generator, style, animation, and all the code needed to reproduce it.

---

## 🔷 Current Fractal: Burning Ship

All the following visuals are located in the [`buring_ship/`](./buring_ship) directory.

| Preview | Title |
|--------|-------|
| ![](./buring_ship/burning_ship_4k.png) | Burning Ship – Overexposed Inferno Core
(Fractal with intense central glow and deep inferno palette)|
| ![](./buring_ship/burning_ship_4k_ultra.png) |Burning Ship – Cool Atmosphere Style
(Bluish color scheme with soft outer gradients and starry glow) |
| ![](./buring_ship/burning_ship_bateau_centre_4k.png) |Burning Ship – Noir Edition
(Monochrome rendering with central focus and high contrast) |
| ![](./buring_ship/burning_ship_inferno.png) |Burning Ship – Inferno Centered Sparkle
(High-res centered version with inferno palette and glow highlights) |

---

## 🌀 Other Fractals

| Preview | Title |
|--------|-------|
| ![](./buring_ship/mandelbrot_distance_4k.png) | **mandelbrot_distance_4k.png** — Mandelbrot with distance est. |
| ![](./buring_ship/julia_a.png) | **julia_a.png** — Julia visual variation |
| ![](./buring_ship/julia_fra.png) | **julia.jp2** — Static Julia domain coloring |

---

## Features

- Python-based fractal generation
- High-res outputs (4K+)
- Domain coloring, super-sampling, distance estimation
- Parallel rendering (`multiprocessing`)
- Artistic styles: noise, glow, sparkles, gradients

---

## Structure

```bash
fractals/
│
├── buring_ship/
│   ├── script_burning_ship.py
│   ├── burning_ship_4k.png
│   ├── ...
│   └── README.md
├── README.md
