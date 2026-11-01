# Client Brief Coverage Audit — Earth Day Network India

**Date:** 01 November 2026  
**Source Document:** `20261016_Updated_Final_Website_Text_docx.pdf` (Client Brief)  
**Target Build:** Earth Day Network India static site generator (`_src/`)  
**Design Reference to Port:** `https://sonudevhub.github.io/earth/` / `https://github.com/rishi-noob/earthdayorg.git`

---

## 1. Global Navigation, Header & Branding Spec

| Brief Instruction | Implementation Location | Status | Notes & Verification |
|---|---|---|---|
| **Logo acts as Home button** | `_src/common.py` (`header()`), `assets/logos/logo-navy-*.png` | **IMPLEMENTED** | `<a class="brand" href="index.html">` with official mark and alt text linking directly to Home. |
| **Top Bar Menu:** About \| Program \| Network \| Awards \| Events \| Resources \| Join Us \| Contact | `_src/common.py` (`NAV`) | **IMPLEMENTED** | Exact 8 menu items in identical order. |
| **Dropdown for all except About** | `_src/common.py` (`NAV`, `header()`) | **IMPLEMENTED** | About is a direct single page link; all others have accessible disclosure button dropdowns with keyboard arrow support. |
| **About:** Single page (No dropdown) | `_src/common.py` (`NAV`) | **IMPLEMENTED** | Links directly to `about.html`. |
| **Program dropdown:** EDO Theme, Youth, Education, Agriculture, Climate Change (Energy/Community/Biodiversity), Women, Cleanup & Plastics, Canopy, Fashion | `_src/common.py` (`NAV`) | **IMPLEMENTED** | Dropdown links point to matching anchors in `programs.html` (`#edo-theme`, `#youth`, `#education`, `#agriculture`, `#climate-change`, `#women`, `#cleanup`, `#canopy`, `#fashion`). |
| **Network dropdown:** MFMV, Artists, Athletes, Ambassadors, Advisors, All our partners photo | `_src/common.py` (`NAV`) | **IMPLEMENTED** | Links to anchors in `network.html` (`#mfmv`, `#artists`, `#athletes`, `#ambassadors`, `#advisors`, `#partners`). |
| **Awards dropdown:** Energy, Institutional, Group, Geographical, Individual | `_src/common.py` (`NAV`) | **IMPLEMENTED** | Links to anchors in `awards.html` (`#energy`, `#institutional`, `#group`, `#geographical`, `#individual`). |
| **Events dropdown:** Upcoming Events, Ongoing Events, Major Past Events, EDN in News | `_src/common.py` (`NAV`) | **IMPLEMENTED** | Links to anchors in `events.html` (`#upcoming`, `#ongoing`, `#past`, `#news`). |
| **Resources dropdown:** Reports, Brochure, Branding, Ebooks, Videos, Courses - Energy Literacy | `_src/common.py` (`NAV`) | **IMPLEMENTED** | Links to anchors in `resources.html` (`#reports`, `#brochure`, `#branding`, `#ebooks`, `#videos`, `#courses`). |
| **Join us dropdown:** CSR Focus, Partner, Volunteer, Project Interest Forms | `_src/common.py` (`NAV`) | **IMPLEMENTED** | Links to anchors in `join-us.html` (`#csr`, `#partner`, `#volunteer`, `#forms`). |
| **Contact:** When clicked, scrolls to bottom bar, no separate page | `_src/common.py` (`header()`) | **IMPLEMENTED** | `<a class="top" href="#contact">Contact</a>` smoothly scrolls to the footer on every page. |
| **Social media floating bar throughout (YT, IG, LIn, X, FB)** | `_src/common.py` (`header()`), `_src/style.css` (`.social-float`) | **IMPLEMENTED** | Floating fixed bar containing YouTube, Instagram, LinkedIn, X, and Facebook SVGs present across all pages. |
| **Registrations line in bottom bar:** NITI Aayog NGO Darpan, 12A, CSR-1 | `_src/common.py` (`footer()`) | **IMPLEMENTED** | Explicit badges and verbatim text: NITI Aayog NGO Darpan, 12A under Income Tax Act, CSR-1 from MCA. |
| **Theme logo slot in bottom bar** | `_src/common.py` (`footer()`) | **IMPLEMENTED** | Dedicated `.theme-logo-slot` alongside the white brand logo linking to the 2027 global theme. |

---

## 2. Home Page (`index.html`)

| Brief Instruction | Implementation Location | Status | Notes & Verification |
|---|---|---|---|
| **4 Home page Photos (Named Home Page Picture 1/2/3/4)**: 1. Canopy Project, 2. Youth, 3. Women Farmers, 4. Cleanup | `_src/home.py` (`SLIDES`), `_src/img/` | **IMPLEMENTED** | Placeholder photos mapped to filenames in `IMAGE_CREDITS.md` with explicit replacement instructions. |
| **Hero headline & copy:** "EARTH DAY, EVERY DAY / Educate. Inspire. Mobilise. Act—for Our Planet / Every act counts. Together, we can build a greener, healthier and more sustainable Earth." | `_src/home.py` (`hero`) | **IMPLEMENTED** | Exact brief text in uppercase letter-spaced H1, kicker and lead paragraphs. |
| **Two Hero buttons:** "Explore Our Work" \| "Partner With Us" | `_src/home.py` (`hero`) | **IMPLEMENTED** | Primary orange CTA with navy text (AA compliant) and ghost button linking to `programs.html` and `join-us.html#partner`. |
| **Ported Hero Video:** Looping, muted, autoplay, playsinline video as slide 0, toggled via `HERO_VIDEO` in `common.py` | `_src/home.py`, `_src/common.py`, `assets/video/` | **IMPLEMENTED** | Calm India-relevant video (`hero.mp4`, `hero.webm`, mobile versions) with Oxford Blue overlay. |
| **White small space line** | `_src/home.py` (`<div class="white-line">`) | **IMPLEMENTED** | Styled horizontal white dividing rule. |
| **Centred intro paragraph:** "Earth Day Network India is a registered trust inspired by the global EARTHDAY.ORG movement. We work with people and organisations across India toward a more sustainable future." | `_src/home.py` (`.intro`) | **IMPLEMENTED** | Centred typography with decorative brand star ornament. |
| **Ported 3D Earth Globe ("Our global movement"):** Three.js interactive globe with markers, fly-to-camera, filter chips, panel | `_src/home.py`, `assets/vendor/three/`, `assets/earth/` | **IMPLEMENTED** | Placed directly after hero intro. Pinpoints places named in brief (Delhi, Mumbai, Ganga, Dal Lake, Saklana, Lalitpur, Anantapur, Sundarbans, D.C.). Programme group legend bar (`All`, `Forests & Canopy`, `Cleanups`, `Education`, `Agriculture`, `Energy`, `Youth`) and interactive place list directory. |
| **"A Glimpse of Our Impact Across India"**: All 7 figures counting up (5,00,000+ farmers, 3.0+ million saplings, 4,50,000+ fruit trees, 20,000+ rural women, 8,51,000+ Energy Literacy, 1,00,000+ schools, 4,50,000+ young people) | `_src/home.py` (`IMPACT`), `_src/main.js` (`countUp`) | **IMPLEMENTED** | Formatted using Indian digit grouping (`en-IN`) counting up with nanosecond ticker easing. |
| **Ported "Guiding Our Path" statement band:** Oversized statement with two offset photos | `_src/home.py`, `_src/style.css` | **IMPLEMENTED** | Brief mission lines: "Educate. Inspire. Mobilise. Act—for Our Planet" and "Earth Day is celebrated once a year, but our responsibility to the Earth is every day." |
| **Awardees block:** 10–12 headshots on the left, "400+ Star Awards and recognitions presented ..." on the right | `_src/home.py` (`#awardees`) | **IMPLEMENTED** | 12 monogram/silhouette headshot tiles on left, large 400+ stat numeral and full brief copy on right. |
| **Show Panel: Top 5 photos, square size, border to border** | `_src/home.py` (`.strip`) | **IMPLEMENTED** | 5 border-to-border show panel photos mapped to `show-panel-1.jpg` through `5.jpg`. |
| **Theme Panel: Landscape panel connecting to 2027 theme on global website** | `_src/home.py` (`#theme`) | **IMPLEMENTED** | Duotone image card linking to `https://www.earthday.org/earth-day-2027/` with external link icon. |
| **Ported Initiatives List:** Numbered rows with hover image preview | `_src/home.py`, `_src/style.css` | **IMPLEMENTED** | 8 brief programme areas with 15-30 word descriptions and links to `programs.html` anchors. |
| **Events section small:** 3 small boxes (Nominations are open for……, Apply for……, Go to events) | `_src/home.py` (`#events-preview`) | **IMPLEMENTED** | Three distinct cards with placeholder markers and direct anchor routes. |
| **Ported Featured Projects Slider:** Full-height panels with swipe, arrows, progress, stats | `_src/home.py`, `_src/style.css`, `_src/main.js` | **IMPLEMENTED** | Brief facts only: Canopy Project, Healthy Energy, Morning Assembly, Cleanups, Young Climate Champions, MFMV. |
| **Major Programs horizontal slider:** 6–8 pic+text boxes that slide to reveal text | `_src/home.py` (`.carousel-track`) | **IMPLEMENTED** | 8 cards connected to Programs anchors with scroll buttons and swipe. |
| **Ported Network Preview ("Leadership & voices"):** Ambassadors, Advisors, Canopy Experts preview | `_src/home.py`, `_src/style.css` | **IMPLEMENTED** | Monogram placeholder tiles linking to `network.html` anchors. |
| **Partners: Slow marquee of named partners + big logo picture slot** | `_src/home.py` (`#partners-home`), `_src/style.css` | **IMPLEMENTED** | Text marquee of 18 named organisations from the brief above the combined logo image slot. |
| **Live YT + Insta Box** | `_src/home.py` (`#live`) | **IMPLEMENTED** | Dual-card click-to-load embeds (zero cookies/third-party calls prior to user click). |
| **2 sections half: 1 side Map (Dynamic) + 1 side News** | `_src/home.py` (`#map-news`) | **IMPLEMENTED** | Left: Leaflet interactive map populated with verified coordinates from brief. Right: 4 news list items. |
| **Quotes and testimonials (in place of ambassadors)** | `_src/home.py` (`#quotes`) | **IMPLEMENTED** | Testimonials slider with Cormorant Garamond typography, 44px navigation buttons, dot indicators, touch swipe and keyboard arrows. |

---

## 3. About Page (`about.html`)

| Brief Instruction | Implementation Location | Status | Notes & Verification |
|---|---|---|---|
| **About us intro:** Earth Day, Every Day / Educate. Inspire. Mobilise. Act—for Our Planet / Registered trust intro / 2 paragraphs on programmes and resilience | `_src/about.py` (`#who-h`) | **IMPLEMENTED** | Verbatim copy from the brief. |
| **Our Approach flow:** Education → Awareness → Engagement → Partnerships → Action → Recognition | `_src/about.py` (`#approach`) | **IMPLEMENTED** | 6-step flow with arrows. |
| **A Call to Action (8 points):** Adopt LiFE, cleaner energies, minimise plastic, reduce pollution, expand canopy, green economy, climate education, natural farming | `_src/about.py` (`#call-to-action`) | **IMPLEMENTED** | Complete 8-point action checklist. |
| **Note from the Trustees:** Full text (5 paragraphs + sign-off) | `_src/about.py` (`#trustees`) | **IMPLEMENTED** | Full letter styled in Cormorant Garamond with Trustees signature. |
| **Timeline: Major events (2010 Inception, 2015 -, 2020 Online, etc. with placeholders)** | `_src/about.py` (`#timeline`) | **IMPLEMENTED** | 4 timeline cards with archival image frames and milestone labels. |
| **Gallery** | `_src/about.py` (`#gallery`) | **IMPLEMENTED** | 8 responsive photos in alternating shapes. |
| **Ported FAQ Accordion (Short version):** Key questions answered from brief | `_src/about.py` | **PORTING** | Adding compact FAQ on trust status, registrations, and 2027 theme. |

---

## 4. Programs Page (`programs.html`)

| Brief Instruction | Implementation Location | Status | Notes & Verification |
|---|---|---|---|
| **Main Picture + Intro:** "Turning Global Priorities into Action in India..." | `_src/programs.py` (`page_hero`) | **IMPLEMENTED** | Verbatim headline and lead text with full banner. |
| **Alternating pattern of photo + text (left-right)** | `_src/programs.py` (`.prog`, `.flip`) | **IMPLEMENTED** | Responsive alternating grid flipping on desktop. |
| **1. Sustainable Food and Agriculture:** Food for Our Planet 2027/2028, Farmers for Earth, First-Gen Women Farmers | `_src/programs.py` (`#agriculture`) | **IMPLEMENTED** | Verbatim brief text. |
| **2. The Canopy Project™:** 3.6 million saplings, mangroves, fruit tree saplings in Saklana, Lalitpur, Anantapur | `_src/programs.py` (`#canopy`) | **IMPLEMENTED** | Verbatim brief text. |
| **3. Clean Energy and Climate-Resilient Communities:** Healthy Energy, 20,000+ women, 15 states, Energy Swaraj Foundation, Prof. Chetan Singh Solanki (68,000 km, 1,600 talks, 4,00,000 citizens, 8,50,000 completions), Star Campus Awards | `_src/programs.py` (`#energy`) | **IMPLEMENTED** | Verbatim brief text with visible flag for incomplete brief sentence. |
| **4. Environmental and Climate Education:** Morning Assembly (1,00,000 schools), Earth Reel, Earth Murals, Climate Clock assemblies, Eco-Comics, teacher-training | `_src/programs.py` (`#education`) | **IMPLEMENTED** | Verbatim brief text. |
| **5. Empowering Youth:** 382 million youth, Young Climate Champions (nearly 4,50,000 youth in 2025-26, JSW-Times of India Earth Care Awards) | `_src/programs.py` (`#youth`) | **IMPLEMENTED** | Verbatim brief text. |
| **6. My Future My Voice:** 300+ Youth Ambassadors, 125 countries, Diana Award, Queen's Young Leaders, Indira Gandhi Award | `_src/programs.py` (`#my-future-my-voice`) | **IMPLEMENTED** | Verbatim brief text. |
| **7. Young Earthpreneurs Awards:** Launched 2022, college student startups | `_src/programs.py` (`#young-earthpreneurs`) | **IMPLEMENTED** | Verbatim brief text. |
| **8. Youth Innovation and Green Livelihoods:** Rising Stars, green-enterprise | `_src/programs.py` (`#youth-innovation`) | **IMPLEMENTED** | Verbatim brief text. |
| **9. Cleanups and Circularity:** Great Global Cleanup, Ganga, Juhu Beach, Dal Lake, Mission LiFE, MCD Nivaran Dadi mascot, Bags for Earth, school e-waste & recycling | `_src/programs.py` (`#cleanup`) | **IMPLEMENTED** | Verbatim brief text. |
| **10. Faith Sites:** 147.5 million outreach | `_src/programs.py` (`#faith-sites`) | **IMPLEMENTED** | Verbatim brief text. |
| **11. Earth Day:** Since 1970, April 22, > 1 billion inspired in India alone | `_src/programs.py` (`#earth-day`) | **IMPLEMENTED** | Dedicated navy highlight panel. |
| **12. Climate Change: Energy, Community and Biodiversity** | `_src/programs.py` (`#climate-change`) | **IMPLEMENTED** | Verbatim brief text. |
| **13. Women:** First-time farm managers, Canopy Project mangroves, WAGE campaign | `_src/programs.py` (`#women`) | **IMPLEMENTED** | Verbatim brief text. |
| **14. Sustainable Fashion:** Circular choices, youth, designers | `_src/programs.py` (`#fashion`) | **IMPLEMENTED** | Verbatim brief text. |
| **Partners Logo slot + Gallery** | `_src/programs.py` (`#partners`, `#gallery`) | **IMPLEMENTED** | Dedicated sections. |
| **Anchors for all dropdown items:** `#edo-theme`, `#youth`, `#education`, `#agriculture`, `#climate-change`, `#women`, `#cleanup`, `#canopy`, `#fashion` | `_src/programs.py` | **IMPLEMENTED** | All 9 anchor IDs defined and tested. |

---

## 5. Network Page (`network.html`)

| Brief Instruction | Implementation Location | Status | Notes & Verification |
|---|---|---|---|
| **Our Ambassadors:** Verbatim text from brief | `_src/inner.py` (`#ambassadors`) | **IMPLEMENTED** | Text from brief with placeholder profile cards. |
| **Our Advisors:** Verbatim text from brief | `_src/inner.py` (`#advisors`) | **IMPLEMENTED** | Text from brief with placeholder profile cards. |
| **Our Experts for the Canopy Project:** Verbatim text from brief | `_src/inner.py` (`#canopy-experts`) | **IMPLEMENTED** | Text from brief with placeholder profile cards. |
| **Sections/Anchors:** `#mfmv`, `#artists`, `#athletes`, `#ambassadors`, `#advisors`, `#partners` | `_src/inner.py` | **IMPLEMENTED** | All 6 section anchors implemented. |
| **All our partners photo** | `_src/inner.py` (`#partners`) | **IMPLEMENTED** | Dedicated partner logo slot. |

---

## 6. Awards Page (`awards.html`)

| Brief Instruction | Implementation Location | Status | Notes & Verification |
|---|---|---|---|
| **AWARDS AND RECOGNITIONS intro:** Verbatim text from brief | `_src/inner.py` (`#overview`) | **IMPLEMENTED** | Text from brief. |
| **9 Award Descriptions:** Earth Day Heroes, Star Municipal Leaders, Star Women's Group, Earth Day Rising Stars, Earth Day Stars, Village Awards, Clean Cooking Stars, Litter Free India Champions, Star Campus Awards | `_src/inner.py` (`#our-awards`) | **IMPLEMENTED** | All 9 award descriptions verbatim. |
| **14 Award Categories/Tiles:** OPOP Stars, Earth Day Heroes, Municipality, Women, Rising, Star, Villages, YEA, Clean Cooking Star, LFIC, Panchayats, Faith Sites, Special Awards, Star Campus | `_src/inner.py` (`#all-awards`) | **IMPLEMENTED** | Reference-style grid with logo slot, bio placeholder, and register link. |
| **Dropdown Anchors:** `#energy`, `#institutional`, `#group`, `#geographical`, `#individual` | `_src/inner.py` (`#browse`) | **IMPLEMENTED** | Group tiles mapped to all 5 dropdown targets. |

---

## 7. Events Page (`events.html`)

| Brief Instruction | Implementation Location | Status | Notes & Verification |
|---|---|---|---|
| **Upcoming Events:** 2027 ED, Cleanup Day, YCC | `_src/inner.py` (`#upcoming`) | **IMPLEMENTED** | Dated event rows with Event JSON-LD schema. |
| **Ongoing Events:** Young Climate Champions (YCC) | `_src/inner.py` (`#ongoing`) | **IMPLEMENTED** | Highlight band with active live status pill. |
| **Major Past Events:** Awards in Mumbai, Save the Beach, Sundarbans | `_src/inner.py` (`#past`) | **IMPLEMENTED** | 3 past event cards with links and image placeholders. |
| **EDN in News** | `_src/inner.py` (`#news`) | **IMPLEMENTED** | News coverage list items. |
| **Designed layout with filter tabs:** Upcoming / Ongoing / Past / News | `_src/inner.py`, `_src/style.css` | **PORTING** | Enhancing with filter tabs matching reference styling. |

---

## 8. Resources Page (`resources.html`)

| Brief Instruction | Implementation Location | Status | Notes & Verification |
|---|---|---|---|
| **Resource categories:** Reports, Brochure, PPT, Branding Usage with Guidelines, Ebooks, Videos, Courses - Energy Literacy, Eco games, Merchs, Link to our books | `_src/inner.py` (`resources()`) | **IMPLEMENTED** | All 10 categories with custom line SVGs. |
| **Featured Course block:** Energy Literacy | `_src/inner.py` | **IMPLEMENTED** | Highlight banner for Energy Swaraj Foundation course. |
| **Designed layout with type icons & filterability** | `_src/inner.py`, `_src/style.css` | **PORTING** | Type filter tabs and clean badge layout. |

---

## 9. Join Us Page (`join-us.html`)

| Brief Instruction | Implementation Location | Status | Notes & Verification |
|---|---|---|---|
| **4 Path Blocks:** CSR Focus, Partner (Common Link), Other forms (e.g., Plantation), Volunteer (Form links) | `_src/inner.py` (`.join-paths`) | **IMPLEMENTED** | 4 interactive pathway cards. |
| **CALL TO ACTION text:** "Every act counts. Collective action multiplies its impact. Partner With Us..." | `_src/inner.py` (`#cta`) | **IMPLEMENTED** | Verbatim text from brief. |
| **Partner With Us full text:** 130+ organisations named (MoEFCC, UNICEF, UNESCO-MGIEP, NSS, NCC, WWF, TERI, CEE, Tata Power, ITC, UPS, BBC Media Action, United Way, SEWA, Energy Swaraj Foundation, Oxford Said, KIIT, BHU) | `_src/inner.py` (`#partner`) | **IMPLEMENTED** | Complete brief text and partner list. |
| **Netlify Forms:** Volunteer and Project Interest Forms | `_src/inner.py` (`#volunteer`, `#forms`) | **IMPLEMENTED** | Accessible, validated Netlify forms with honeypot spam protection. |
| **Ported FAQ Accordion:** Comprehensive brief Q&A + FAQPage JSON-LD | `_src/inner.py`, `_src/common.py` | **PORTING** | Adding accordion answering all brief questions with schema. |

---

## 10. SEO & Keyword Coverage

| Keyword | Target Placement | Verified Placement Status |
|---|---|---|
| **Earth Day Network India** | Titles, headings, footer, meta, alt | Verified across all pages |
| **EARTHDAY.ORG India** | Header brand, tagline, schema, meta | Verified across all pages |
| **Earth Day India** | Hero H1, event titles, meta descriptions | Verified across all pages |
| **environmental organisation in India** | About H1, meta descriptions, image alts | Verified across all pages |
| **environmental NGO in India** | Home intro eyebrow, meta descriptions | Verified across all pages |
| **environmental nonprofit India** | Join Us intro, footer, meta | Verified across all pages |
| **climate education India** | Programs H1, resources title, meta | Verified across all pages |
| **environmental education India** | Programs education section, meta | Verified across all pages |
| **climate action organisation** | Climate change program section, meta | Verified across all pages |
| **green initiatives India** | Programs, awards, meta | Verified across all pages |
| **Earth Day** | Throughout content, events, footer | Verified across all pages |
| **Earth Day Every Day** | Tagline, hero H1, footer copyright | Verified across all pages |

