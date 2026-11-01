# Repository Clean-Up and Structure Alignment Report

**Date:** 2026-11-02  
**Safety Branch Created:** `backup-before-cleanup`  
**Git Object Size:** 83.98 MiB (505 objects)  
**Tracked Files:** 477 files  

---

## 1. Directory Structure Alignment

The repository directory structure was reconciled with the strict project specification:

| Directory / Location | Purpose & Contents | Status |
|---|---|---|
| `/` (Project Root) | Generated clean static HTML (`index.html`, `about.html`, `programs.html`, `network.html`, `awards.html`, `events.html`, `resources.html`, `join-us.html`, `privacy-policy.html`, `terms.html`, `credits.html`, `thank-you.html`, `404.html`), `favicon.ico`, `robots.txt`, `sitemap.xml`, `site.webmanifest`, `_headers`, `_redirects`, `netlify.toml`, `README.md`, `.gitignore`. | Verified & Clean |
| `/_src/` | Generator source scripts (`build.py`, `common.py`, `home.py`, `about.py`, `programs.py`, `inner.py`, `legal.py`, `style.css`, `main.js`, `fonts.css`, `og-template.html`). | Standardized |
| `/_src/data/` | Data files (`markers.json` for 3D Globe and Leaflet maps, `credits.json` for 77 media assets). | Structured & Clean |
| `/_src/img/` | Original high-resolution source photos and custom badge SVGs/JPGs. | Maintained |
| `/_src/brand/` | Official client logo vectors. | Maintained |
| `/assets/img/<group>/` | Grouped responsive image sets (`hero/`, `programs/`, `awards/`, `network/`, `events/`, `resources/`, `gallery/`, `about/`, `partners/`, `theme/`). Multi-width WebP, AVIF, and JPG formats. | Grouped & Populated |
| `/assets/icons/` | Web application icons (`icon-192.png`, `icon-512.png`, `icon-maskable.png`, `apple-touch-icon.png`, `favicon-16.png`, `favicon-32.png`, `favicon-48.png`, `favicon.svg`), while preserving `/favicon.ico` at the root. | Generated & Standardized |
| `/assets/data/` | Client-accessible synced data endpoints (`assets/data/markers.json` and `assets/earth/markers.json`). | Synced |
| `/docs/` | Project documentation, client briefs, verification logs (`20261016_Updated_Final_Website_Text_docx.pdf`, `QA_REPORT.md`, `LAUNCH_CHECKLIST.md`, `IMAGE_CREDITS.md`, `coverage.md`, `cleanup.md`, `verify/banners.md`, `verify/verification_summary.json`, `verify/*.png`). | Reorganized |

---

## 2. Removed and Untracked Files

1. **Python Cache Artifacts:**
   - Untracked from Git using `git rm -r --cached _src/__pycache__`:
     - `_src/__pycache__/about.cpython-312.pyc`
     - `_src/__pycache__/about.cpython-313.pyc`
     - `_src/__pycache__/common.cpython-312.pyc`
     - `_src/__pycache__/common.cpython-313.pyc`
     - `_src/__pycache__/home.cpython-312.pyc`
     - `_src/__pycache__/home.cpython-313.pyc`
     - `_src/__pycache__/inner.cpython-312.pyc`
     - `_src/__pycache__/inner.cpython-313.pyc`
     - `_src/__pycache__/legal.cpython-312.pyc`
     - `_src/__pycache__/legal.cpython-313.pyc`
     - `_src/__pycache__/programs.cpython-312.pyc`
     - `_src/__pycache__/programs.cpython-313.pyc`
   - Added `__pycache__/` and `*.pyc` to root `.gitignore`.

2. **Redundant Files Removed:**
   - `_src/credits.json` -> consolidated to canonical `_src/data/credits.json`.
   - Stale build cache hashes removed: `assets/css/style.ce8052ee03.min.css`, `assets/js/main.6f1fb48062.min.js`.

3. **Documentation Moved to `/docs/`:**
   - `IMAGE_CREDITS.md` -> `docs/IMAGE_CREDITS.md`
   - `LAUNCH_CHECKLIST.md` -> `docs/LAUNCH_CHECKLIST.md`
   - `QA_REPORT.md` -> `docs/QA_REPORT.md`

---

## 3. Git Repository Statistics

- **Repository Branch:** `main`
- **Safety Backup Branch:** `backup-before-cleanup`
- **Total Tracked Objects:** 505
- **Tracked Files in Tree:** 477
- **Git Object Pack / Loose Size:** 83.98 MiB
- **Git History Policy:** No force-pushing or destructive history rewrites were performed.

---

## 4. Verification Check Summary

- **Banner Exact Specs:** All 11 inner pages strictly adhere to:
  - H1: 2 to 4 words ($\le 32$ characters)
  - Lede: 14 to 18 words ($\le 110$ characters)
  - Height: 200–240px (mobile), 260–300px (tablet), 340–400px (desktop)
  - Verified via build-time linter outputting `docs/verify/banners.md`
- **Mobile Menu Bounding-Box Overlap:** 0 overlaps detected across all 23 nav links at 360px, 390px, 414px, and 768px.
- **Horizontal Overflows:** 0 horizontal overflows detected across all 9 standard viewports (360px to 1920px).
- **Console Errors:** 0 errors across all 13 pages.
- **Button Contrast:** 6.34:1 (Navy on Blaze Orange), exceeding WCAG AA standards.

