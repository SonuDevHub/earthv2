import json, os
from common import *

def simple_hero(crumb, h1, lede, file):
    return f'''<section class="page-hero"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li><li><a href="{file}" aria-current="page">{crumb}</a></li></ol></nav><h1>{h1}</h1><p class="lede">{lede}</p></div></section>'''

def privacy():
    body = simple_hero("Privacy policy","Privacy Policy","How this website handles information.","privacy-policy.html") + f'''
<section class="section paper-white"><div class="wrap prose">
<p class="draft-banner">DRAFT — requires legal review before publication. Last updated: [date to be set at launch].</p>
<p>This policy explains what information the {ORG} website collects and why. It describes only what the site actually does.</p>
<h2>Who we are</h2><p>{ORG} (“we”). Contact: <span class="tag">TODO</span> official email and postal address to be supplied.</p>
<h2>Information you give us through forms</h2>
<p>Our contact, volunteer and partner / project-interest forms are processed by <strong>Netlify Forms</strong> (Netlify, Inc.), our website host. When you submit a form we receive the details you enter (for example name, email, phone, organisation, city and your message) and the date and time of submission. Netlify stores submissions on its servers and may record technical data such as your IP address and browser for spam filtering.</p>
<p>We use these details only to respond to your enquiry, volunteer interest or partnership request. We do not sell them or use them for advertising. <span class="tag">TODO</span> retention period and who on our team has access to be confirmed.</p>
<h2>Analytics</h2>
<p>The site is prepared for a privacy-friendly, <strong>cookieless</strong> analytics tool (Umami or Plausible). At the time of writing it is <strong>not enabled</strong>. If enabled, it records aggregate page views and events (such as form submissions and button clicks) without cookies and without building individual profiles. <span class="tag">TODO</span> update this section with the chosen provider once enabled.</p>
<h2>Cookies</h2><p>The site itself does not set cookies. We do not use advertising pixels or tag managers.</p>
<h2>Embedded YouTube and Instagram content</h2>
<p>Video and Instagram posts are shown as “click-to-load” placeholders. Nothing is requested from YouTube or Instagram until you click. After you click, content is loaded from <strong>youtube-nocookie.com</strong> (Google) or <strong>instagram.com</strong> (Meta), and those services may set cookies and collect data under their own privacy policies.</p>
<h2>Map</h2><p>The home page map loads map tiles from <strong>OpenStreetMap</strong> (tile.openstreetmap.org) when you scroll to it. Your browser sends a normal request (including your IP address) to OpenStreetMap's servers to fetch the tiles, under the OpenStreetMap Foundation's privacy policy. The map uses no cookies.</p>
<h2>Fonts and other assets</h2><p>All fonts, scripts and images are served from our own website; no third-party font services are used.</p>
<h2>Your choices and rights</h2><p>You can ask us to access, correct or delete the details you submitted through a form. <span class="tag">TODO</span> add contact method and any rights under India's Digital Personal Data Protection Act, 2023, as advised by counsel.</p>
<h2>Changes</h2><p>We will update this page if what the site does changes.</p>
<p><a class="link-arrow" href="terms.html">Terms of use {ARROW}</a></p>
</div></section>'''
    page("privacy-policy.html", f"Privacy Policy | {ORG}", f"How the {ORG} website handles form submissions, cookieless analytics, click-to-load embeds and map tiles.", "", body, crumbs=[("Home","index.html"),("Privacy policy","privacy-policy.html")], priority="0.3")

def terms():
    body = simple_hero("Terms of use","Terms of Use","Simple terms for using this website.","terms.html") + f'''
<section class="section paper-white"><div class="wrap prose">
<p class="draft-banner">DRAFT — requires legal review before publication.</p>
<h2>Use of this site</h2><p>This website provides information about {ORG} and its programmes. You may browse and share pages for non-commercial purposes.</p>
<h2>Content and trademarks</h2><p>Text and materials are © {ORG} unless stated otherwise. EARTHDAY.ORG, Earth Day logos, The Canopy Project™ and The Great Global Cleanup® marks belong to their respective owners. Photographs credited on our <a href="credits.html">photo credits</a> page are used under their stated licences.</p>
<h2>Accuracy</h2><p>We aim to keep information accurate and up to date but make no warranty that it is complete or current.</p>
<h2>External links</h2><p>We are not responsible for the content of external websites we link to.</p>
<h2>Forms</h2><p>Please do not submit sensitive personal information through our forms. See our <a href="privacy-policy.html">privacy policy</a>.</p>
<h2>Governing law</h2><p><span class="tag">TODO</span> jurisdiction to be confirmed by counsel.</p>
</div></section>'''
    page("terms.html", f"Terms of Use | {ORG}", f"Terms for using the {ORG} website, its content and its forms.", "", body, crumbs=[("Home","index.html"),("Terms of use","terms.html")], priority="0.3")

def credits():
    rows = json.load(open(os.path.join(SRC, "credits.json")))
    items = "".join(f'<li><strong>{e(r[0])}</strong> — “{e(r[1])}” by {e(r[3])}, <a href="{e(r[2])}" target="_blank" rel="noopener">Wikimedia Commons<span class="sr-only"> (opens in a new tab)</span></a>, licence: {e(r[4])}{(" (" + "<a href=\"" + e(r[5]) + "\" target=\"_blank\" rel=\"noopener\">licence text<span class=\"sr-only\"> (opens in a new tab)</span></a>)") if r[5] else ""}. Resized and colour-treated. <em>Placeholder — to be replaced by client photos.</em></li>' for r in rows)
    body = simple_hero("Photo credits","Photo Credits","Placeholder photography used on this site, with sources and licences.","credits.html") + f'''
<section class="section paper-white"><div class="wrap prose"><p>All photographs below are placeholders from Wikimedia Commons, used under the licences shown, until the client's own photos are supplied. Logos: EARTHDAY.ORG Brand Library (placeholder mark).</p><ul>{items}</ul></div></section>'''
    page("credits.html", f"Photo Credits | {ORG}", f"Sources and licences of the placeholder photographs used on the {ORG} website.", "", body, crumbs=[("Home","index.html"),("Photo credits","credits.html")], priority="0.2")

def thank_you():
    body = simple_hero("Thank you","Thank You","Your message has been received.","thank-you.html") + f'''
<section class="section paper-white"><div class="wrap narrow"><p class="lede">Thank you for writing to {ORG}. We will get back to you soon.</p><div class="btns"><a class="btn" href="index.html">Back to home {ARROW}</a><a class="btn outline" href="programs.html">Explore our programmes</a></div></div></section>'''
    page("thank-you.html", f"Thank You | {ORG}", f"Thank you for contacting {ORG}.", "", body, noindex=True)

def not_found():
    body = f'''<section class="section paper-white nf"><div class="wrap"><p class="code" aria-hidden="true">4<em>0</em>4</p><h1>Page not found</h1><p class="lede">The page you're looking for has moved or doesn't exist.</p>
<div class="btns btns-center"><a class="btn" href="index.html">Go to home {ARROW}</a><a class="btn outline" href="programs.html">Programmes</a><a class="btn outline" href="join-us.html">Join Us</a></div></div></section>'''
    page("404.html", f"Page Not Found | {ORG}", f"This page could not be found on the {ORG} website.", "", body, noindex=True)

def build():
    privacy(); terms(); credits(); thank_you(); not_found()
