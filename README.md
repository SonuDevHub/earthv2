# Earth Day Network India — website

This is a static, multi-page website built with HTML, CSS and vanilla JS. It has no framework and does not need a build step to view.

- **To view it:** open `http://localhost/earth-day/` through XAMPP, or open `index.html` directly.
- **To deploy it:** publish this folder as-is on Netlify. The folder includes `_headers`, `_redirects` and `netlify.toml`.

## Pages & Components
| Page | File | Notes & Components |
|---|---|---|
| Home | `index.html` | Hero slideshow (5 photos), intro, show panel (5 square photos), impact counters, awardee collage, Theme 2027 panel, events boxes, major programs carousel, partner marquee and logo image, YouTube/Instagram click-to-load embeds, news, quotes, footer with newsletter form. The 3D globe is commented out |
| About | `about.html` | Story, 4-stat impact strip (55+ years, 192 countries, 1B+ mobilized, 130+ partners), approach flow, call to action, Trustees note, timeline, gallery, trust & governance FAQ accordion (`FAQPage` schema), closing CTA band |
| Programs | `programs.html` | Stats strip (3.6M+ trees, 5,00,000+ farmers, 8,50,000+ completions, 1,00,000+ schools), EDO Theme, all 10 brief programmes (`#agriculture`, `#canopy`, `#energy`, `#education`, `#youth`, `#cleanup`, `#faith-sites`, `#earth-day`, `#climate-change`, `#women`, `#fashion`), partners slot, gallery, closing CTA band |
| Network | `network.html` | Stats strip (300+ youth ambassadors, 130+ partners, 400+ awards, 147.5M outreach), `#ambassadors`, `#advisors`, `#canopy-experts`, `#mfmv`, `#artists`, `#athletes`, `#partners`, closing CTA band |
| Awards | `awards.html` | Reference-style award card grid with medal icons, `#our-awards` (9 key awards), `#browse` (5 sectors), `#all-awards` (14 categories with ledger cards and nomination CTAs) |
| Events | `events.html` | Interactive filter tabs (All, Upcoming, Ongoing, Past, News), dated rows, `#ongoing` Young Climate Champions spotlight, `#past` archival cards, `#news` coverage list |
| Resources | `resources.html` | Interactive filter tabs (All, Reports, Educational, Media, Guides), filterable index across 10 resource categories, featured Energy Literacy course card |
| Join Us | `join-us.html` | 4 path blocks (`#csr`, `#partner`, `#volunteer`, `#forms`), Partner With Us section featuring all 18 named organizations, Netlify Forms with validation, comprehensive 6-item FAQ accordion with `FAQPage` schema |
| Contact | (footer `#contact`) | Accessible footer with Write to Us form, Newsletter subscription form, NITI Aayog/12A/CSR-1 badges, social links, and legal links |
| Legal / utility | `privacy-policy.html`, `terms.html`, `credits.html`, `thank-you.html` (noindex), `404.html` (noindex) | Complete privacy policy, terms, credits with full licensing details |

## Editing
The site is plain HTML, CSS and JS with no build step. Edit the files directly and refresh the browser.

| File | Purpose |
|---|---|
| `*.html` | Each page. The header and footer are repeated in every page, so change them in all of them |
| `assets/css/style.css` | All styles, including the font-face rules |
| `assets/js/main.js` | All scripts |
| `assets/img/<group>/` | Photos in AVIF, WebP and JPG sizes. Each `<picture>` lists its own files |
| `assets/earth/markers.json` | Marker data for the 3D globe |

The 3D globe section is commented out in `index.html`. Remove the two comment lines around it to bring it back.

## Placeholders still needed from the client
Every placeholder is visibly labelled on the site, so nothing passes as real content.
1. **Photos:** still needed for Sustainable Fashion, the Network groups and the E-Racing Car show-panel slot.
2. **More awardee headshots:** the home collage has 8 people; the document asks for 10–12.
5. **Social media URLs**, plus a **YouTube video ID** and an **Instagram post URL**.
6. **Address, phone, email** (footer + JSON-LD). NGO Darpan / 12A / CSR-1 registration numbers if they should be shown.
7. **Timeline entries** (About). The brief only gives 2010 Inception and 2020 Online.
8. **News items** (4 on home, list on Events).
9. **Event dates, venues and pages** for upcoming and past events.
10. **Resource files** (reports, brochure, PPT, branding kit, e-books, videos, courses, eco-games, merch, books).
11. **Network profiles** (MFMV, artists, athletes, ambassadors, advisors): names, roles, photos.
12. **Award bios / winners**, and confirmation of which categories sit under which award group.
13. **CSR details** for the Join Us page.
14. **Analytics choice** (Umami or Plausible) and the site ID.
15. **Legal review** of `privacy-policy.html` and `terms.html`. Both are marked as drafts.

## Brief inconsistencies / open questions
- The home impact figure says **3.7+ million** saplings; the Programs copy says **3.6 million**. Both are kept as written. Which is correct?
- The home figure says **8,51,000+** Energy Literacy completions; Programs says **8,50,000**. Which is correct?
- One Clean Energy sentence in the document stops at "The programme". The fragment is left out until the full sentence is supplied.

## Design notes and deliberate decisions
- **Brand:** follows the EARTHDAY.ORG toolkit: Oxford Blue #07074E, Blaze Orange #F37321 (CTAs), Steel Blue, Light Sea Green, Chrome Yellow, Anti-Flash White; Montserrat; uppercase, letter-spaced headings; square corners.
- **Deviation:** one serif, *Cormorant Garamond*, is used **only** for pull quotes, the Trustees note and testimonials, to give the "heritage meets modern" feel the brief asked for. To remove it, delete the Cormorant font-face and `--serif` rules in `style.css`.
- **Contrast:** orange buttons use **navy text** (6.3:1). White on orange is only 2.9:1, which fails WCAG AA.
- **No hreflang:** the site has a single language (English, `lang="en-IN"`). Add hreflang if a Hindi version is created.
- **No cookie banner:** the site sets no cookies. Fonts are self-hosted, analytics are cookieless (Umami/Plausible, still disabled), and YouTube/Instagram load only after the visitor clicks (facade). Revisit if any cookie-setting tool is added.
- **HTTPS** is provided by the host (Netlify, Let's Encrypt). `_headers` adds HSTS and `upgrade-insecure-requests`.
- **CSP** (`_headers`) is strict: `script-src 'self'`, no inline scripts. When analytics is enabled, add its host to `script-src` and `connect-src` (e.g. `https://cloud.umami.is` or `https://plausible.io`). If reCAPTCHA is enabled on Netlify Forms, add `https://www.google.com https://www.gstatic.com` to `script-src` and `frame-src`. Instructions are in the comments in `_headers`.
- **Analytics hooks:** `main.js` sends events (CTA clicks, form submits, tel/mailto taps, outbound social and outbound links) through `window.umami` or `window.plausible` if one is present. Until then it does nothing. There are no ad pixels and no GTM.
- **Forms:** Netlify Forms (`data-netlify`, honeypot `bot-field`, POST to `/thank-you`). JS validation is added on top of native HTML validation, so the forms also work without JS. Set the notification email in Netlify → Forms.

## Other files
- `IMAGE_CREDITS.md`: photo sources and licences, with the Drive filename to use for each replacement.
- `QA_REPORT.md`: test results and TODOs.
- `qa/`: Lighthouse reports, axe/console JSON, HTML validation and link-check output.
- `screenshots/`: desktop (1280) and mobile (390) full-page screenshots of every page.
- `_redirects` / `netlify.toml`: 301 examples (TODO: map the real old URLs) and 404 rules for the QA folders.
