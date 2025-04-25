#!/usr/bin/env python3
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import numpy as np
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
from PIL import Image, ImageDraw, ImageFilter
import matplotlib.pyplot as plt

SSF = 1.2
W_SS, H_SS = int(3840 * SSF), int(2160 * SSF)
W, H = 3840, 2160

RE_MIN, RE_MAX = -1.82, -1.68
IM_MIN, IM_MAX = -0.12, 0.08

MAX_ITER = 1000
N_WORKERS = min(cpu_count(), 32)

def compute_strip(args):
    y0, y1 = args
    arr = np.zeros((y1 - y0, W_SS), dtype=np.float32)
    xs = np.linspace(RE_MIN, RE_MAX, W_SS, dtype=np.float32)
    ys = np.linspace(IM_MIN, IM_MAX, H_SS, dtype=np.float32)[y0:y1]
    for i, im in enumerate(ys):
        for j, re in enumerate(xs):
            z = 0 + 0j
            c = complex(re, im)
            n = 0
            while (z.real*z.real + z.imag*z.imag < 4.0) and (n < MAX_ITER):
                z = complex(abs(z.real), abs(z.imag))**2 + c
                n += 1
            if n < MAX_ITER:
                mod = abs(z)
                mu = n + 1 - np.log(np.log(mod)) / np.log(2)
            else:
                mu = MAX_ITER
            arr[i, j] = mu
    return y0, arr

if __name__ == '__main__':
    ys = np.linspace(0, H_SS, N_WORKERS + 1, dtype=int)
    jobs = [(ys[i], ys[i+1]) for i in range(N_WORKERS)]
    mu = np.zeros((H_SS, W_SS), dtype=np.float32)

    with Pool(N_WORKERS) as pool:
        for y0, part in tqdm(pool.imap_unordered(compute_strip, jobs),
                              total=len(jobs), desc="bands"):
            mu[y0:y0+part.shape[0]] = part

    mask = mu < MAX_ITER
    ext = mu.copy()
    ext[~mask] = 0
    vmin = np.percentile(ext[ext>0], 1)
    vmax = np.percentile(ext, 99)
    norm = np.clip((mu - vmin) / (vmax - vmin), 0, 1)

    bg = Image.new('RGB', (W_SS, H_SS), (0, 0, 0))
    draw = ImageDraw.Draw(bg)
    top = np.array((0, 0, 0))
    bot = np.array((10, 0, 31))
    for y in range(H_SS):
        t = y / (H_SS - 1)
        col = tuple((top * (1 - t) + bot * t).astype(int))
        draw.line([(0, y), (W_SS, y)], fill=col)
    bg = bg.convert('RGBA')

    cmap = plt.get_cmap('inferno')
    img_rgba = cmap(norm, bytes=True)
    img_rgba[..., 3] = (mask * 255).astype(np.uint8)
    layer = Image.fromarray(img_rgba, mode='RGBA')

    edge = np.zeros_like(mask)
    edge[1:-1, 1:-1] = (mask[1:-1, 1:-1] &
                        (~mask[1:-1, 2:] | ~mask[1:-1, :-2] |
                         ~mask[2:, 1:-1] | ~mask[:-2, 1:-1]))
    ys_e, xs_e = np.nonzero(edge)
    np.random.seed(7)
    picks = np.random.choice(len(xs_e), size=6000, replace=False)
    draw_e = ImageDraw.Draw(layer)
    for idx in picks:
        x, y = xs_e[idx], ys_e[idx]
        rgba = cmap(norm[y, x])
        rgb = tuple(int(255 * c) for c in rgba[:3])
        r = np.random.randint(1, 4)
        a = np.random.randint(100, 180)
        draw_e.ellipse([(x - r, y - r), (x + r, y + r)], fill=(*rgb, a))

    noise = np.random.normal(0.5, 0.08, (H_SS, W_SS)).clip(0, 1)
    noise = (noise * 255).astype(np.uint8)
    n_img = Image.fromarray(noise, mode='L').convert('RGBA')
    n_img.putalpha(20)
    layer = Image.alpha_composite(layer, n_img)

    glow = layer.filter(ImageFilter.GaussianBlur(radius=4))
    layer = Image.blend(layer, glow, alpha=0.15)

    final = Image.alpha_composite(bg, layer)
    final = final.resize((W, H), resample=Image.LANCZOS)

    out = '...'
    final.save(out, 'PNG')