#!/usr/bin/env python3
"""Owned motion graphics for the HARMONICS video -> assets/generated/gfx_*.mp4"""
import math, os, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
ROOT = os.path.dirname(os.path.abspath(__file__))
OUTD = os.path.join(ROOT, "assets", "generated")
W, H, FPS = 1920, 1080, 30
BG = (11, 14, 24)
GOLD = (214, 178, 102)
SOFT = (226, 228, 234)
DIM = (120, 126, 140)
SERIF = "/System/Library/Fonts/Supplemental/Baskerville.ttc"
SANS = "/System/Library/Fonts/HelveticaNeue.ttc"


def font(path, size, index=0):
    return ImageFont.truetype(path, size, index=index)


F_BIG = font(SERIF, 150)
F_MID = font(SERIF, 64)
F_LAB = font(SANS, 34, index=7)   # Helvetica Neue Light
F_SM = font(SANS, 24, index=7)


def ease(x):
    x = min(max(x, 0.0), 1.0)
    return x * x * (3 - 2 * x)


def background():
    y, x = np.mgrid[0:H, 0:W]
    r = np.hypot((x - W * 0.5) / W, (y - H * 0.42) / H)
    v = np.clip(1.0 - r * 1.3, 0, 1)[..., None]
    base = np.array(BG, float)
    lift = np.array([24, 26, 40], float)
    return Image.fromarray((base + lift * v * 0.6).astype(np.uint8))


BGIMG = background()


def writer(name, seconds):
    out = os.path.join(OUTD, name)
    p = subprocess.Popen([FF, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "16",
                          "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    return p, int(seconds * FPS), out


def glow(img, layer, radius=14, strength=1.0):
    blur = layer.filter(ImageFilter.GaussianBlur(radius))
    a = np.asarray(img, float) + np.asarray(blur, float) * strength + np.asarray(layer, float)
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def centered(d, xy, text, f, fill):
    w = d.textlength(text, font=f)
    d.text((xy[0] - w / 2, xy[1]), text, font=f, fill=fill)


# ---------- 1. octave climb ----------
def octave_climb(seconds=10):
    year = 365.25636 * 86400
    p, n, out = writer("gfx_octave_climb.mp4", seconds)
    x0, y0, x1, y1 = 300, 820, 1620, 200
    for i in range(n):
        t = i / FPS
        prog = ease((t - 0.8) / (seconds - 3.2))
        steps = prog * 32
        img = BGIMG.copy()
        lay = Image.new("RGB", (W, H), (0, 0, 0))
        d, dl = ImageDraw.Draw(img), ImageDraw.Draw(lay)
        # staircase: 32 doublings
        for k in range(32):
            sx = x0 + (x1 - x0) * k / 32
            sy = y0 + (y1 - y0) * k / 32
            ex = x0 + (x1 - x0) * (k + 1) / 32
            ey = y0 + (y1 - y0) * (k + 1) / 32
            on = steps - k
            col = GOLD if on > 0 else (40, 44, 58)
            a = min(max(on, 0), 1)
            if a > 0:
                mx = sx + (ex - sx) * a
                dl.line([(sx, sy), (mx, sy)], fill=col, width=4)
                if a >= 1:
                    dl.line([(ex, sy), (ex, ey)], fill=col, width=4)
            else:
                d.line([(sx, sy), (ex, sy), (ex, ey)], fill=col, width=2)
        img = glow(img, lay, 10, 0.9)
        d = ImageDraw.Draw(img)
        k = int(min(steps, 32))
        f = (2 ** k) / year
        period = 1 / f
        if period >= 86400 * 2:
            line = f"one cycle every {period / 86400:,.0f} days"
        elif period >= 3600 * 2:
            line = f"one cycle every {period / 3600:,.1f} hours"
        elif period >= 120:
            line = f"one cycle every {period / 60:,.0f} minutes"
        elif period >= 1.2:
            line = f"one cycle every {period:,.1f} seconds"
        else:
            line = f"{f:,.1f} Hz" if f < 100 else f"{f:,.2f} Hz"
        d.text((300, 120), "Earth's year" if k == 0 else f"doubled {k} time{'s' if k > 1 else ''}", font=F_LAB, fill=DIM)
        d.text((300, 165), line, font=F_MID, fill=SOFT)
        if steps >= 32:
            a = ease((t - (seconds - 2.4)) / 0.9)
            big = "136.1 Hz"
            tl = Image.new("RGB", (W, H), (0, 0, 0))
            ImageDraw.Draw(tl).text((1180, 380), big, font=F_BIG, fill=tuple(int(c * a) for c in GOLD))
            img = glow(img, tl, 18, 1.1)
            d = ImageDraw.Draw(img)
            d.text((1190, 560), "audible: Earth's year as a tone", font=F_LAB, fill=tuple(int(c * a) for c in SOFT))
        d.text((300, 860), "32 octaves · after Cousto, The Cosmic Octave", font=F_SM, fill=DIM)
        p.stdin.write(np.asarray(img).tobytes())
    p.stdin.close(); p.wait()
    return out


# ---------- 2. Kepler intervals as Lissajous figures ----------
def kepler_lissajous(seconds=11):
    p, n, out = writer("gfx_kepler_intervals.mp4", seconds)
    figs = [("Saturn", 4, 5, "major third"), ("Jupiter", 5, 6, "minor third"), ("Mars", 2, 3, "perfect fifth")]
    cx = [400, 960, 1520]
    R = 210
    for i in range(n):
        t = i / FPS
        img = BGIMG.copy()
        lay = Image.new("RGB", (W, H), (0, 0, 0))
        dl = ImageDraw.Draw(lay)
        for j, (name, a, b, label) in enumerate(figs):
            start = 0.6 + j * 0.9
            prog = ease((t - start) / 5.5)
            if prog <= 0:
                continue
            T = np.linspace(0, 2 * math.pi * prog, max(int(1400 * prog), 2))
            phase = t * 0.35
            xs = cx[j] + R * np.sin(a * T + math.pi / 2 + phase)
            ys = 430 + R * np.sin(b * T)
            pts = list(zip(xs.tolist(), ys.tolist()))
            dl.line(pts, fill=GOLD, width=3)
        img = glow(img, lay, 9, 0.8)
        d = ImageDraw.Draw(img)
        for j, (name, a, b, label) in enumerate(figs):
            al = ease((t - 0.6 - j * 0.9) / 1.2)
            c = lambda col: tuple(int(v * al) for v in col)
            centered(d, (cx[j], 700), name, F_LAB, c(DIM))
            centered(d, (cx[j], 745), f"{a} : {b}", F_MID, c(SOFT))
            centered(d, (cx[j], 830), label, F_LAB, c(GOLD))
        d.text((240, 120), "Kepler's interval assignments, drawn as two frequencies in ratio", font=F_LAB, fill=DIM)
        p.stdin.write(np.asarray(img).tobytes())
    p.stdin.close(); p.wait()
    return out


# ---------- 3. Schumann resonance spectrum ----------
def schumann(seconds=10):
    p, n, out = writer("gfx_schumann.mp4", seconds)
    peaks = [(7.83, 1.0), (14.3, 0.62), (20.8, 0.45), (27.3, 0.33), (33.8, 0.25)]
    gx0, gx1, gy0, gy1 = 260, 1660, 830, 360   # plot box (y0 bottom)
    fx = lambda hz: gx0 + (gx1 - gx0) * hz / 40.0
    hz = np.linspace(0.5, 40, 900)
    amp = sum(h / (1 + ((hz - f) / 1.6) ** 2) for f, h in peaks) + 0.05
    amp = amp / amp.max()
    ys = gy0 - (gy0 - gy1) * amp * 0.92
    for i in range(n):
        t = i / FPS
        img = BGIMG.copy()
        d = ImageDraw.Draw(img)
        # below-hearing band
        d.rectangle([gx0, gy1 - 40, fx(20), gy0], fill=(18, 22, 36))
        d.text((fx(20) - 330, gy0 - 40), "below human hearing (< 20 Hz)", font=F_SM, fill=DIM)
        d.line([(gx0, gy0), (gx1, gy0)], fill=(70, 76, 92), width=2)
        for f in (0, 10, 20, 30, 40):
            centered(d, (fx(f), gy0 + 14), f"{f} Hz", F_SM, DIM)
        prog = ease((t - 0.5) / 5.0)
        k = int(len(hz) * prog)
        lay = Image.new("RGB", (W, H), (0, 0, 0))
        dl = ImageDraw.Draw(lay)
        if k > 2:
            dl.line(list(zip([fx(v) for v in hz[:k]], ys[:k].tolist())), fill=GOLD, width=4)
        img = glow(img, lay, 10, 0.9)
        d = ImageDraw.Draw(img)
        for f, h in peaks:
            if hz[max(k - 1, 0)] >= f:
                a = ease((t - 0.5 - 5.0 * f / 40) / 0.8)
                py = gy0 - (gy0 - gy1) * (h / 1.0) * 0.92
                col = tuple(int(v * a) for v in (SOFT if f != 7.83 else GOLD))
                centered(d, (fx(f), py - 62 - (0 if f == 7.83 else 22)), f"{f:g} Hz" if f == 7.83 else f"{f:g}", F_LAB, col)
        a = ease((t - 6.0) / 1.0)
        d.text((gx0, 120), "Schumann resonances: the Earth–ionosphere cavity", font=F_LAB, fill=DIM)
        d.text((gx0, 165), "7.83 Hz, delivered as vibration", font=F_MID, fill=tuple(int(v * a) for v in SOFT))
        d.text((gx0, gy0 + 60), "Peak values after Balser & Wagner (1960)", font=F_SM, fill=DIM)
        p.stdin.write(np.asarray(img).tobytes())
    p.stdin.close(); p.wait()
    return out


if __name__ == "__main__":
    for fn in (octave_climb, kepler_lissajous, schumann):
        print(fn())
