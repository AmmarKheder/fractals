# Fractal Weekends

A personal collection of fractal explorations — every weekend, I experiment with a new fractal type, render it in high resolution, and share the code behind it.

##  Structure

Each fractal type lives in its own folder (e.g. `burning_ship/`, `julia/`, `mandelbrot/`, etc.), and contains:

- `script_<name>.py` – the full Python script to generate the fractal  
- `README.md` – short description and instructions  
- `examples/` – high-res outputs and animations

##  Features

- 4K rendering with smooth coloring and super-sampling  
- Custom palettes (e.g. `inferno` from `matplotlib`)  
- Glow, sparkles, domain coloring, and more  
- Parallelized computation for heavy fractals (`multiprocessing`)

---

##  My Creations

<!-- Add links or previews here -->

---

## 🧪 How to Run

1. Install dependencies:
   ```bash
   pip install numpy pillow matplotlib tqdm
