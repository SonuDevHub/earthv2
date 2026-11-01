from common import *

SLIDES = [("home-page-picture-1.jpg","Canopy Project","Mangrove forest of the Sundarbans, West Bengal — The Canopy Project™ and mangrove restoration in India"),
          ("home-page-picture-2.jpg","Youth","School students in Tamil Nadu — youth and climate education India"),
          ("home-page-picture-3.jpg","Women Farmers","Women farmers sowing seeds in Karnataka — sustainable agriculture in India"),
          ("home-page-picture-4.jpg","Cleanup","Volunteers collecting debris on a beach — cleanups and plastic reduction, Earth Day India")]

# Figures strictly from the client brief
IMPACT = [("500000","0","","+","5,00,000+","farmers engaged","through sustainable agriculture initiatives"),
          ("3.0","1","","+ million","3.0+ million","saplings planted","over the past decade, including extensive mangrove restoration"),
          ("450000","0","","+","4,50,000+","fruit trees gifted","predominantly in impoverished areas to provide both sustenance and income"),
          ("20000","0","","+","20,000+","rural women supported","through clean-energy awareness and adoption programmes"),
          ("851000","0","","+","8,51,000+","Energy Literacy Training completions","With partners"),
          ("100000","0","","+","1,00,000+","schools connected","each year through environmental awareness initiatives"),
          ("450000","0","","+","4,50,000+","young people inspired","through Young Climate Champions initiatives")]

INITIATIVES = [
    ("01", "Sustainable Food and Agriculture", "agriculture", "program-agriculture.jpg",
     "Farmers for Earth connects farmers and Farmer Producer Organisations with experts, climate-resilient agricultural practices, financial opportunities and knowledge-sharing networks."),
    ("02", "The Canopy Project™", "canopy", "program-canopy.jpg",
     "Advancing afforestation, reforestation, agroforestry and large-scale mangrove restoration across climate-vulnerable landscapes in India."),
    ("03", "Clean Energy & Climate-Resilient Communities", "energy", "program-energy.jpg",
     "Our Healthy Energy programme promotes cleaner energy, practical low-carbon choices and clean-cooking solutions across rural and urban India."),
    ("04", "Environmental and Climate Education", "education", "program-education.jpg",
     "Environmental and climate literacy are central to our work, building green curricula, campus green audits and school awareness networks."),
    ("05", "Empowering Youth", "youth", "program-youth.jpg",
     "Our initiatives share climate knowledge with youth and showcase opportunities to be innovators, advocates and leaders in the emerging green economy."),
    ("06", "Cleanups and Circularity", "cleanup", "program-cleanup.jpg",
     "Through The Great Global Cleanup®, we mobilise volunteers and partners to remove waste from beaches, rivers, lakes, neighbourhoods and shared spaces."),
    ("07", "Women", "women", "program-women.jpg",
     "We empower women with knowledge, skills and opportunities to strengthen climate resilience, sustainable livelihoods and community leadership."),
    ("08", "Sustainable Fashion", "fashion", "program-fashion.jpg",
     "Our sustainable fashion initiatives champion responsible, circular and environmentally conscious garment choices and artisan handloom traditions.")
]

FEATURED_PROJECTS = [
    ("The Canopy Project™", "canopy", "Sundarbans & Pan-India", "program-canopy.jpg",
     "3.0+ million saplings planted over the past decade, including extensive mangrove restoration in the Sundarbans and fruit trees gifted to rural communities in Bundelkhand and Andhra Pradesh.",
     "3.0+ Million", "Saplings Planted"),
    ("Healthy Energy Programme", "energy", "15 States across India", "program-energy.jpg",
     "Supporting 20,000+ rural women with clean-energy adoption and clean-cooking awareness, alongside 8,51,000+ Energy Literacy Training completions with partners.",
     "20,000+", "Rural Women Supported"),
    ("Morning Assembly Network", "education", "National School Reach", "program-education.jpg",
     "Engaging 1,00,000+ schools annually through morning assembly environmental awareness broadcasts, green competitions, and teacher-training toolkits.",
     "1,00,000+", "Schools Connected Annually"),
    ("The Great Global Cleanup®", "cleanup", "Beaches, Rivers & Urban Lakes", "program-cleanup.jpg",
     "Mobilising volunteers and civil society to clean critical waterways from Devprayag to Ganga Sagar along the Ganga, Juhu Beach in Mumbai, and Dal Lake in Srinagar.",
     "Major Waterways", "Devprayag to Ganga Sagar"),
    ("Young Climate Champions", "youth", "Pan-India Youth Outreach", "program-youth.jpg",
     "Inspiring 4,50,000+ young people with hands-on climate education, hackathons, and sustainability leadership opportunities across colleges and universities.",
     "4,50,000+", "Young People Inspired"),
    ("My Future My Voice", "mfmv", "Global & India Movement", "gallery-4.jpg",
     "Uniting over 300 youth ambassadors from 125 countries, amplifying youth-driven grassroots environmental solutions and policy advocacy.",
     "300+ Ambassadors", "From 125 Countries")
]

PCARDS = [("program-agriculture.jpg","Sustainable Food and Agriculture","agriculture","Farmers for Earth connects farmers and Farmer Producer Organisations with experts, climate-resilient agricultural practices, financial opportunities and knowledge-sharing networks."),
          ("program-canopy.jpg","The Canopy Project™","canopy","Advancing afforestation, reforestation, agroforestry and large-scale mangrove restoration."),
          ("program-energy.jpg","Clean Energy and Climate-Resilient Communities","energy","Our Healthy Energy programme promotes cleaner energy and practical low-carbon choices."),
          ("program-education.jpg","Environmental and Climate Education","education","Environmental and climate literacy are central to our work."),
          ("program-youth.jpg","Empowering Youth","youth","Our initiatives aim to share climate knowledge with youth and showcase opportunities to be innovators, advocates, and community leaders in the green economy."),
          ("program-cleanup.jpg","Cleanups and Circularity","cleanup","Through The Great Global Cleanup®, we mobilise volunteers and partners to remove waste from beaches, rivers, lakes, neighbourhoods and other shared spaces."),
          ("program-women.jpg","Women","women","We empower women with knowledge, skills and opportunities to strengthen climate resilience, livelihoods and leadership."),
          ("program-fashion.jpg","Sustainable Fashion","fashion","Our sustainable fashion initiatives champion responsible, circular and environmentally conscious choices.")]

PINS = [[30.36,78.43,"Saklana village, Tehri Garhwal","Fruit-tree saplings — The Canopy Project™"],
        [24.69,78.41,"Lalitpur, Bundelkhand","Fruit-tree saplings — The Canopy Project™"],
        [14.68,77.60,"Anantapur, Andhra Pradesh","Fruit-tree saplings — The Canopy Project™"],
        [19.10,72.83,"Juhu Beach, Mumbai","The Great Global Cleanup®"],
        [34.12,74.86,"Dal Lake","The Great Global Cleanup®"],
        [30.15,78.60,"Devprayag","The Great Global Cleanup® — along the Ganga from Devprayag to Ganga Sagar"],
        [21.64,88.07,"Ganga Sagar","The Great Global Cleanup® — along the Ganga from Devprayag to Ganga Sagar"],
        [28.64,77.22,"Delhi","Anti-plastic education material with MCD (Nivaran Dadi)"]]

# 18 Named Partner Organisations strictly from the client brief
PARTNER_NAMES = [
    "Ministry of Environment, Forest and Climate Change",
    "UNICEF",
    "UNESCO-MGIEP",
    "National Service Scheme",
    "National Cadet Corps",
    "WWF",
    "TERI",
    "Centre for Environment Education",
    "Tata Power",
    "ITC",
    "UPS",
    "BBC Media Action",
    "United Way India",
    "SEWA",
    "Energy Swaraj Foundation",
    "Oxford University (Saïd School of Business)",
    "KIIT",
    "Banaras Hindu University"
]

def build():
    dot_count = len(SLIDES) + (1 if HERO_VIDEO else 0)
    slides = ""
    dots = []

    if HERO_VIDEO:
        slides += f'''<div class="slide slide-video is-active" role="group" aria-roledescription="slide" aria-label="1 of {dot_count}: Highlight Video" data-label="Highlight Video">
  <div class="hero-video-wrap">
    <video autoplay muted loop playsinline poster="assets/video/hero-poster.jpg" preload="metadata" class="hero-bg-video">
      <source src="assets/video/hero.webm" type="video/webm">
      <source src="assets/video/hero.mp4" type="video/mp4">
    </video>
  </div>
</div><!-- CLIENT VIDEO: assets/video/hero.mp4 / assets/video/hero.webm -->\n'''
        dots.append(f'<button type="button" aria-label="Show slide 1: Highlight Video" aria-current="true"></button>')

    for i,(src,lab,alt) in enumerate(SLIDES):
        idx = (i + 1) if HERO_VIDEO else i
        act = " is-active" if (i == 0 and not HERO_VIDEO) else ""
        cur = "true" if (i == 0 and not HERO_VIDEO) else "false"
        eager_flag = (i == 0 and not HERO_VIDEO)
        slides += f'<div class="slide{act}" role="group" aria-roledescription="slide" aria-label="{idx+1} of {dot_count}: {lab}" data-label="{lab}">{picture(src, alt, "100vw", eager=eager_flag)}</div><!-- CLIENT PHOTO: replace _src/img/{src} with Drive "Home Page front 4" / Home Page Picture {i+1} ({lab}) -->\n'
        dots.append(f'<button type="button" aria-label="Show slide {idx+1}: {lab}" aria-current="{cur}"></button>')

    dots_html = "".join(dots)
    initial_label = "Highlight Video" if HERO_VIDEO else SLIDES[0][1]

    impact_items = "".join(f'<li class="impact reveal"><p class="n mb-0" data-count="{c}" data-dec="{d}" data-prefix="{p}" data-suffix="{s}" data-final="{disp}"><span class="sr-only">{disp}</span><span aria-hidden="true">{disp}</span></p><p class="t">{t}</p><p class="c">{cap}</p></li>' for c,d,p,s,disp,t,cap in IMPACT)
    # Awardee headshot monogram tiles
    head_monograms = [
        ("HR", "Earth Day Hero", "Heroes"),
        ("ML", "Municipal Leader", "Urban"),
        ("WG", "Women's Group", "Women"),
        ("RS", "Rising Star", "Youth"),
        ("ES", "Earth Star", "Civic"),
        ("VG", "Village Award", "Rural"),
        ("CS", "Clean Cooking", "Energy"),
        ("LF", "Litter Free", "Cleanups"),
        ("SC", "Star Campus", "Campus"),
        ("YE", "Earthpreneur", "Green Biz"),
        ("PC", "Panchayat Star", "Local Gov"),
        ("SR", "Special Honor", "Security")
    ]
    heads = "".join(f'''<li class="headshot">
  <div class="ph monogram-avatar" title="{title} — {cat}">
    <span class="mono-initials">{mono}</span>
  </div>
  <span>{title}</span>
</li>''' for mono, title, cat in head_monograms)

    strip_alts = ["Dense mangrove forest of the Sundarban Tiger Reserve, West Bengal","Rice fields in Kerala — sustainable agriculture India","Dal Lake, Srinagar — lake cleanups in India","Ganga Mahal Ghat, Varanasi — Ganga cleanup India","Solar power at Dhanas Lake, Chandigarh — clean energy India"]
    strip = "".join(f'<li class="{"archival archival-hover" if i in (1,3) else ""}">{picture(f"show-panel-{i+1}.jpg", a, "(max-width:640px) 20vw, 20vw")}</li>' for i,a in enumerate(strip_alts))
    cards = "".join(f'<li><a class="p-card" href="programs.html#{anc}" data-track="Programme card">{picture(src, "", "(max-width:640px) 82vw, (max-width:980px) 50vw, 300px")}<span class="shade"></span><span class="fr"></span><div class="body"><span class="pn">No. {i+1:02d} · Placeholder</span><h3>{t}</h3><p>{txt}</p><span class="link-arrow">Read more {ARROW}</span></div></a></li>' for i,(src,t,anc,txt) in enumerate(PCARDS))

    # Initiatives rows with preview images
    init_rows = []
    for num, title, anc, img, desc in INITIATIVES:
        img_base = os.path.splitext(img)[0]
        preview_src = f"assets/img/programs/{img_base}-800.jpg"
        init_rows.append(f'''<a class="init-row reveal" href="programs.html#{anc}" data-preview="{preview_src}" data-track="Initiative: {title}">
  <span class="init-num">{num}</span>
  <div class="init-body">
    <h3 class="init-title">{title}</h3>
    <p class="init-desc">{desc}</p>
  </div>
  <span class="init-arrow">{ARROW}</span>
</a>''')
    initiatives_html = "".join(init_rows)

    # Globe places list
    markers_path = os.path.join(SRC, "data", "markers.json")
    if not os.path.exists(markers_path): markers_path = os.path.join(ROOT, "assets", "earth", "markers.json")
    markers_data = json.load(open(markers_path, encoding="utf-8")) if os.path.exists(markers_path) else []
    
    place_buttons = []
    for m in markers_data:
        place_buttons.append(f'''<button class="globe-place-item" type="button" data-id="{m['id']}" data-cat="{m['category']}" data-lat="{m['lat']}" data-lng="{m['lng']}" data-name="{e(m['name'])}" data-place="{e(m['place'])}" data-prog="{e(m['program'])}" data-desc="{e(m['description'])}" data-stats="{e(m.get('stats',''))}" data-anchor="{m.get('anchor','programs.html')}">
  <span class="place-dot" aria-hidden="true"></span>
  <span class="place-text">
    <strong class="place-name">{e(m['name'])}</strong>
    <small class="place-loc">{e(m['place'])}</small>
  </span>
  <span class="place-tag">{e(m['category'])}</span>
</button>''')
    places_list_html = "".join(place_buttons)

    # Testimonials Slider items (Content strictly from brief)
    brief_quotes = [
        ("Earth Day is celebrated once a year, but our responsibility to the Earth is every day.",
         "The Trustees", "Earth Day Network India", "TR", "about.html#trustees"),
        ("Every act counts. Collective action multiplies its impact.",
         "Earth Day Network India", "National Citizen Movement", "EDN", "join-us.html"),
        ("We need all hands on deck—and many more green actions—to build a healthier, more sustainable world that benefits everyone.",
         "Leadership Message", "Earth Day Network India", "LM", "about.html"),
        ("Additional partner testimonial and quotes to be supplied upon official client launch.",
         "Partner Organisation", "Institutional Network (TODO)", "TODO", "join-us.html#partner")
    ]
    t_slides = []
    t_dots = []
    for i, (q, author, org_role, mono, link) in enumerate(brief_quotes):
        act_cls = " is-active" if i == 0 else ""
        cur_attr = ' aria-current="true"' if i == 0 else ' aria-current="false"'
        t_slides.append(f'''<div class="t-slide{act_cls}" data-index="{i}" role="group" aria-roledescription="slide" aria-label="Quote {i+1} of {len(brief_quotes)}">
  <div class="t-slide-content">
    <blockquote class="pull mb-0">“{q}”</blockquote>
    <div class="t-author-block">
      <div class="t-avatar" aria-hidden="true">{mono}</div>
      <div class="t-meta">
        <cite class="t-author">{author}</cite>
        <span class="t-role">{org_role}</span>
        <a class="link-arrow mt-s" href="{link}">Learn more {ARROW}</a>
      </div>
    </div>
  </div>
</div>''')
        t_dots.append(f'<button class="t-dot" type="button" data-index="{i}" aria-label="Go to testimonial {i+1}"{cur_attr}></button>')
    
    t_slides_html = "".join(t_slides)
    t_dots_html = "".join(t_dots)

    # Featured projects slides
    feat_slides = []
    for i, (title, anc, loc, img, desc, stat_val, stat_lbl) in enumerate(FEATURED_PROJECTS):
        act_cls = " is-active" if i == 0 else ""
        feat_slides.append(f'''<div class="feat-slide{act_cls}" data-index="{i}" role="group" aria-roledescription="slide" aria-label="{i+1} of {len(FEATURED_PROJECTS)}: {title}">
  <div class="feat-slide-grid">
    <div class="feat-slide-info">
      <span class="feat-tag">{loc}</span>
      <h3 class="feat-slide-title">{title}</h3>
      <p class="feat-slide-desc">{desc}</p>
      <div class="feat-stat-badge">
        <span class="feat-stat-num">{stat_val}</span>
        <span class="feat-stat-label">{stat_lbl}</span>
      </div>
      <div class="feat-slide-cta">
        <a class="btn" href="programs.html#{anc}">Explore project {ARROW}</a>
      </div>
    </div>
    <div class="feat-slide-media">
      {picture(img, f"{title} - Earth Day India", "(max-width:768px) 100vw, 600px")}
    </div>
  </div>
</div>''')
    featured_slides_html = "".join(feat_slides)

    # Partner marquee items
    partner_marquee_items = "".join(f'<span class="m-item">{p}</span><span class="m-dot" aria-hidden="true">&bull;</span>' for p in PARTNER_NAMES)

    news = "".join('<li><span class="date">Date TBC</span><div><h3>News headline placeholder</h3><p>Short summary of the news item — to be supplied.</p></div></li>' for _ in range(4))
    tests = "".join('<li class="testimonial"><blockquote>“Testimonial text to be supplied by the client.”</blockquote><p class="who mb-0">Name · Role / Organisation</p></li>' for _ in range(3))
    yt_src = f"https://www.youtube-nocookie.com/embed/{YOUTUBE_ID}" if YOUTUBE_ID else ""
    ig_src = (INSTAGRAM_POST.rstrip("/") + "/embed") if INSTAGRAM_POST else ""

    body = f'''
<!-- SECTION 1: HERO (Dark) -->
<section class="hero" aria-roledescription="carousel" aria-label="{ORG} highlights">
{slides}<div class="hero-scrim" aria-hidden="true"></div>
<div class="hero-content"><div class="wrap"><div class="inner">
 <span class="eyebrow left">{ORG}</span>
 <h1>Earth Day, Every Day</h1>
 <p class="kicker">Educate. Inspire. Mobilise. Act—for Our Planet</p>
 <p class="sub">Every act counts. Together, we can build a greener, healthier and more sustainable Earth.</p>
 <div class="btns">
  <a class="btn" href="programs.html" data-track="CTA: Explore Our Work">Explore Our Work {ARROW}</a>
  <a class="btn ghost btn-secondary-hero" href="join-us.html#partner" data-track="CTA: Partner With Us">Partner With Us</a>
 </div>
</div></div></div>
<div class="hero-controls">
 <button class="ctl pause" type="button" aria-pressed="false" aria-label="Pause slideshow">{icon("pause","icon i-pause")}{icon("play","icon i-play")}</button>
 <button class="ctl prev" type="button" aria-label="Previous slide">{icon("arrow-l")}</button>
 <div class="hero-dots">{dots_html}</div>
 <button class="ctl next" type="button" aria-label="Next slide">{icon("arrow-r")}</button>
</div>
<p class="slide-label" aria-hidden="true">Now showing &nbsp;<b>{initial_label}</b></p>
<p class="sr-only hero-live" aria-live="polite"></p>
</section>
<div class="white-line" aria-hidden="true"></div>

<!-- SECTION 2: INTRO (Light - paper-white) -->
<section class="section paper-white intro center" aria-labelledby="intro-h"><div class="wrap">
 <h2 id="intro-h" class="sr-only">About {ORG}</h2>
 {eyebrow("Environmental NGO in India")}
 <p class="reveal">{ORG} is a registered trust inspired by the global EARTHDAY.ORG movement.</p>
 <p class="reveal">We work with people and organisations across India toward a more sustainable future.</p>
 <div class="ornament" aria-hidden="true">{STAR}</div>
 <p class="mt-l"><a class="link-arrow" href="about.html">Read about us {ARROW}</a></p>
</div></section>

<!-- SECTION 3: 3D EARTH GLOBE (Dark - Navy) -->
<section class="section navy" id="global-movement" aria-labelledby="globe-h"><div class="wrap">
 <div class="section-head split">
  <div>
   {eyebrow("Our Global Movement", "left")}
   <h2 id="globe-h">One Movement. Across India and the World.</h2>
  </div>
  <p class="lede mb-0">EARTHDAY.ORG works with over 130 partner organisations across India and engages citizens in 192 countries. Filter by programme or select a location from the legend to explore our on-the-ground action.</p>
 </div>

 <!-- Map Legend Programme Groups -->
 <div class="globe-legend-bar" role="group" aria-label="Filter programme locations on the globe">
  <button class="globe-legend-btn active" type="button" data-filter="all">All Programmes</button>
  <button class="globe-legend-btn" type="button" data-filter="forests">Forests &amp; Canopy</button>
  <button class="globe-legend-btn" type="button" data-filter="cleanups">Cleanups</button>
  <button class="globe-legend-btn" type="button" data-filter="education">Education</button>
  <button class="globe-legend-btn" type="button" data-filter="agriculture">Agriculture</button>
  <button class="globe-legend-btn" type="button" data-filter="energy">Energy</button>
  <button class="globe-legend-btn" type="button" data-filter="youth">Youth</button>
 </div>

 <!-- 3D Globe Stage Grid (Globe + Places Directory) -->
 <div class="globe-stage-grid">
  <!-- 3D Globe Canvas Container -->
  <div class="earth-canvas-wrapper" id="earth-canvas-container" aria-label="Interactive 3D Earth Globe showing Earth Day Network India project locations">
   <noscript>
    <div class="earth-fallback" style="background-image: url('assets/earth/earth-day.jpg');">
     <div class="earth-fallback-overlay">
      <h3>Our Worldwide Movement</h3>
      <p>Mobilizing 1 billion people annually across 192 countries.</p>
      <a href="network.html" class="btn">Explore Network {ARROW}</a>
     </div>
    </div>
   </noscript>
   <!-- Bottom-sheet info card for clicked markers -->
   <div class="globe-sheet" id="globe-sheet" hidden aria-live="polite">
    <button class="sheet-close" id="globe-sheet-close" type="button" aria-label="Close location card">&times;</button>
    <div class="sheet-content" id="globe-sheet-content"></div>
   </div>
  </div>

  <!-- Interactive Places List Directory -->
  <div class="globe-places-dir" aria-label="Programme Locations Directory">
   <div class="globe-places-header">
    <h4>Programme Locations</h4>
    <span class="globe-places-count" id="globe-places-count">{len(markers_data)} locations</span>
   </div>
   <div class="globe-places-scroll" id="globe-places-list" role="list">
    {places_list_html}
   </div>
  </div>
 </div>

 <!-- Count-Up Stats Strip -->
 <div class="globe-stats-strip">
  <div class="globe-stat-col">
   <span class="globe-stat-number counter" data-target="130">130+</span>
   <span class="globe-stat-label">Partner Organisations</span>
  </div>
  <div class="globe-stat-col">
   <span class="globe-stat-number counter" data-target="192">192</span>
   <span class="globe-stat-label">Countries Active</span>
  </div>
  <div class="globe-stat-col">
   <span class="globe-stat-number counter" data-target="1000000000">1B+</span>
   <span class="globe-stat-label">People Mobilised Annually</span>
  </div>
  <div class="globe-stat-col">
   <span class="globe-stat-number counter" data-target="300">300+</span>
   <span class="globe-stat-label">Youth Ambassadors</span>
  </div>
 </div>

 <div class="center mt-l">
  <a class="btn" href="network.html" data-track="CTA: Explore Our Network">Explore Our Network {ARROW}</a>
 </div>
</div></section>

<!-- SECTION 4: GUIDING OUR PATH STATEMENT BAND (Light - paper) -->
<section class="section paper" id="statement" aria-label="Guiding Our Path"><div class="wrap">
 <div class="statement-band">
  <div class="statement-header">
   {eyebrow("Guiding Our Path", "left")}
   <h2 class="statement-quote">Educate. Inspire. Mobilise. Act—for Our Planet</h2>
  </div>
  <div class="statement-body">
   <div class="statement-photos">
    <div class="photo-offset photo-1">
     {picture("program-agriculture.jpg", "Women farmers participating in sustainable agriculture — Earth Day India", "(max-width:768px) 90vw, 380px")}
    </div>
    <div class="photo-offset photo-2">
     {picture("program-canopy.jpg", "Mangrove reforestation and tree sapling planting — The Canopy Project India", "(max-width:768px) 90vw, 380px")}
    </div>
   </div>
   <div class="statement-text">
    <p class="statement-lead">Earth Day is celebrated once a year, but our responsibility to the Earth is every day.</p>
    <p class="statement-sub">From rural farming belts to coastal mangrove ecosystems and nationwide schools, we turn environmental commitment into measurable grassroots impact.</p>
    <a class="link-arrow" href="about.html">Learn more about our mission {ARROW}</a>
   </div>
  </div>
 </div>
</div></section>

<!-- SECTION 5: IMPACT (Dark - Navy) -->
<section class="section navy" id="impact" aria-labelledby="impact-h"><div class="wrap">
 <div class="section-head center"><span class="num">No. 01</span>{eyebrow("Impact")}<h2 id="impact-h">A Glimpse of Our Impact Across India</h2></div>
 <ul class="impact-grid">{impact_items}<li class="impact cta reveal"><a class="link-arrow" href="programs.html">Explore our programmes {ARROW}</a></li></ul>
</div></section>

<!-- SECTION 6: AWARDEES (Light - paper) -->
<section class="section paper" id="awardees" aria-labelledby="aw-h"><div class="wrap awardees">
 <div><h3 class="sr-only">Awardee headshots (placeholders)</h3><ul class="headshots">{heads}</ul><p class="notice">Placeholder headshots — 10–12 awardee photos to be supplied by the client.</p></div>
 <div class="reveal">{eyebrow("Awards &amp; Recognitions","left")}<p class="big-stat mb-0">400<em>+</em></p><h2 id="aw-h" class="big-stat-title">Star Awards and recognitions presented</h2>
  <p class="lede">to villages, women's groups, environmental leaders, clean-cooking champions, educational institutions, municipalities and religious sites advancing sustainability.</p>
  <a class="btn solid-navy" href="awards.html" data-track="CTA: View the Awards">View the Awards {ARROW}</a></div>
</div></section>

<!-- SECTION 7: SHOW PANEL (Photo Strip) -->
<section aria-label="Show panel"><ul class="strip">{strip}</ul></section>
<!-- CLIENT PHOTOS: Show panel — replace show-panel-1..5.jpg with the 5 square photos from Drive -->

<!-- SECTION 8: THEME 2027 (Light - paper-white) -->
<section class="section paper-white" id="theme" aria-labelledby="theme-h"><div class="wrap">
 <div class="section-head split"><div>{eyebrow("Global theme","left")}<h2 id="theme-h">Earth Day 2027</h2></div><a class="link-arrow" href="programs.html#edo-theme">How we bring it to India {ARROW}</a></div>
 <a class="theme-panel reveal" href="{GLOBAL_THEME_URL}" target="_blank" rel="noopener" data-track="Outbound: global theme">
  <div class="img duotone">{picture("theme-2027.jpg", "Farmers working a field in Kerala — Earth Day 2027 theme, Food for Our Planet (placeholder image)", "(max-width:980px) 100vw, 700px")}</div>
  <div class="txt"><span class="eyebrow left on-yellow">EARTHDAY.ORG · 22 April 2027</span><h3>Food for Our Planet™</h3><p>Healthy People, Healthy Soils, Healthy Futures — explore the global Earth Day 2027 theme on EARTHDAY.ORG.</p><span class="link-arrow">Visit the global theme page {icon("ext")}<span class="sr-only"> (opens in a new tab)</span></span></div>
 </a><!-- CLIENT PHOTO: replace with Drive 'Theme 2027' -->
</div></section>

<!-- SECTION 9: INITIATIVES LIST WITH HOVER PREVIEW (Light - paper) -->
<section class="section paper" id="initiatives" aria-labelledby="init-h"><div class="wrap">
 <div class="section-head split">
  <div>
   <span class="num">No. 02</span>
   {eyebrow("Key Initiatives", "left")}
   <h2 id="init-h">Building Nature's Future</h2>
  </div>
  <p class="lede mb-0">From agriculture to clean energy, we act where nature needs us most across India.</p>
 </div>
 <div class="initiatives-list-container">
  <div class="initiatives-rows">
   {initiatives_html}
  </div>
  <!-- Floating desktop preview card -->
  <div class="init-hover-preview" id="init-hover-preview" aria-hidden="true">
   <img src="assets/img/program-agriculture-800.jpg" alt="" id="init-preview-img">
  </div>
 </div>
</div></section>

<!-- SECTION 10: EVENTS PREVIEW (Light - paper-white tight) -->
<section class="section paper-white tight" id="events-preview" aria-labelledby="ev-h"><div class="wrap">
 <div class="section-head split"><div>{eyebrow("Events","left")}<h2 id="ev-h">Events</h2></div><a class="link-arrow" href="events.html">All events {ARROW}</a></div>
 <ul class="event-boxes">
  <li class="event-box reveal"><span class="idx">01 · Nominations</span><h3>Nominations are open for……</h3><p>More information to come. {tag()}</p><a class="link-arrow" href="awards.html#all-awards">Award categories {ARROW}</a></li>
  <li class="event-box reveal"><span class="idx">02 · Applications</span><h3>Apply for……</h3><p>More information to come. {tag()}</p><a class="link-arrow" href="join-us.html#forms">Project interest forms {ARROW}</a></li>
  <li class="event-box reveal"><span class="idx">03 · Calendar</span><h3>Go to events</h3><p>Upcoming, ongoing and major past events.</p><a class="link-arrow" href="events.html#upcoming">See events {ARROW}</a></li>
 </ul>
</div></section>

<!-- SECTION 11: FEATURED PROJECTS SLIDER (Dark - Navy) -->
<section class="section navy" id="featured-projects" aria-labelledby="feat-h"><div class="wrap">
 <div class="section-head split">
  <div>
   <span class="num">No. 03</span>
   {eyebrow("Featured Projects", "left")}
   <h2 id="feat-h">Action on the Ground</h2>
  </div>
  <div class="feat-slider-nav">
   <button class="feat-nav-btn feat-prev" id="feat-prev-btn" type="button" aria-label="Previous project">{icon("arrow-l")}</button>
   <span class="feat-counter" id="feat-slide-counter" aria-live="polite">01 / {len(FEATURED_PROJECTS):02d}</span>
   <button class="feat-nav-btn feat-next" id="feat-next-btn" type="button" aria-label="Next project">{icon("arrow-r")}</button>
  </div>
 </div>
 <div class="feat-progress-bar"><div class="feat-progress-track" id="feat-progress-track"></div></div>
 <div class="feat-slider-container" id="feat-slider-wrap">
  {featured_slides_html}
 </div>
</div></section>

<!-- SECTION 12: MAJOR PROGRAMS CAROUSEL (Light - paper-white) -->
<section class="section paper-white" id="programs" aria-labelledby="pr-h"><div class="wrap">
 <div class="section-head split"><div><span class="num">No. 04</span>{eyebrow("Major Programs","left")}<h2 id="pr-h">Turning Global Priorities into Action in India</h2><p class="lede mb-0">Our programmes reflect global Earth Day themes while responding to India's environmental priorities and diverse social realities.</p></div>
 <div class="carousel-nav" data-for="pcar"><button class="c-prev" type="button" aria-controls="pcar" aria-label="Previous programmes">{icon("arrow-l")}</button><button class="c-next" type="button" aria-controls="pcar" aria-label="Next programmes">{icon("arrow-r")}</button></div></div>
 <section class="carousel" aria-roledescription="carousel" aria-label="Major programmes"><ul class="carousel-track" id="pcar">{cards}</ul></section>
 <p class="notice">Placeholder cards — final home-page text and photos for this section will be supplied by the client.</p>
</div></section>

<!-- SECTION 13: NETWORK PREVIEW - LEADERSHIP & VOICES (Light - paper) -->
<section class="section paper" id="network-preview" aria-labelledby="np-h"><div class="wrap">
 <div class="section-head split">
  <div>
   <span class="num">No. 05</span>
   {eyebrow("Leadership & Voices", "left")}
   <h2 id="np-h">Voices Across Our Network</h2>
  </div>
  <a class="link-arrow" href="network.html">View full network {ARROW}</a>
 </div>
 <div class="network-cards-grid">
  <div class="network-tile reveal">
   <div class="tile-avatar"><span>AM</span></div>
   <div class="tile-content">
    <h3>Ambassadors &amp; Youth</h3>
    <p>Over 300 My Future My Voice youth ambassadors from 125 countries, championing grassroots sustainability in India and worldwide.</p>
    <a class="link-arrow" href="network.html#ambassadors">Learn more {ARROW}</a>
   </div>
  </div>
  <div class="network-tile reveal">
   <div class="tile-avatar"><span>AD</span></div>
   <div class="tile-content">
    <h3>Advisory Committee</h3>
    <p>Distinguished experts, scientists, educators, and sustainability thought leaders providing strategic guidance to our programmes.</p>
    <a class="link-arrow" href="network.html#advisors">Learn more {ARROW}</a>
   </div>
  </div>
  <div class="network-tile reveal">
   <div class="tile-avatar"><span>CE</span></div>
   <div class="tile-content">
    <h3>Canopy Project Experts</h3>
    <p>Specialists in afforestation, native species selection, agroforestry and mangrove conservation across ecologically sensitive zones.</p>
    <a class="link-arrow" href="network.html#canopy-experts">Learn more {ARROW}</a>
   </div>
  </div>
 </div>
</div></section>

<!-- SECTION 14: PARTNERS MARQUEE & LOGOS (Dark - Navy) -->
<section class="section navy tight" id="partners-home" aria-labelledby="pa-h">
 <div class="wrap">
  <div class="section-head center">
   {eyebrow("Our Partners")}
   <h2 id="pa-h">Partner Organisations Across India</h2>
  </div>
 </div>
 <div class="marquee-track-wrap" aria-label="Partner organisations slow marquee">
  <div class="marquee-track">
   <div class="marquee-content">
    {partner_marquee_items}
   </div>
   <div class="marquee-content" aria-hidden="true">
    {partner_marquee_items}
   </div>
  </div>
 </div>
 <div class="wrap mt-l">
  <div class="slot"><div><strong>Partner logos</strong>Placeholder — the client's combined partner-logo image (Drive) goes here. <a href="join-us.html#partner">Partner with us {ARROW}</a></div></div>
 </div>
</section>

<!-- SECTION 15: LIVE ON YOUTUBE & INSTAGRAM (Light - paper-white) -->
<section class="section paper-white" id="live" aria-label="YouTube and Instagram"><div class="wrap halves">
 <div><div class="half-title"><h2>Live on YouTube</h2>{social_link("youtube")}</div>
  <div class="embed"><button class="facade" type="button" data-kind="youtube" data-title="{ORG} on YouTube" data-src="{yt_src}">{picture("show-panel-1.jpg","","(max-width:980px) 100vw, 560px")}<span class="play">{icon("play")}</span><span class="lbl">Load YouTube video</span><span class="fine">Click to load. YouTube (youtube-nocookie.com) is contacted only after you click.</span></button></div></div>
 <div><div class="half-title"><h2>On Instagram</h2>{social_link("instagram")}</div>
  <div class="embed"><button class="facade" type="button" data-kind="instagram" data-title="{ORG} on Instagram" data-src="{ig_src}">{picture("gallery-3.jpg","","(max-width:980px) 100vw, 560px")}<span class="play">{icon("play")}</span><span class="lbl">Load Instagram post</span><span class="fine">Click to load. Instagram is contacted only after you click.</span></button></div></div>
</div></section>

<!-- SECTION 16: MAP AND NEWS (Light - paper) -->
<section class="section paper" id="map-news" aria-label="Map and news"><div class="wrap halves">
 <div><div class="half-title"><h2>Where We Work</h2>{tag("Sample pins")}</div>
  <section id="map" aria-label="Map of places named in {ORG} programme texts" data-css="assets/vendor/leaflet/leaflet.css" data-js="assets/vendor/leaflet/leaflet.js" data-img="assets/vendor/leaflet/images/" data-pins='{json.dumps(PINS, ensure_ascii=False)}'><p class="map-fallback">Interactive map (OpenStreetMap) loads here.</p></section>
  <p class="notice">Pins mark places named in the programme texts. Final project locations to be supplied by the client.</p></div>
 <div><div class="half-title"><h2>News</h2><a class="link-arrow" href="events.html#news">EDN in News {ARROW}</a></div><ul class="news-list">{news}</ul></div>
</div></section>

<!-- SECTION 17: QUOTES & TESTIMONIALS SLIDER (Dark - Navy) -->
<section class="section navy" id="quotes" aria-labelledby="q-h" aria-roledescription="carousel" aria-label="Quotes and Testimonials">
 <div class="wrap">
  <div class="section-head center">
   {eyebrow("Quotes &amp; Testimonials")}
   <h2 id="q-h">Voices of Responsibility</h2>
   <p class="lede">Reflections and commitments from our trustees, leadership, and nationwide movement.</p>
  </div>
  <div class="t-slider-wrap">
   <div class="t-slider-track" id="t-slider-track">
    {t_slides_html}
   </div>
   <div class="t-slider-controls">
    <button class="t-nav-btn t-prev" type="button" aria-label="Previous quote">{icon("arrow-l")}</button>
    <div class="t-dots" role="tablist" aria-label="Quote slide controls">
     {t_dots_html}
    </div>
    <button class="t-nav-btn t-next" type="button" aria-label="Next quote">{icon("arrow-r")}</button>
   </div>
  </div>
 </div>
</section>
'''
    page("index.html", f"{ORG} | Environmental NGO in India — Earth Day Every Day",
         f"{ORG} is a registered trust and environmental NGO in India inspired by EARTHDAY.ORG — climate education, sustainable agriculture, clean energy, tree planting and cleanups.",
         "index.html", body, priority="1.0")
