"""Shared config + layout for the Earth Day Network India static site generator.
Single place to change: ORG (organisation name), BASE_URL (TODO confirm domain), SOCIAL, CONTACT, ANALYTICS."""
import os, json, html, hashlib
from PIL import Image

ORG = "Earth Day Network India"
BASE_URL = "https://www.earthdayindia.org"   # TODO: confirm the production domain before launch
GLOBAL_THEME_URL = "https://www.earthday.org/earth-day-2027/"
HERO_VIDEO = True
# TODO: client to supply official profile URLs. Empty = placeholder link (no outbound URL is invented).
SOCIAL = {"youtube": "", "instagram": "", "linkedin": "", "x": "", "facebook": ""}
# TODO: client to supply. Shown as clearly marked placeholders; never invented.
CONTACT = {"address": "", "email": "", "phone": ""}
# Embeds (click-to-load). TODO: client to supply a YouTube video/live ID and an Instagram post URL.
YOUTUBE_ID = ""
INSTAGRAM_POST = ""

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_src")
e = html.escape
ASSETS = {}   # filled by build.py: {"css": "assets/css/style.<hash>.min.css", "js": ...}

NAV = [
 ("About","about.html",[]),
 ("Program","programs.html",[("EDO Theme","edo-theme"),("Youth","youth"),("Education","education"),("Agriculture","agriculture"),("Climate Change (Energy/Community/Biodiversity)","climate-change"),("Women","women"),("Cleanup & Plastics","cleanup"),("Canopy","canopy"),("Fashion","fashion")]),
 ("Network","network.html",[("MFMV","mfmv"),("Artists","artists"),("Athletes","athletes"),("Ambassadors","ambassadors"),("Advisors","advisors"),("All our partners photo","partners")]),
 ("Awards","awards.html",[("Energy","energy"),("Institutional","institutional"),("Group","group"),("Geographical","geographical"),("Individual","individual")]),
 ("Events","events.html",[("Upcoming Events","upcoming"),("Ongoing Events","ongoing"),("Major Past Events","past"),("EDN in News","news")]),
 ("Resources","resources.html",[("Reports","reports"),("Brochure","brochure"),("Branding","branding"),("Ebooks","ebooks"),("Videos","videos"),("Courses - Energy Literacy","courses")]),
 ("Join Us","join-us.html",[("CSR Focus","csr"),("Partner","partner"),("Volunteer","volunteer"),("Project Interest Forms","forms")]),
]

# ---------- Icons (hand-drawn line SVGs, 24px grid) ----------
_I = {
 "arrow-r":'<path d="M4 12h15M13 6l6 6-6 6"/>', "arrow-l":'<path d="M20 12H5M11 6l-6 6 6 6"/>', "chev-d":'<path d="M5 9l7 7 7-7"/>',
 "pause":'<path d="M8 5v14M16 5v14"/>', "play":'<path d="M7 5l12 7-12 7z"/>', "ext":'<path d="M14 4h6v6M20 4l-9 9M18 14v6H4V6h6"/>',
 "doc":'<path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4M9 12h7M9 16h7"/>',
 "fold":'<path d="M3 5l6-2 6 2 6-2v16l-6 2-6-2-6 2z"/><path d="M9 3v16M15 5v16"/>',
 "slides":'<path d="M3 4h18v12H3z"/><path d="M12 16v4M8 20h8M7 12l3-3 2 2 4-4"/>',
 "brand":'<circle cx="12" cy="12" r="8.5"/><path d="M12 3.5v17M3.5 12h17"/><circle cx="12" cy="12" r="3"/>',
 "book":'<path d="M4 5c3-1.5 6-1.5 8 0 2-1.5 5-1.5 8 0v14c-3-1.5-6-1.5-8 0-2-1.5-5-1.5-8 0z"/><path d="M12 5v14"/>',
 "video":'<path d="M3 6h13v12H3z"/><path d="M16 10l5-3v10l-5-3"/>',
 "cap":'<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5M22 9v6"/>',
 "game":'<path d="M6 8h12a4 4 0 0 1 0 8c-2 0-3-2-6-2s-4 2-6 2a4 4 0 0 1 0-8z"/><path d="M8 10v4M6 12h4M16 11h.01M18 13h.01"/>',
 "bag":'<path d="M5 8h14l-1 13H6z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>',
 "shelf":'<path d="M4 20h16M6 20V6h3v14M10 20V4h3v16M14.5 20l2-13 3 .5-2 12.5"/>',
 "leaf":'<path d="M5 19c0-9 6-14 15-14 0 9-5 15-14 15"/><path d="M5 19l8-8"/>',
 "hand":'<path d="M7 11V5.5a1.5 1.5 0 0 1 3 0V11M10 10V4.5a1.5 1.5 0 0 1 3 0V10M13 10.5V6a1.5 1.5 0 0 1 3 0v7M7 11a1.5 1.5 0 0 0-3 0v2a8 8 0 0 0 8 8h1a6 6 0 0 0 6-6v-4a1.5 1.5 0 0 0-3 0"/>',
 "link":'<path d="M10 14a4 4 0 0 0 6 0l3-3a4 4 0 0 0-6-6l-1 1M14 10a4 4 0 0 0-6 0l-3 3a4 4 0 0 0 6 6l1-1"/>',
 "pen":'<path d="M4 20l4-1 11-11-3-3L5 16z"/><path d="M14 6l3 3"/>',
}
def icon(name, cls="icon"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{_I[name]}</svg>'
ARROW = icon("arrow-r")
MEDAL = '<svg viewBox="0 0 72 72" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="36" cy="40" r="22"/><circle cx="36" cy="40" r="17" stroke-dasharray="2 3"/><path d="M24 4l8 16M48 4l-8 16M28 4h16"/><path d="M36 30l3 6.5 7 .8-5.2 4.8 1.4 7-6.2-3.5-6.2 3.5 1.4-7-5.2-4.8 7-.8z"/></g></svg>'

SOCIAL_SVG = {
 "youtube":'<path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.7 15.1V8.9l5.8 3.1-5.8 3.1z"/>',
 "instagram":'<path d="M12 2.2c3.2 0 3.6 0 4.8.1 3.3.1 4.8 1.7 4.9 4.9.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 3.2-1.7 4.8-4.9 4.9-1.3.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-3.3-.1-4.8-1.7-4.9-4.9C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8C2.4 3.9 3.9 2.4 7.2 2.3 8.4 2.2 8.8 2.2 12 2.2zM12 0C8.7 0 8.3 0 7.1.1 2.7.3.3 2.7.1 7.1 0 8.3 0 8.7 0 12s0 3.7.1 4.9c.2 4.4 2.6 6.8 7 7 1.2.1 1.6.1 4.9.1s3.7 0 4.9-.1c4.4-.2 6.8-2.6 7-7 .1-1.2.1-1.6.1-4.9s0-3.7-.1-4.9c-.2-4.4-2.6-6.8-7-7C15.7 0 15.3 0 12 0zm0 5.8a6.2 6.2 0 1 0 0 12.4 6.2 6.2 0 0 0 0-12.4zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.4-11.8a1.4 1.4 0 1 0 0 2.9 1.4 1.4 0 0 0 0-2.9z"/>',
 "linkedin":'<path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.75h4V21H3zM9.5 9.75h3.8v1.6h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6V21h-4v-5c0-1.2 0-2.8-1.7-2.8s-2 1.3-2 2.7V21h-4z"/>',
 "x":'<path d="M18.2 2.25h3.4l-7.4 8.5 8.7 11.5h-6.8l-5.3-7-6.1 7H1.3l7.9-9.1L.8 2.25h7l4.8 6.4zm-1.2 18h1.9L7 4.2H5z"/>',
 "facebook":'<path d="M24 12a12 12 0 1 0-13.9 11.9v-8.4h-3V12h3V9.4c0-3 1.8-4.7 4.5-4.7 1.3 0 2.7.2 2.7.2v3h-1.5c-1.5 0-2 .9-2 1.9V12h3.4l-.5 3.5h-2.9v8.4A12 12 0 0 0 24 12z"/>',
}
SOCIAL_NAMES = {"youtube":"YouTube","instagram":"Instagram","linkedin":"LinkedIn","x":"X","facebook":"Facebook"}
SILHOUETTE = '<svg viewBox="0 0 100 100" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false"><rect width="100" height="100" fill="#cfc8b8"/><circle cx="50" cy="40" r="17" fill="#a89f8c"/><path d="M18 100c2-22 15-34 32-34s30 12 32 34z" fill="#a89f8c"/></svg>'
STAR = '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0l1.8 6.2L16 8l-6.2 1.8L8 16l-1.8-6.2L0 8l6.2-1.8z"/></svg>'

def social_link(k):
    url = SOCIAL.get(k) or ""
    name = SOCIAL_NAMES[k]
    if url:
        return f'<a href="{e(url)}" data-social="{k}" target="_blank" rel="noopener me" aria-label="{ORG} on {name} (opens in a new tab)"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">{SOCIAL_SVG[k]}</svg></a>'
    return f'<a href="#" data-social="{k}" aria-label="{ORG} on {name} (link coming soon)" title="{name} — link coming soon"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">{SOCIAL_SVG[k]}</svg></a>'

def contact_value(k, label):
    v = CONTACT.get(k)
    if not v: return f'<span class="tag">TODO</span> {label} to be supplied'
    if k == "email": return f'<a href="mailto:{e(v)}" data-track="Email tap">{e(v)}</a>'
    if k == "phone": return f'<a href="tel:{e(v.replace(" ",""))}" data-track="Phone tap">{e(v)}</a>'
    return e(v)

# ---------- Responsive images ----------
WIDTHS = [480, 800, 1200, 1800]
_dims = {}
def src_dims(name):
    if name not in _dims:
        with Image.open(os.path.join(SRC, "img", name)) as im: _dims[name] = im.size
    return _dims[name]
def variants(name):
    w0, h0 = src_dims(name)
    ws = [w for w in WIDTHS if w < w0] + [min(w0, WIDTHS[-1])]
    return sorted(set(ws)), w0, h0
def picture(name, alt, sizes="100vw", cls="", eager=False, img_cls=""):
    ws, w0, h0 = variants(name)
    base = os.path.splitext(name)[0]
    ss = lambda ext: ", ".join(f"assets/img/{base}-{w}.{ext} {w}w" for w in ws)
    wmax = ws[-1]; hmax = round(h0 * wmax / w0)
    mid = [w for w in ws if w >= 800]; fb = mid[0] if mid else ws[-1]
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ''
    ic = f' class="{img_cls}"' if img_cls else ''
    return (f'<picture{c}><source type="image/avif" srcset="{ss("avif")}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{ss("webp")}" sizes="{sizes}">'
            f'<img{ic} src="assets/img/{base}-{fb}.jpg" srcset="{ss("jpg")}" sizes="{sizes}" width="{wmax}" height="{hmax}" alt="{e(alt)}" {load}></picture>')

# ---------- Structured data ----------
def org_ld():
    d = {"@type": "NGO", "@id": BASE_URL + "/#organization", "name": ORG, "alternateName": "EARTHDAY.ORG India",
         "url": BASE_URL + "/", "logo": BASE_URL + "/assets/logos/logo-navy-512.png",
         "description": f"{ORG} is a registered trust inspired by the global EARTHDAY.ORG movement.",
         "areaServed": {"@type": "Country", "name": "India"},
         "sameAs": [v for v in SOCIAL.values() if v],
         "email": CONTACT["email"] or "TODO: official email to be supplied",
         "telephone": CONTACT["phone"] or "TODO: official phone to be supplied",
         "address": {"@type": "PostalAddress", "streetAddress": CONTACT["address"] or "TODO: registered address to be supplied", "addressCountry": "IN"}}
    return d
def website_ld():
    return {"@type": "WebSite", "@id": BASE_URL + "/#website", "url": BASE_URL + "/", "name": ORG, "inLanguage": "en-IN", "publisher": {"@id": BASE_URL + "/#organization"}}
def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": BASE_URL + "/" + (u if u != "index.html" else "")} for i, (n, u) in enumerate(items)]}

def faq_ld(faqs):
    return [{"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}]

def ld_block(extra=None, crumbs=None):
    graph = [org_ld(), website_ld()]
    if crumbs: graph.append(crumbs_ld(crumbs))
    if extra: graph += extra
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":")) + '</script>'

# ---------- Layout ----------
def header(active):
    items = []
    for label, href, subs in NAV:
        act = ' active' if href == active else ''
        cur = ' aria-current="page"' if href == active else ''
        if subs:
            dd = "".join(f'<li><a href="{href}#{a}">{e(t)}</a></li>' for t, a in subs)
            mid = "dd-" + href.split(".")[0]
            items.append(f'<li class="has-dd{act}"><a class="top" href="{href}"{cur}>{e(label)}</a><button class="dd-btn" type="button" aria-expanded="false" aria-controls="{mid}"><span class="sr-only">{e(label)} submenu</span>{icon("chev-d")}</button><ul class="dropdown" id="{mid}">{dd}</ul></li>')
        else:
            items.append(f'<li class="{act.strip()}"><a class="top" href="{href}"{cur}>{e(label)}</a></li>')
    items.append('<li><a class="top" href="#contact">Contact</a></li>')
    return f'''<a class="skip" href="#main">Skip to content</a>
<aside class="utility" aria-label="Tagline"><div class="wrap"><span>Inspired by the global EARTHDAY.ORG movement</span><span class="accent">Earth Day, Every Day</span></div></aside>
<header class="site-header"><div class="wrap header-inner">
<a class="brand" href="index.html"><picture><source type="image/webp" srcset="assets/logos/logo-navy-182.webp 1x, assets/logos/logo-navy-364.webp 2x"><img src="assets/logos/logo-navy-182.png" width="91" height="54" alt="{ORG} logo — home"></picture><span class="brand-text">{ORG}<small>EARTHDAY.ORG India</small></span></a>
<button class="menu-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="site-nav"><span></span><span></span><span></span></button>
<nav class="nav" id="site-nav" aria-label="Main"><ul>{"".join(items)}</ul></nav>
</div></header>
<aside aria-label="Social media"><ul class="social-float">{"".join(f"<li>{social_link(k)}</li>" for k in SOCIAL_SVG)}</ul></aside>'''

def field(fid, name, label, typ="text", req=True, auto="", full=False, extra=""):
    r = ' required aria-required="true"' if req else ''
    star = ' <span class="req" aria-hidden="true">*</span>' if req else ''
    ac = f' autocomplete="{auto}"' if auto else ''
    cls = "field full" if full else "field"
    if typ == "textarea":
        ctl = f'<textarea id="{fid}" name="{name}" rows="4"{r} minlength="10" aria-describedby="{fid}-err"{extra}></textarea>'
    else:
        ctl = f'<input id="{fid}" name="{name}" type="{typ}"{ac}{r} aria-describedby="{fid}-err"{extra}>'
    return f'<div class="{cls}"><label for="{fid}">{label}{star}</label>{ctl}<span class="err" id="{fid}-err" aria-live="polite"></span></div>'

def netlify_form(name, prefix, fields_html, submit, cls="", note=""):
    return f'''<form class="{cls}" name="{name}" method="POST" action="/thank-you" data-netlify="true" netlify-honeypot="bot-field" data-validate>
<input type="hidden" name="form-name" value="{name}">
<p class="hp" aria-hidden="true"><label>Leave this field empty <input type="text" name="bot-field" tabindex="-1" autocomplete="off"></label></p>
<div class="form-grid">{fields_html}
<div class="field full"><label class="check"><input id="{prefix}-consent" name="consent" type="checkbox" value="yes" required aria-describedby="{prefix}-consent-err"> I agree that {ORG} may use these details to respond to me, as described in the <a href="privacy-policy.html">privacy policy</a>.</label><span class="err" id="{prefix}-consent-err" aria-live="polite"></span></div>
<div class="full"><button class="btn" type="submit" data-track="Form submit: {name}">{submit} {ARROW}</button><p class="form-status" role="status" aria-live="polite"></p>{note}</div>
</div></form>'''

def footer():
    ff = field("ft-name","name","Name",auto="name") + field("ft-email","email","Email","email",auto="email") + field("ft-msg","message","Message","textarea",full=True)
    nl_f = field("nl-email","email","Email address","email",auto="email")
    return f'''<footer class="site-footer" id="contact">
<div class="wrap">
<div class="footer-top">
 <div>
  <div class="footer-logos"><a href="index.html" aria-label="{ORG} — Home"><picture><source type="image/webp" srcset="assets/logos/logo-white-216.webp 2x"><img src="assets/logos/logo-white-216.png" width="108" height="64" alt="{ORG} logo" loading="lazy"></picture></a><div class="theme-logo-slot">Theme logo<br>(to be supplied)</div></div>
  <p>{ORG} is a registered trust inspired by the global EARTHDAY.ORG movement.</p>
  <p><a class="link-arrow" href="{GLOBAL_THEME_URL}" target="_blank" rel="noopener">Earth Day 2027 global theme {icon("ext")}<span class="sr-only"> (opens in a new tab)</span></a></p>
  <div class="footer-newsletter">
   <h2>Newsletter</h2>
   <p class="nl-note">Subscribe for updates on environmental actions across India.</p>
   {netlify_form("newsletter","nl",nl_f,"Subscribe",cls="nl-form")}
  </div>
 </div>
 <nav aria-label="Footer"><h2>Explore</h2><ul>
  <li><a href="about.html">About</a></li><li><a href="programs.html">Programs</a></li><li><a href="network.html">Network</a></li><li><a href="awards.html">Awards</a></li><li><a href="events.html">Events</a></li><li><a href="resources.html">Resources</a></li><li><a href="join-us.html">Join Us</a></li></ul></nav>
 <div><h2>Contact</h2><ul class="contact-list">
  <li><b class="cl">Address</b>{contact_value("address","Postal address")}</li>
  <li><b class="cl">Email</b>{contact_value("email","Email")}</li>
  <li><b class="cl">Phone</b>{contact_value("phone","Phone")}</li></ul>
  <ul class="social-row">{"".join(f"<li>{social_link(k)}</li>" for k in SOCIAL_SVG)}</ul>
 </div>
 <div class="footer-form"><h2>Write to us</h2>{netlify_form("contact","ft",ff,"Send message")}</div>
</div>
<div class="registrations">
 <ul class="badges"><li>NGO Darpan</li><li>12A</li><li>CSR-1</li></ul>
 <p class="mb-0">{ORG} also holds NITI Aayog's NGO Darpan registration and 12A registration under the Government of India's Income Tax Act, and CSR-1 Certification from the Ministry of Corporate Affairs.</p>
</div>
<div class="footer-bottom"><span>&copy; <span id="year">2026</span> {ORG}. Earth Day, Every Day.</span><ul><li><a href="privacy-policy.html">Privacy policy</a></li><li><a href="terms.html">Terms of use</a></li><li><a href="credits.html">Photo credits</a></li></ul></div>
</div>
</footer>'''

PAGES = []   # (filename, priority) for sitemap
def page(fn, title, desc, active, body, crumbs=None, extra_ld=None, noindex=False, og_image="assets/og/og-default.jpg", priority="0.8"):
    canon = BASE_URL + "/" + ("" if fn == "index.html" else fn)
    robots = '<meta name="robots" content="noindex, follow">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    og = BASE_URL + "/" + og_image
    preload = '<link rel="preload" href="assets/fonts/Montserrat-900-normal-latin.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="assets/fonts/Montserrat-400-normal-latin.woff2" as="font" type="font/woff2" crossorigin>'
    doc = f'''<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
{'<script>document.write(\'<base href="\' + (location.pathname.indexOf("/earth-day/") !== -1 ? "/earth-day/" : "/") + \'">\');</script>' if fn == "404.html" else ""}
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}
{"" if noindex else f'<link rel="canonical" href="{canon}">'}
<meta name="theme-color" content="#07074E">
<meta property="og:site_name" content="{ORG}"><meta property="og:locale" content="en_IN"><meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{og}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{ORG} — Earth Day, Every Day">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{og}">
<link rel="icon" href="favicon.ico" sizes="32x32"><link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="manifest" href="site.webmanifest">
{preload}
<link rel="stylesheet" href="{ASSETS["css"]}">
<!-- ANALYTICS SLOT (cookieless). Disabled placeholder — enable ONE after launch and add its host to the CSP in _headers:
<script defer src="https://cloud.umami.is/script.js" data-website-id="TODO-UMAMI-ID"></script>
<script defer data-domain="TODO-domain" src="https://plausible.io/js/script.js"></script>
No ad pixels, no GTM. -->
{ld_block(extra_ld, crumbs)}
</head>
<body>
{header(active)}
<main id="main" tabindex="-1">
{body}
</main>
{footer()}
<script src="{ASSETS["js"]}" defer></script>
</body>
</html>
'''
    open(os.path.join(ROOT, fn), "w", encoding="utf-8").write(doc)
    if not noindex: PAGES.append((fn, priority))
    print("wrote", fn)

def eyebrow(t, cls=""): return f'<span class="eyebrow {cls}">{t}</span>'
def tag(t="Placeholder"): return f'<span class="tag">{t}</span>'

def page_hero(crumb, h1, lede, img, alt, file):
    lp = f'<p class="lede">{lede}</p>' if lede else ''
    return f'''<section class="page-hero"><div class="bg">{picture(img, alt, "100vw", eager=True)}</div><div class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li><li><a href="{file}" aria-current="page">{crumb}</a></li></ol></nav><h1>{h1}</h1>{lp}</div></section>'''

def subnav(items, label="On this page"):
    return f'<nav class="subnav" aria-label="{label}"><ul>' + "".join(f'<li><a href="#{a}">{e(t)}</a></li>' for t, a in items) + '</ul></nav>'

def gallery(imgs):
    shapes = ["wide", "", "tall", "", "", "wide", "", ""]
    out = []
    for i, (src, alt) in enumerate(imgs):
        s = shapes[i % len(shapes)]
        sizes = "(max-width:640px) 100vw, 50vw" if s == "wide" else "(max-width:640px) 100vw, 25vw"
        out.append(f'<li class="{s}">{picture(src, alt, sizes)}<span class="cap">Placeholder photo</span></li>')
    return '<ul class="gallery">' + "".join(out) + '</ul>'

GALLERY = [("gallery-1.jpg","Boat among the Sundarbans mangroves, West Bengal — mangrove restoration in India"),("program-agriculture.jpg","Women farmers in an Indian field — sustainable agriculture, green initiatives India"),("gallery-3.jpg","Handloom weaver at work — sustainable fashion in India"),("gallery-4.jpg","School children with a mentor — environmental education India"),("gallery-2.jpg","Rice paddies in Kerala — sustainable food and agriculture in India"),("gallery-5.jpg","Ghats along the Ganga at Varanasi — river cleanups in India"),("gallery-6.jpg","Mango tree in flower, Madhya Pradesh — fruit trees and green canopy"),("show-panel-5.jpg","Solar panels at Dhanas Lake, Chandigarh — clean energy in India")]
