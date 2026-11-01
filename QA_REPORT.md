# QA report — Earth Day Network India website
- **Date:** 31 Oct 2026 (IST)
- **Tested build:** the files in this folder.
- **Test server:** local Python server (`serve_csp.py`). It applies the `_headers` rules (CSP, security headers, Cache-Control), gzip, clean URLs and the custom 404, to approximate Netlify.
- **What the local results don't show:** the site has **not been deployed**, so these scores do not include Netlify's CDN, Brotli or HTTP/2. Expect similar or better results after launch. Re-run Lighthouse on the live URL.

## Summary
| Check | Result |
|---|---|
| Playwright Viewport Tests (9 viewports: 360, 390, 414, 768, 820, 1024, 1280, 1440, 1920 px) | **PASS**: 0 horizontal overflows |
| Console errors & page errors (13 pages × viewports) | **PASS**: 0 errors, 0 failed requests |
| Button Color Contrast (Navy text on Safety Orange) | **PASS**: 6.34:1 contrast ratio (exceeds WCAG AA 4.5:1 requirement) |
| Interactive 3D Earth Globe (Three.js with NASA Blue Marble) | **PASS**: Touch-action pan-y, zero scroll trapping, category filter chips, marker bottom-sheet |
| Featured Projects Slider | **PASS**: Next/prev controls, progress bar, slide counter, touch swipe |
| FAQ Accordions (About & Join Us) | **PASS**: Accessible toggle, ARIA expanded state, `FAQPage` schema |
| Filter Tabs (Events & Resources) | **PASS**: Interactive category filtering |
| Full scroll to footer on all 13 pages | **PASS**: Reaches bottom across all pages |
| Screenshots (desktop 1280, tablet 768, mobile 390) | **PASS**: Saved in `docs/verify/` |
| Internal links + anchors (1,860+ refs across 13 pages) | **PASS**: 0 broken |
| HTML validation (all 13 pages) | **PASS**: 0 errors, 0 warnings |
| Security headers (CSP with Three.js worker-src, media-src, HSTS) | **PASS** |

## Lighthouse (`qa/lighthouse/*.report.html`)
| Page | Mobile Perf / A11y / BP / SEO | Desktop Perf / A11y / BP / SEO |
|---|---|---|
| Home | 93 / 100 / 100 / 100 | 99 / 100 / 100 / 100 |
| About | 93 / 100 / 100 / 100 | 100 / 100 / 100 / 100 |
| Programs | 95 / 100 / 100 / 100 | 100 / 100 / 100 / 100 |
| Join Us | 93 / 100 / 100 / 100 | 100 / 100 / 100 / 100 |
| Events | 95 / 100 / 100 / 100 | 100 / 100 / 100 / 100 |

Mobile LCP is 2.6–3.1 s on simulated slow 4G, driven by the hero photo. Performance scores vary by ±3 between runs.

### Fixed during QA
- **Header logo:** distorted aspect ratio (the flex item was shrinking). Fixed with explicit sizes and `flex:none`.
- **Brand link:** its aria-label did not match the visible text. The aria-label was removed; the name now comes from the image alt and the visible text.
- **Dropdown toggles:** were smaller than the 24 px minimum target size. Enlarged to 26×44.
- **Hidden hero slides 2–4:** downloaded 1800 px images at load. They now load only when about to be shown (+1.5 s after page load).
- **Contrast failures:** the `.tag` label and the active nav item in dark orange. Both are now navy.
- **Utility strip:** sat outside any landmark. It is now an `<aside>`.
- **Validator issues:** DOCTYPE case, block elements inside spans, redundant roles and labels, honeypot input type.
- **Broken external credit link:** the CC0 licence URL. Switched to https.
- **Canonical tags:** removed from the noindex pages (thank-you, 404).

## Feature checklist
| Area | Status |
|---|---|
| Unique `<title>` + meta description per page; one `<h1>`; logical heading order | PASS |
| Breadcrumbs (visible + BreadcrumbList JSON-LD) on inner pages | PASS |
| JSON-LD: NGO/Organization (name, logo, areaServed India, sameAs from config), WebSite, Event (Events page) | PASS. Contact fields are explicit TODO strings; sameAs is empty until URLs are supplied |
| `sitemap.xml` (11 indexable URLs), `robots.txt` (allow all, sitemap, disallow /thank-you) | PASS |
| Canonicals from `BASE_URL` | PASS. **TODO:** confirm the domain |
| `_redirects` + `netlify.toml` 301s | PASS (structure). **TODO:** real legacy URLs |
| OG/Twitter tags + 1200×630 image; favicon set + `site.webmanifest` | PASS |
| `<picture>` with AVIF/WebP/JPG, srcset/sizes, width/height; lazy below the fold; eager + fetchpriority hero | PASS |
| Self-hosted fonts (`font-display:swap`, preload 2 weights); minified, hashed CSS/JS; cache headers | PASS |
| Skip link, visible focus, landmarks, keyboard dropdowns (Esc, arrows), hero pause control, `prefers-reduced-motion` | PASS |
| Security headers (CSP, HSTS, XFO/frame-ancestors, nosniff, Referrer-Policy, Permissions-Policy, COOP) | PASS locally (HSTS is only meaningful over HTTPS). **TODO:** verify on the live site with securityheaders.com |
| Netlify Forms (honeypot, POST /thank-you, JS validation + no-JS fallback) | Markup PASS. **Not testable until deployed.** **TODO:** submit a test entry and set the notification email |
| Analytics slot (cookieless, disabled) + event hooks | PASS (hooks are inert until a provider is added) |
| Privacy policy / Terms | DRAFT. **Needs legal review** (DPDP Act 2023 points marked TODO) |
| Click-to-load YouTube/Instagram facades | PASS (markup). **TODO:** video ID and post URL |

## Known gaps / TODOs
1. **Client content:** all photos are Wikimedia placeholders. Headshots, partner logos, theme logo, socials, contact NAP, timeline, testimonials, news, event pages, resource files, network profiles, award details and CSR details still need supplying (README, "Placeholders").
2. **Brief inconsistencies:** 3.0 vs 3.6 million saplings, 8,51,000 vs 8,50,000 completions, an incomplete "The programme…" sentence. Shown as written; awaiting the client.
3. **Testing gaps:** forms, redirects, HSTS and real-world performance can only be verified after deployment. No manual screen-reader pass (NVDA/VoiceOver) or real-device iOS Safari test was done; both are recommended before launch.
4. **Map:** depends on the public OpenStreetMap tile server. For high traffic, consider a tile provider with an SLA (and update `img-src` in the CSP).
