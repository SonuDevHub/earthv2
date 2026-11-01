#!/usr/bin/env python3
"""Build the Earth Day Network India static site.
Usage (from the site root):  python3 _src/build.py      (needs Pillow with AVIF/WebP, and esbuild via npx)
Inputs : _src/*.py templates, _src/style.css, _src/main.js, _src/fonts.css, _src/img/*.jpg (replace with client photos, same names)
Outputs: *.html, assets/css|js (minified + content-hashed), assets/img (AVIF/WebP/JPG srcsets), favicons, sitemap.xml, robots.txt."""
import os, sys, glob, hashlib, subprocess, re, json, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common
from common import ROOT, SRC, BASE_URL, ORG
from PIL import Image

def images():
    out = os.path.join(ROOT, "assets", "img"); os.makedirs(out, exist_ok=True)
    n = 0
    for f in sorted(glob.glob(os.path.join(SRC, "img", "*.jpg"))):
        name = os.path.basename(f); base = os.path.splitext(name)[0]
        ws, w0, h0 = common.variants(name)
        im = None
        for w in ws:
            targets = {ext: os.path.join(out, f"{base}-{w}.{ext}") for ext in ("avif", "webp", "jpg")}
            if all(os.path.exists(t) and os.path.getmtime(t) >= os.path.getmtime(f) for t in targets.values()): continue
            if im is None: im = Image.open(f).convert("RGB")
            r = im.resize((w, round(h0 * w / w0)), Image.LANCZOS) if w < w0 else im
            r.save(targets["jpg"], "JPEG", quality=74, optimize=True, progressive=True)
            r.save(targets["webp"], "WEBP", quality=70, method=6)
            r.save(targets["avif"], "AVIF", quality=52, speed=6)
            n += 1
    print("images: generated", n, "width sets")

def logos_and_icons():
    L = os.path.join(ROOT, "assets", "logos")
    src_blue = os.path.join(SRC, "brand", "logo_blue.png"); src_white = os.path.join(SRC, "brand", "logo_white.png")
    mark = os.path.join(SRC, "brand", "mark-navy.png")
    for src, stem, ws in ((src_blue, "logo-navy", (182, 364, 512)), (src_white, "logo-white", (216,))):
        im = Image.open(src).convert("RGBA")
        for w in ws:
            r = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
            r.save(os.path.join(L, f"{stem}-{w}.png"), optimize=True); r.save(os.path.join(L, f"{stem}-{w}.webp"), quality=85, method=6)
    m = Image.open(mark).convert("RGBA")
    bbox = m.getbbox(); m = m.crop(bbox)
    side = max(m.size); sq = Image.new("RGBA", (side, side), (0, 0, 0, 0)); sq.paste(m, ((side - m.width) // 2, (side - m.height) // 2))
    def on_bg(size, pad=0.14, bg=(255, 255, 255, 255)):
        c = Image.new("RGBA", (size, size), bg); inner = round(size * (1 - 2 * pad))
        t = sq.resize((inner, inner), Image.LANCZOS); c.alpha_composite(t, ((size - inner) // 2, (size - inner) // 2)); return c
    for s in (16, 32, 48): on_bg(s, .06).save(os.path.join(ROOT, f"favicon-{s}.png"))
    on_bg(48, .06).save(os.path.join(ROOT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    on_bg(180, .12).convert("RGB").save(os.path.join(ROOT, "apple-touch-icon.png"))
    on_bg(192, .12).save(os.path.join(ROOT, "icon-192.png")); on_bg(512, .12).save(os.path.join(ROOT, "icon-512.png"))
    on_bg(512, .22).save(os.path.join(ROOT, "icon-maskable-512.png"))
    # SVG favicon: vector frame with the official mark embedded (raster source; replace with a vector mark when available)
    import base64, io
    b = io.BytesIO(); sq.resize((128, 128), Image.LANCZOS).save(b, "PNG", optimize=True)
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#fff"/><image x="4" y="4" width="56" height="56" href="data:image/png;base64,{base64.b64encode(b.getvalue()).decode()}"/></svg>'
    open(os.path.join(ROOT, "favicon.svg"), "w").write(svg)
    json.dump({"name": ORG, "short_name": "EDN India", "start_url": "/", "scope": "/", "display": "standalone", "background_color": "#ffffff", "theme_color": "#07074E", "lang": "en-IN",
               "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"},
                         {"src": "/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]},
              open(os.path.join(ROOT, "site.webmanifest"), "w"), indent=2)
    print("logos/favicons done")

def minify(kind, text):
    cmd = ["npx.cmd" if os.name == "nt" else "npx", "--yes", "esbuild", f"--loader={kind}", "--minify", "--target=es2017" if kind == "js" else "--target=chrome90,firefox90,safari14"]
    r = subprocess.run(cmd, input=text.encode(), capture_output=True, shell=(os.name == "nt"))
    if r.returncode:
        print(f"Warning: esbuild minify error: {r.stderr.decode()[:120]}, using original text")
        return text
    return r.stdout.decode()

def css_js():
    fonts = open(os.path.join(SRC, "fonts.css")).read()
    fonts = re.sub(r"url\(([^)\"']+\.woff2)\)", r"url(../fonts/\1)", fonts)
    css = open(os.path.join(SRC, "style.css")).read().replace('@import "fonts.css";', fonts)
    js = open(os.path.join(SRC, "main.js")).read()
    for kind, text, d in (("css", css, "css"), ("js", js, "js")):
        out = minify(kind, text); h = hashlib.sha256(out.encode()).hexdigest()[:10]
        od = os.path.join(ROOT, "assets", d); os.makedirs(od, exist_ok=True)
        for old in glob.glob(os.path.join(od, f"*.min.{kind}")): os.remove(old)
        fn = f"{'style' if kind == 'css' else 'main'}.{h}.min.{kind}"
        open(os.path.join(od, fn), "w").write(out)
        common.ASSETS[kind] = f"assets/{d}/{fn}"
        print(kind, fn, len(text), "->", len(out), "bytes")

def seo_files():
    today = datetime.date.today().isoformat()
    urls = "".join(f"<url><loc>{BASE_URL}/{'' if f == 'index.html' else f}</loc><lastmod>{today}</lastmod><priority>{p}</priority></url>\n" for f, p in common.PAGES)
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"# TODO: confirm BASE_URL ({BASE_URL}) before launch\nUser-agent: *\nAllow: /\nDisallow: /thank-you\nDisallow: /thank-you.html\n\nSitemap: {BASE_URL}/sitemap.xml\n")
    print("sitemap:", len(common.PAGES), "urls")

if __name__ == "__main__":
    images(); logos_and_icons(); css_js()
    import home, about, programs, inner, legal
    home.build(); about.build(); programs.build()
    inner.network(); inner.awards(); inner.events(); inner.resources(); inner.join()
    legal.build()
    seo_files()
