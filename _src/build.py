#!/usr/bin/env python3
"""Build the Earth Day Network India static site.
Usage (from the site root):  python3 _src/build.py      (needs Pillow with AVIF/WebP, and esbuild via npx)
Inputs : _src/*.py templates, _src/style.css, _src/main.js, _src/fonts.css, _src/img/*.jpg (replace with client photos, same names)
Outputs: *.html, assets/css|js (minified + content-hashed), assets/img (AVIF/WebP/JPG srcsets), favicons, sitemap.xml, robots.txt."""
import os, sys, glob, hashlib, subprocess, re, json, datetime, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common
from common import ROOT, SRC, BASE_URL, ORG
from PIL import Image

def images():
    n = 0
    for f in sorted(glob.glob(os.path.join(SRC, "img", "*.jpg"))):
        name = os.path.basename(f); base = os.path.splitext(name)[0]
        grp = common.get_image_group(name)
        out = os.path.join(ROOT, "assets", "img", grp)
        os.makedirs(out, exist_ok=True)
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
    print("images: generated", n, "width sets into grouped folders")

def logos_and_icons():
    L = os.path.join(ROOT, "assets", "logos")
    I = os.path.join(ROOT, "assets", "icons")
    os.makedirs(L, exist_ok=True); os.makedirs(I, exist_ok=True)
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
    for s in (16, 32, 48):
        icon_img = on_bg(s, .06)
        icon_img.save(os.path.join(I, f"favicon-{s}.png"))
    # Save favicon.ico to assets/icons/ and root for browser fallback
    ico = on_bg(48, .06)
    ico.save(os.path.join(I, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    ico.save(os.path.join(ROOT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    
    ati = on_bg(180, .12).convert("RGB")
    ati.save(os.path.join(I, "apple-touch-icon.png"))
    
    for s, name in ((192, "icon-192.png"), (512, "icon-512.png")):
        ic = on_bg(s, .12)
        ic.save(os.path.join(I, name))
        
    maskable = on_bg(512, .22)
    maskable.save(os.path.join(I, "icon-maskable-512.png"))
    
    # SVG favicon
    import base64, io
    b = io.BytesIO(); sq.resize((128, 128), Image.LANCZOS).save(b, "PNG", optimize=True)
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#fff"/><image x="4" y="4" width="56" height="56" href="data:image/png;base64,{base64.b64encode(b.getvalue()).decode()}"/></svg>'
    open(os.path.join(I, "favicon.svg"), "w").write(svg)
    
    json.dump({"name": ORG, "short_name": "EDN India", "start_url": "/", "scope": "/", "display": "standalone", "background_color": "#ffffff", "theme_color": "#07074E", "lang": "en-IN",
               "icons": [{"src": "assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
                         {"src": "assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
                         {"src": "assets/icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]},
              open(os.path.join(ROOT, "site.webmanifest"), "w"), indent=2)
    print("icons organized in assets/icons/ done")

def data_sync():
    src_markers = os.path.join(SRC, "data", "markers.json")
    if os.path.exists(src_markers):
        os.makedirs(os.path.join(ROOT, "assets", "data"), exist_ok=True)
        os.makedirs(os.path.join(ROOT, "assets", "earth"), exist_ok=True)
        shutil.copy2(src_markers, os.path.join(ROOT, "assets", "data", "markers.json"))
        shutil.copy2(src_markers, os.path.join(ROOT, "assets", "earth", "markers.json"))
        print("synced markers.json to assets/data and assets/earth")

def lint_banners():
    print("--- Linting Inner Page Banners ---")
    verify_dir = os.path.join(ROOT, "docs", "verify")
    os.makedirs(verify_dir, exist_ok=True)
    
    report_lines = [
        "# Inner Page Banners Verification Audit\n",
        "Mandatory spec constraints:",
        "- Breadcrumb: max 3 levels, one line, middle collapsed on mobile",
        "- H1: 2 to 4 words, max 32 characters",
        "- Intro line (lede): 14 to 18 words, max 110 characters",
        "- Banner height: mobile 200–240px, tablet 260–300px, desktop 340–400px\n",
        "| Page | H1 Banner Title | Words (2-4) | Chars (≤32) | Intro Line (Lede) | Words (14-18) | Chars (≤110) | Result |",
        "| :--- | :--- | :---: | :---: | :--- | :---: | :---: | :---: |"
    ]
    
    errors = []
    inner_pages = [
        "about.html", "programs.html", "network.html", "awards.html", 
        "events.html", "resources.html", "join-us.html", 
        "privacy-policy.html", "terms.html", "credits.html", "thank-you.html"
    ]
    
    for p in inner_pages:
        path = os.path.join(ROOT, p)
        if not os.path.exists(path):
            errors.append(f"{p}: file does not exist")
            continue
        content = open(path, encoding="utf-8").read()
        
        # Extract banner section
        hero_m = re.search(r'<section class="page-hero">(.*?)</section>', content, re.DOTALL)
        if not hero_m:
            errors.append(f"{p}: missing <section class=\"page-hero\">")
            continue
        hero_html = hero_m.group(1)
        
        # Extract H1
        h1_m = re.search(r'<h1>(.*?)</h1>', hero_html)
        h1_text = h1_m.group(1).strip() if h1_m else ""
        h1_words = len(h1_text.split())
        h1_chars = len(h1_text)
        
        # Extract Lede
        lede_m = re.search(r'<p class="lede">(.*?)</p>', hero_html)
        lede_text = lede_m.group(1).strip() if lede_m else ""
        lede_words = len(lede_text.split())
        lede_chars = len(lede_text)
        
        # Validate limits
        h1_ok = (2 <= h1_words <= 4) and (h1_chars <= 32)
        lede_ok = (14 <= lede_words <= 18) and (lede_chars <= 110)
        
        status = "PASS" if (h1_ok and lede_ok) else "FAIL"
        if not (h1_ok and lede_ok):
            err_msg = f"{p}: H1({h1_words}w, {h1_chars}c, ok={h1_ok}) | Lede({lede_words}w, {lede_chars}c, ok={lede_ok})"
            errors.append(err_msg)
        
        report_lines.append(f"| `{p}` | {h1_text} | {h1_words} | {h1_chars} | {lede_text} | {lede_words} | {lede_chars} | **{status}** |")
        print(f"[{status}] {p:20} -> H1: {h1_words}w/{h1_chars}c | Lede: {lede_words}w/{lede_chars}c")
    
    out_md = os.path.join(verify_dir, "banners.md")
    open(out_md, "w", encoding="utf-8").write("\n".join(report_lines) + "\n")
    print(f"Wrote banner verification report to {out_md}")
    
    if errors:
        print("\nBanner Linter FAILED:")
        for e in errors:
            print("  -", e)
        raise AssertionError("Banner linting failed: one or more pages breached H1 / Lede constraints.")
    else:
        print("All inner page banners PASSED specification!")

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
    data_sync()
    images(); logos_and_icons(); css_js()
    import home, about, programs, inner, legal
    home.build(); about.build(); programs.build()
    inner.network(); inner.awards(); inner.events(); inner.resources(); inner.join()
    legal.build()
    seo_files()
    lint_banners()
