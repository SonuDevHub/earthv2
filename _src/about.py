from common import *

FAQS_ABOUT = [
    ("Is Earth Day Network India a registered trust?",
     f"{ORG} is a registered trust inspired by the global EARTHDAY.ORG movement. It operates across India to advance environmental education, climate literacy, sustainable agriculture, clean energy, and nature restoration."),
    ("What official registrations does Earth Day Network India hold?",
     f"{ORG} holds NITI Aayog's NGO Darpan registration, 12A registration under the Government of India's Income Tax Act, and CSR-1 Certification from the Ministry of Corporate Affairs for CSR partnerships."),
    ("What is the global theme for Earth Day 2027?",
     'The global theme for Earth Day 2027 is "Food for Our Planet™", focusing on sustainable agriculture, soil health, and resilient food systems across India and the world.')
]

def build():
    approach_steps = [
        ("01", "Education", "Fostering environmental literacy through school assemblies, Eco-Comics, and teacher training across India."),
        ("02", "Awareness", "Inspiring public stewardship through nationwide Earth Day campaigns, Earth Murals, and media advocacy."),
        ("03", "Engagement", "Mobilising youth champions, rural women, farmers, and students into active conservation stewards."),
        ("04", "Partnerships", "Collaborating with 130+ institutions, universities, state forest departments, and civil society groups."),
        ("05", "Action", "Delivering tangible ground impact: planting native biodiverse trees, cleaning river corridors, and solar transitions."),
        ("06", "Recognition", "Honouring outstanding grassroots leaders, panchayats, and schools with 400+ Star Awards and citations.")
    ]
    flow_html = "".join(f'''<li class="approach-card reveal">
  <div class="approach-num-wrap">
    <span class="approach-num">{num}</span>
    <span class="approach-dot" aria-hidden="true"></span>
  </div>
  <div class="approach-content">
    <h3 class="approach-title">{title}</h3>
    <p class="approach-desc">{desc}</p>
  </div>
</li>''' for num, title, desc in approach_steps)

    cta = "".join(f'<li>{s}</li>' for s in ["Adopt LiFE initiatives","Encourage a shift to renewable and cleaner energies","Minimise plastic use and manage plastic waste","Expand ways to reduce soil, water and air pollution","Expand the green canopy","Invest in widening the green economy","Promote climate education","Encourage natural farming practices"])

    tl = [
        ("1970", "Global Movement", "Global Earth Day movement begins, mobilising 20 million citizens.", "about-timeline-1970.jpg"),
        ("2010", "Inception in India", "Earth Day Network India established as a registered trust.", "about-timeline-2010.jpg"),
        ("2020", "50th Anniversary", "Digital mobilisation connecting educators, youth, and institutions.", "about-timeline-2020.jpg"),
        ("2026", "Pan-India Network", "Active across all Indian states and Union Territories.", "about-timeline-2026.jpg"),
        ("2027", "Food for Our Planet™", "Global campaign for resilient soils, agriculture, and nourishment.", "about-timeline-2027.jpg")
    ]
    tli = "".join(f'''<li class="tl-item reveal">
  <div class="tl-marker" aria-hidden="true"><span class="tl-dot"></span><span class="tl-line"></span></div>
  <span class="yr">{y}</span>
  <figure class="frame ratio-43 archival">
    <div class="fi">{picture(img, f"Earth Day through the years ({y}) — {t}", "(max-width:640px) 75vw, (max-width:1024px) 35vw, 220px")}</div>
  </figure>
  <div class="tl-content">
    <h3 class="tl-title">{t}</h3>
    <p class="tl-desc">{desc}</p>
  </div>
</li>''' for y, t, desc, img in tl)

    # FAQ accordion items
    faq_items = []
    for i, (q, a) in enumerate(FAQS_ABOUT):
        fid = f"faq-ab-{i+1}"
        faq_items.append(f'''<div class="faq-item">
  <button class="faq-trigger" type="button" aria-expanded="false" aria-controls="{fid}">
    <span class="faq-q">{q}</span>
    <span class="faq-icon" aria-hidden="true">+</span>
  </button>
  <div class="faq-panel" id="{fid}" hidden>
    <p>{a}</p>
  </div>
</div>''')
    faq_html = "".join(faq_items)

    body = f'''{page_hero("About", "About Earth Day India", "Learn how our nationwide network inspires citizens to protect the living environment across all Indian states.", "program-climate.jpg", f"Sundarbans mangroves — {ORG}, environmental organisation in India", "about.html")}
<section class="section paper-white" aria-labelledby="who-h"><div class="wrap editorial">
 <div class="side">{eyebrow("About us","left")}<h2 id="who-h">Earth Day, Every Day</h2><p>Educate. Inspire. Mobilise. Act—for Our Planet</p></div>
 <div class="reveal">
  <p class="dropcap">{ORG} is a registered trust inspired by the global EARTHDAY.ORG movement. We work with people and organisations across India toward a more sustainable future.</p>
  <div class="columns-2">
  <p>Our programmes advance environmental education and climate literacy; nurture youth stewardship for the environment; promote sustainable agriculture and clean energy; help restore forests, mangroves and biodiversity; and mobilise communities for cleanups and plastic reduction.</p>
  <p>Through this work, we aim to help communities build resilience to climate change, adapt to its impacts and contribute to its mitigation, while expanding green livelihoods and supporting the growth of the green economy.</p>
  </div>
  <div class="xlinks"><a class="link-arrow" href="programs.html#education">Climate education {ARROW}</a><a class="link-arrow" href="programs.html#canopy">The Canopy Project™ {ARROW}</a><a class="link-arrow" href="programs.html#cleanup">Cleanups {ARROW}</a></div>
 </div>
</div></section>

<!-- STATS STRIP -->
<section class="section navy tight" id="about-stats" aria-label="Key Figures"><div class="wrap">
 <div class="about-stats-grid">
  <div class="about-stat reveal">
   <span class="about-stat-num">55+</span>
   <span class="about-stat-lbl">Years of Global Movement (Since 1970)</span>
  </div>
  <div class="about-stat reveal">
   <span class="about-stat-num">192</span>
   <span class="about-stat-lbl">Countries Active Worldwide</span>
  </div>
  <div class="about-stat reveal">
   <span class="about-stat-num">1B+</span>
   <span class="about-stat-lbl">Citizens Mobilised Annually</span>
  </div>
  <div class="about-stat reveal">
   <span class="about-stat-num">130+</span>
   <span class="about-stat-lbl">Partner Organisations Across India</span>
  </div>
 </div>
</div></section>

<section class="section paper" id="approach" aria-labelledby="ap-h"><div class="wrap">
 <div class="section-head center">
  <span class="num">No. 01</span>
  {eyebrow("How we work")}
  <h2 id="ap-h">Our Approach</h2>
  <p class="lede">A six-pillar methodology turning environmental commitment into measurable grassroots conservation across India.</p>
 </div>
 <ol class="approach-grid">{flow_html}</ol>
</div></section>

<section class="section paper-white" id="call-to-action" aria-labelledby="cta-h"><div class="wrap editorial">
 <div class="side">{eyebrow("No. 02","left")}<h2 id="cta-h">A Call to Action</h2></div>
 <div><p class="lede strong">The evidence is everywhere: humanity is responsible for the destruction of the environment. We are all in it together.</p>
 <h3 class="mt-l">Let's work to:</h3><ul class="cta-list">{cta}</ul>
 <div class="xlinks"><a class="btn" href="join-us.html" data-track="CTA: Join Us (About)">Join Us {ARROW}</a></div></div>
</div></section>

<section class="section paper" id="trustees" aria-labelledby="tr-h"><div class="wrap">
 <div class="section-head center">{eyebrow("No. 03 · A letter")}<h2 id="tr-h">Note from the Trustees</h2></div>
 <article class="letter reveal">
  <p>The environmental challenges before us are no longer distant concerns. They are visible in our changing climate, water stress, soil degradation, plastic pollution, biodiversity loss and the growing pressures on communities and livelihoods.</p>
  <p>At {ORG}, we believe that meaningful environmental action begins with awareness but must move towards participation and measurable action.</p>
  <p>Our programmes are designed to bring together young people, women, farmers, educators, communities, institutions, businesses and environmental leaders so that everyone can contribute to creating a healthier and more sustainable Earth.</p>
  <p>We remain committed to building partnerships, supporting innovative ideas and creating opportunities for people to become active stewards of our planet.</p>
  <p>We also believe that sustainability and profitability can go hand in hand, and we work with businesses to identify practical pathways to go green, reduce environmental impact, create value and build long-term sustainable growth.</p>
  <p>Earth Day is celebrated once a year, but our responsibility to the Earth is every day.</p>
  <p>Let us work together for our common home—Earth.</p>
  <p class="sign">— The Trustees<small>{ORG}</small></p>
 </article>
</div></section>

<section class="section paper-white" id="timeline" aria-labelledby="tl-h"><div class="wrap">
 <div class="section-head">{eyebrow("No. 04 · Archive","left")}<h2 id="tl-h">Earth Day Through the Years</h2><p class="notice">Placeholder — timeline of major events to be supplied by the client (brief example: 2010 – Inception, 2015 – , 2020 – Online, etc.).</p></div>
 <ol class="timeline">{tli}</ol>
</div></section>

<section class="section paper" id="gallery" aria-labelledby="ga-h"><div class="wrap">
 <div class="section-head split"><div>{eyebrow("No. 05","left")}<h2 id="ga-h">Gallery</h2></div><a class="link-arrow" href="credits.html">Photo credits {ARROW}</a></div>{gallery(GALLERY)}
</div></section>

<!-- FAQ ACCORDION -->
<section class="section paper-white" id="about-faq" aria-labelledby="afaq-h"><div class="wrap narrow">
 <div class="section-head center"><span class="num">No. 06</span>{eyebrow("Frequently Asked Questions")}<h2 id="afaq-h">Trust &amp; Governance</h2></div>
 <div class="faq-accordion" data-accordion>{faq_html}</div>
</div></section>

<!-- CLOSING CTA BAND -->
<section class="section navy cta-band" id="about-cta" aria-labelledby="acta-h"><div class="wrap center narrow">
 {eyebrow("Get Involved")}
 <h2 id="acta-h">Every act counts. Together, we can build a greener, healthier and more sustainable Earth.</h2>
 <p class="lede">Join thousands of individuals, educators, businesses, and communities taking practical environmental action across India.</p>
 <div class="btns btns-center">
  <a class="btn" href="programs.html">Explore Programmes {ARROW}</a>
  <a class="btn ghost" href="join-us.html#partner">Partner With Us</a>
 </div>
</div></section>
'''
    extra_ld = faq_ld(FAQS_ABOUT)
    page("about.html", f"About Us | {ORG} — Environmental Organisation in India",
         f"About {ORG}: a registered trust inspired by EARTHDAY.ORG advancing environmental education, climate action, sustainable agriculture and clean energy across India.",
         "about.html", body, crumbs=[("Home","index.html"),("About","about.html")], extra_ld=extra_ld)
