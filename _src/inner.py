from common import *

def profiles(n, role):
    return '<ul class="profiles">' + "".join(f'<li class="profile reveal"><div class="ph">{SILHOUETTE}</div><h3>Name</h3><p>{role} · details to be supplied</p></li>' for _ in range(n)) + '</ul>'

def network():
    groups = [("ambassadors","Our Ambassadors","Each is an influential individual in their field who also champions the Earth Day movement and helps extend its reach through their networks, platforms, communities, and environmental initiatives. They inspire wider participation, strengthen public awareness and encourage meaningful action.","Ambassador",4),
              ("advisors","Our Advisors","Our Advisors are distinguished subject-matter experts and experienced professionals who contribute knowledge, insight and strategic guidance across environmental and sustainability issues, strengthening our programmes, initiatives and outreach as needs and opportunities arise.","Advisor",4),
              ("canopy-experts","Our Experts for the Canopy Project","Each has served at the highest level of their state's forest department, bringing decades of field experience and expertise to guide and strengthen our conservation and restoration initiatives.","Canopy Project expert",4),
              ("mfmv","MFMV",'My Future My Voice — Youth Ambassadors. <a href="programs.html#my-future-my-voice">Read about the initiative</a>.',"Youth Ambassador",4),
              ("artists","Artists",None,"Artist",4),
              ("athletes","Athletes",None,"Athlete",4)]
    rows = []
    for i,(aid,t,txt,role,n) in enumerate(groups):
        intro = f'<p>{txt}</p>' if txt else f'<p class="notice">Introduction text to be supplied by the client.</p>'
        rows.append(f'<section class="network-row" id="{aid}" aria-labelledby="{aid}-h"><div class="nr-aside">{eyebrow(f"No. {i+1:02d}","left")}<h2 id="{aid}-h">{t}</h2>{intro}</div>{profiles(n, role)}</section>')
    sn = [("Ambassadors","ambassadors"),("Advisors","advisors"),("Canopy Experts","canopy-experts"),("MFMV","mfmv"),("Artists","artists"),("Athletes","athletes"),("Partners","partners")]
    body = f'''{page_hero("Network","Our Network","Ambassadors, advisors, experts, artists, athletes and partners who extend the Earth Day movement across India.","gallery-4.jpg",f"Mentors with school children — the {ORG} network","network.html")}
{subnav(sn)}

<!-- STATS STRIP -->
<section class="section navy tight" id="network-stats" aria-label="Network Figures"><div class="wrap">
 <div class="about-stats-grid">
  <div class="about-stat reveal">
   <span class="about-stat-num">300+</span>
   <span class="about-stat-lbl">Youth Ambassadors from 125 Countries</span>
  </div>
  <div class="about-stat reveal">
   <span class="about-stat-num">130+</span>
   <span class="about-stat-lbl">Partner Organisations Across India</span>
  </div>
  <div class="about-stat reveal">
   <span class="about-stat-num">400+</span>
   <span class="about-stat-lbl">Star Awards &amp; Recognitions Presented</span>
  </div>
  <div class="about-stat reveal">
   <span class="about-stat-num">147.5M</span>
   <span class="about-stat-lbl">Faith-Site Outreach Reach</span>
  </div>
 </div>
</div></section>

<div class="paper-white"><div class="wrap">{"".join(rows)}</div></div>

<section class="section navy" id="partners" aria-labelledby="pa-h"><div class="wrap"><div class="section-head center">{eyebrow("All our partners")}<h2 id="pa-h">Our Partners</h2></div><div class="slot"><div><strong>All our partners photo</strong>Placeholder — combined partner-logo image to be supplied. <a href="join-us.html#partner">Become a partner</a></div></div></div></section>

<!-- CLOSING CTA BAND -->
<section class="section paper cta-band" id="network-cta" aria-labelledby="netcta-h"><div class="wrap center narrow">
 {eyebrow("Join the Network")}
 <h2 id="netcta-h">Connect With Our Movement Across India</h2>
 <p class="lede">Whether you are an institutional leader, educator, youth activist or conservationist, add your voice to the Earth Day network.</p>
 <div class="btns btns-center">
  <a class="btn" href="join-us.html#partner">Partner With Us {ARROW}</a>
  <a class="btn ghost" href="join-us.html#volunteer">Volunteer</a>
 </div>
</div></section>
'''
    page("network.html", f"Our Network | Ambassadors, Advisors & Partners — {ORG}",
         f"Meet the {ORG} network: ambassadors, advisors, Canopy Project experts, My Future My Voice youth ambassadors, artists, athletes and partners of Earth Day India.",
         "network.html", body, crumbs=[("Home","index.html"),("Network","network.html")])

AW9 = [("Earth Day Heroes","Individuals and organisations demonstrating exceptional environmental commitment and community mobilisation."),
 ("Star Municipal Leaders Award","Municipal corporations and urban local bodies leading environmental sustainability, waste management, cleanups, plastic reduction, green initiatives and community engagement."),
 ("Star Women's Group Award","Women leaders, women-led groups and community initiatives creating meaningful environmental and climate action."),
 ("Earth Day Rising Stars","Children and teenagers actively engaged in environmental conservation, with opportunities to showcase their work and connect with useful networks."),
 ("Earth Day Stars","Individuals and organisations making outstanding contributions to environmental awareness, sustainability and action."),
 ("Village Awards","Villages and rural communities leading conservation, responsible resource use, waste management, renewable energy, biodiversity and community participation."),
 ("Clean Cooking Stars","Individuals, communities and initiatives advancing cleaner and healthier cooking, renewable energy and low-carbon lifestyles."),
 ("Litter Free India Champions","Innovative and sustained efforts to reduce litter, promote responsible waste management and create cleaner communities."),
 ("Star Campus Awards","Recognises educational campuses advancing renewable energy, rainwater harvesting, climate education, green audits, waste management, biodiversity and community engagement.")]

CATS = [
    ("OPOP Stars", "One Planet One People Stars honoring collective community environmental stewardship."),
    ("Earth Day Heroes", "Grassroots pioneers driving transformative climate resilience across India."),
    ("Star Municipal Leaders", "Urban local bodies implementing circular waste and clean energy models."),
    ("Star Women's Group", "Women-led self-help groups and cooperatives spearheading green economies."),
    ("Earth Day Rising Stars", "Youth advocates and school students leading conservation innovation."),
    ("Earth Day Stars", "Exemplary citizens and mentors mobilizing millions for Earth Day action."),
    ("Village Awards", "Rural panchayats demonstrating self-reliance in water and clean energy."),
    ("Young Earthpreneurs", "Next-generation entrepreneurs creating market-tested green enterprises."),
    ("Clean Cooking Stars", "Rural leaders advancing clean-cooking fuels and indoor air health."),
    ("Litter Free India Champions", "Local coalitions ending single-use plastics and restoring public spaces."),
    ("Panchayat Champions", "Local self-governance bodies advancing ecological conservation."),
    ("Faith Sites", "Religious and spiritual institutions advancing renewable energy and waste circularity."),
    ("Special Recognition Awards", "Special honors for pioneering contributions to India's environmental security."),
    ("Star Campus Awards", "Universities and schools operating climate-neutral, zero-waste campuses.")
]

def awards():
    lst = "".join(f'''<li class="award-card reveal">
  <div class="award-badge-icon">{MEDAL}</div>
  <div class="award-info">
    <h3>{t}</h3>
    <p>{dsc}</p>
    <a class="link-arrow" href="join-us.html#forms">Nominate / Enquire {ARROW}</a>
  </div>
</li>''' for t,dsc in AW9)

    cats = "".join(f'''<li class="category-card reveal">
  <div class="category-header">
    <span class="medal">{MEDAL}</span>
    <h3>{c}</h3>
  </div>
  <p class="category-desc">{d}</p>
  <span class="category-tag">Logo &middot; List &middot; Bios to come</span>
  <a class="link-arrow" href="join-us.html#forms">Register interest {ARROW}</a>
</li>''' for c, d in CATS)

    groups = [("energy","Energy","Awards recognising renewable energy, energy literacy, and clean cooking transitions."),
              ("institutional","Institutional","Awards for municipal corporations, universities, schools, and faith sites."),
              ("group","Group","Awards for women's groups, village panchayats, and civic cleanup coalitions."),
              ("geographical","Geographical","Awards recognising regional, district, and state-level environmental stewardship."),
              ("individual","Individual","Awards honoring Earth Day Heroes, Rising Stars, and youth green innovators.")]
    grp = "".join(f'<li id="{a}" class="group-box reveal"><span class="k">{i+1:02d}</span><h3>{t}</h3><p>{dsc}</p><a class="link-arrow" href="#all-awards">View categories {ARROW}</a></li>' for i,(a,t,dsc) in enumerate(groups))

    body = f'''{page_hero("Awards","Awards and Recognitions","We believe there is no time to lose.","gallery-6.jpg",f"Mango tree in flower — {ORG} awards and recognitions","awards.html")}
{subnav([("Overview","overview"),("Our Awards","our-awards"),("Browse by type","browse"),("All award categories","all-awards")])}
<section class="section paper-white" id="overview" aria-labelledby="ov-h"><div class="wrap editorial"><div class="side">{eyebrow("Overview","left")}<h2 id="ov-h">Why We Recognise</h2></div>
 <div><p class="dropcap">We believe there is no time to lose. Many effective environmental solutions are already delivering results and can be adapted and replicated without reinventing the wheel. Our awards identify, recognise and showcase these proven initiatives so that they can inspire wider action and accelerate meaningful change.</p>
 <div class="xlinks"><p class="big-stat mb-0">400<em>+</em></p><p class="mb-0">Star Awards and recognitions presented to villages, women's groups, environmental leaders, clean-cooking champions, educational institutions, municipalities and religious sites advancing sustainability.</p></div></div>
</div></section>
<section class="section paper" id="our-awards" aria-labelledby="oa-h"><div class="wrap"><div class="section-head">{eyebrow("No. 01","left")}<h2 id="oa-h">Our Awards</h2><p class="lede">Recognising excellence across grassroots, civic, and institutional environmental action.</p></div><ul class="award-cards-grid">{lst}</ul></div></section>
<section class="section paper-white tight" id="browse" aria-labelledby="br-h"><div class="wrap"><div class="section-head">{eyebrow("No. 02","left")}<h2 id="br-h">Browse by Type</h2><p class="notice">Grouped by sector to highlight focused impacts across India.</p></div><ul class="groups-grid">{grp}</ul></div></section>
<section class="section navy" id="all-awards" aria-labelledby="aa-h"><div class="wrap"><div class="section-head center">{eyebrow("No. 03")}<h2 id="aa-h">All Award Categories</h2><p class="lede">Proven initiatives across 14 dedicated categories. Nominations and enquiries open.</p></div><ul class="categories-ledger">{cats}</ul>
<p class="center mt-l"><a class="btn" href="join-us.html#forms" data-track="CTA: Nominate">Register interest / Nominate {ARROW}</a></p></div></section>'''
    page("awards.html", f"Awards and Recognitions | Earth Day Heroes & Star Awards — {ORG}",
         f"{ORG} awards recognise proven environmental solutions in India: Earth Day Heroes, Star Municipal Leaders, Star Women's Group, Rising Stars, Village Awards and more.",
         "awards.html", body, crumbs=[("Home","index.html"),("Awards","awards.html")])

def events():
    up = [("22","Apr 2027","Earth Day 2027","upcoming","Upcoming",f'Commemorated every year on April 22. <a href="{GLOBAL_THEME_URL}" target="_blank" rel="noopener">Global theme: Food for Our Planet™<span class="sr-only"> (opens in a new tab)</span></a>.'),
          ("TBC","Date","Cleanup Day","upcoming","Upcoming","Beach, lake and river cleanup drives across multiple states. Details to be announced."),
          ("Ongoing","Active","Young Climate Champions (YCC)","ongoing","Ongoing","Part of the JSW–The Times of India Earth Care Awards, reaching college youth across India."),
          ("2025","Archive","National Climate Assemblies","past","Past event","Student assemblies uniting educators and students across 1,00,000+ schools."),
          ("2024","Archive","Ganga River Basin Cleanups","past","Past event","Community waste cleanups from Devprayag to Ganga Sagar."),
          ("Press","Coverage","National Press & Television Features","news","In News","Coverage of Earth Day Network India initiatives, Energy Swaraj Yatra, and Morning Assembly broadcasts.")]

    rows = "".join(f'''<li class="ev-row reveal" data-category="{cat}">
  <p class="ev-date mb-0"><span class="d">{dd}</span><span class="m">{m}</span></p>
  <div class="ev-info">
    <span class="status status-{cat}">{s}</span>
    <h3>{t}</h3>
    <p>{p} {tag() if "TBC" in dd else ""}</p>
  </div>
  <a class="btn outline" href="join-us.html#forms" data-track="CTA: Event interest">Register interest</a>
</li>''' for dd,m,t,cat,s,p in up)

    past = [("Awards in Mumbai","gallery-5.jpg"),("Save the Beach","program-cleanup.jpg"),("Sundarbans","gallery-1.jpg")]
    pc = "".join(f'<li><a class="past-card reveal" href="#past-{i+1}" id="past-{i+1}"><figure class="frame ratio-43 archival archival-hover"><div class="fi">{picture(img, f"{t} — major past event placeholder photo", "(max-width:640px) 100vw, 33vw")}</div></figure><span class="status past">Past event</span><h3>{t}</h3><p>Event page link to be supplied.</p></a></li>' for i,(t,img) in enumerate(past))
    news = "".join('<li><span class="date">Date TBC</span><div><h3>Publication · Headline placeholder</h3><p>Coverage summary and link to be supplied.</p></div></li>' for _ in range(5))
    ev_ld = [{"@type":"Event","name":"Earth Day 2027","startDate":"2027-04-22","endDate":"2027-04-22","eventStatus":"https://schema.org/EventScheduled",
              "eventAttendanceMode":"https://schema.org/MixedEventAttendanceMode","description":"Commemorated every year on April 22, Earth Day brings people together across countries, communities and generations to protect our shared planet.",
              "location":{"@type":"Place","name":"India (TODO: venue to be confirmed)","address":{"@type":"PostalAddress","addressCountry":"IN"}},
              "organizer":{"@id":BASE_URL+"/#organization"},"url":BASE_URL+"/events.html#upcoming","image":BASE_URL+"/assets/og/og-default.jpg"}]

    body = f'''{page_hero("Events","Events",f"Upcoming, ongoing and major past events of {ORG}.","show-panel-4.jpg","Ghats on the Ganga, Varanasi — Earth Day India events","events.html")}
{subnav([("Filter Events","events-feed"),("Ongoing Spotlight","ongoing"),("Major Past Events","past"),("EDN in News","news")])}

<section class="section paper-white" id="events-feed" aria-labelledby="feed-h"><div class="wrap">
 <div class="section-head split">
  <div>{eyebrow("Events Feed","left")}<h2 id="feed-h">Calendar &amp; Activities</h2></div>
  <div class="filter-tabs" role="tablist" aria-label="Filter events by category">
   <button class="filter-tab active" role="tab" aria-selected="true" data-filter="all">All</button>
   <button class="filter-tab" role="tab" aria-selected="false" data-filter="upcoming">Upcoming</button>
   <button class="filter-tab" role="tab" aria-selected="false" data-filter="ongoing">Ongoing</button>
   <button class="filter-tab" role="tab" aria-selected="false" data-filter="past">Past</button>
   <button class="filter-tab" role="tab" aria-selected="false" data-filter="news">News</button>
  </div>
 </div>
 <ul class="ev-list" id="events-list">{rows}</ul>
</div></section>

<section class="section navy" id="ongoing" aria-labelledby="on-h"><div class="wrap halves v-center">
 <div>{eyebrow("No. 02 · Ongoing","left")}<p><span class="status live">Ongoing</span></p><h2 id="on-h">Young Climate Champions (YCC)</h2><p class="lede">Young Climate Champions, part of the JSW–The Times of India Earth Care Awards, encourages college students to develop practical, innovative, and scalable solutions to environmental challenges.</p><a class="btn" href="programs.html#youth">Empowering Youth {ARROW}</a></div>
 <figure class="frame ratio-43"><div class="fi">{picture("program-youth.jpg","College students — Young Climate Champions, climate education India","(max-width:980px) 100vw, 560px")}</div></figure>
</div></section>

<section class="section paper" id="past" aria-labelledby="pe-h"><div class="wrap"><div class="section-head">{eyebrow("No. 03 · Archive","left")}<h2 id="pe-h">Major Past Events</h2></div><ul class="past-grid">{pc}</ul></div></section>

<section class="section paper-white" id="news" aria-labelledby="nw-h"><div class="wrap editorial"><div class="side">{eyebrow("No. 04","left")}<h2 id="nw-h">EDN in News</h2><p>Press coverage of {ORG}.</p></div><ul class="news-list">{news}</ul></div></section>'''
    page("events.html", f"Events | Earth Day 2027, Cleanups & Youth — {ORG}",
         f"Upcoming, ongoing and past events of {ORG}: Earth Day 2027, Cleanup Day, Young Climate Champions, and EDN in News. Earth Day, Every Day.",
         "events.html", body, crumbs=[("Home","index.html"),("Events","events.html")], extra_ld=ev_ld)

def resources():
    R = [("reports","Reports","doc","Programme and impact reports.","reports"),
         ("brochure","Brochure","fold","Organisation brochure.","brochure"),
         ("ppt","PPT","slides","Presentation decks.","educational"),
         ("branding","Branding Usage with Guidelines","brand","Social media use, tags, logo usage, banner placements.","guides"),
         ("ebooks","Ebooks","book","Downloadable ebooks for eco-literacy.","educational"),
         ("videos","Videos","video","Video library on YouTube and multimedia.","media"),
         ("courses","Courses - Energy Literacy","cap","Energy Literacy courses with Energy Swaraj Foundation.","educational"),
         ("eco-games","Eco games","game","Interactive games for environmental learning.","educational"),
         ("merch","Merch","bag","Sustainable merchandise.","guides"),
         ("books","Link to our books","shelf","Our authored books and printed resources.","educational")]

    rows = "".join(f'''<li id="{a}" class="res-item reveal" data-filter-group="{cat}">
  <span class="rn">{i+1:02d}</span>
  <span class="ic">{icon(ic)}</span>
  <div class="res-body">
    <h3>{t}</h3>
    <p>{dsc} Files and links to be supplied.</p>
  </div>
  <span class="res-badge soon">Coming soon</span>
</li>''' for i,(a,t,ic,dsc,cat) in enumerate(R))

    body = f'''{page_hero("Resources","Resources","Reports, brochures, branding guidelines, ebooks, videos, courses and more for environmental and climate education in India.","gallery-3.jpg",f"Handloom weaver — {ORG} resources","resources.html")}
<section class="section paper-white" aria-labelledby="lib-h"><div class="wrap editorial">
 <div class="side">
  {eyebrow("Library","left")}
  <h2 id="lib-h">Resource Library</h2>
  <p>An index of everything we publish. Each entry will link to a download, a viewer or an external course page.</p>
  <div class="filter-tabs filter-tabs-vertical mt-l" role="tablist" aria-label="Filter resources by type">
   <button class="filter-tab active" role="tab" aria-selected="true" data-filter="all">All Resources</button>
   <button class="filter-tab" role="tab" aria-selected="false" data-filter="reports">Reports</button>
   <button class="filter-tab" role="tab" aria-selected="false" data-filter="educational">Educational</button>
   <button class="filter-tab" role="tab" aria-selected="false" data-filter="media">Media</button>
   <button class="filter-tab" role="tab" aria-selected="false" data-filter="guides">Guides</button>
  </div>
  <a class="link-arrow mt-l" href="programs.html#education">Our education work {ARROW}</a>
 </div>
 <ul class="res-index" id="resources-list">{rows}</ul>
</div></section>
<section class="section navy" aria-labelledby="ft-h"><div class="wrap halves v-center">
 <div>{eyebrow("Featured","left")}<h2 id="ft-h">Courses - Energy Literacy</h2><p class="lede">In partnership with the Energy Swaraj Foundation, we advance energy literacy and encourage energy conservation, responsible consumption and the transition to renewable energy.</p><a class="btn" href="programs.html#energy">Clean energy programme {ARROW}</a></div>
 <div class="slot"><div><strong>Featured resource</strong>Cover image / course link placeholder.</div></div>
</div></section>'''
    page("resources.html", f"Resources | Reports, Ebooks & Climate Education India — {ORG}",
         f"{ORG} resources: reports, brochure, branding guidelines, ebooks, videos, Energy Literacy courses, eco games and books for climate education in India.",
         "resources.html", body, crumbs=[("Home","index.html"),("Resources","resources.html")])

FAQS_JOIN = [
    ("How can my organisation partner with Earth Day Network India?",
     f"Organisations across corporate, government, education, research, and civil society sectors can collaborate with {ORG} on nationwide tree planting, clean energy awareness, youth climate literacy, and community cleanups. Submit our Partner form below to start a conversation."),
    ("Is Earth Day Network India eligible for CSR funding?",
     f"Yes. {ORG} is a registered trust holding CSR-1 Certification from the Ministry of Corporate Affairs, 12A registration under the Government of India's Income Tax Act, and NITI Aayog's NGO Darpan registration."),
    ("How can individuals volunteer for Earth Day initiatives?",
     f"Individuals can participate in local community cleanups, tree planting drives, morning assembly school networks, and youth awareness campaigns. Submit our Volunteer form to join the volunteer roster."),
    ("How do I nominate an individual or group for an Earth Day Award?",
     f"Nominations and enquiries for Earth Day Heroes, Star Municipal Leaders, Star Women's Group, Rising Stars, and other awards can be submitted directly through our Project Interest Forms under 'Other project interest'."),
    ("How can schools and universities participate in environmental programmes?",
     f"Educational institutions can engage in our Morning Assembly Network, Young Climate Champions, Climate Clock assemblies, Eco-Comics workshops, and Star Campus green audits by registering interest on our website."),
    ("What is the procedure for plantation and green project requests?",
     f"Communities, panchayats, and partner organisations can request fruit-tree saplings and reforestation support by selecting 'Plantation' on our Project Interest Forms.")
]

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

def join():
    names = "".join(f"<li>{n}</li>" for n in PARTNER_NAMES)
    vol = (field("v-name","name","Full name",auto="name") + field("v-email","email","Email","email",auto="email")
           + field("v-phone","phone","Phone","tel",req=False,auto="tel",extra=' pattern="[0-9+ ()-]{7,20}" data-pattern-msg="Use digits, spaces, + or - only."')
           + field("v-city","city","City",auto="address-level2")
           + '<div class="field full"><label for="v-interest">Area of interest <span class="req" aria-hidden="true">*</span></label><select id="v-interest" name="interest" required aria-required="true" aria-describedby="v-interest-err"><option value="">Choose one…</option><option>Cleanups</option><option>Tree planting</option><option>Education</option><option>Events</option><option>Other</option></select><span class="err" id="v-interest-err" aria-live="polite"></span></div>'
           + field("v-msg","message","Tell us a little about yourself","textarea",req=False,full=True))
    par = (field("p-name","name","Contact name",auto="name") + field("p-org","organisation","Organisation",auto="organization")
           + field("p-email","email","Work email","email",auto="email") + field("p-phone","phone","Phone","tel",req=False,auto="tel",extra=' pattern="[0-9+ ()-]{7,20}" data-pattern-msg="Use digits, spaces, + or - only."')
           + '<div class="field full"><label for="p-type">Form <span class="req" aria-hidden="true">*</span></label><select id="p-type" name="form_type" required aria-required="true" aria-describedby="p-type-err"><option value="">Choose one…</option><option>Partner (Common Link)</option><option>CSR Focus</option><option>Plantation</option><option>Other project interest</option></select><span class="err" id="p-type-err" aria-live="polite"></span></div>'
           + field("p-msg","message","How would you like to work with us?","textarea",full=True))
    recaptcha = '<p class="notice">Spam protection: honeypot field enabled. Optional: enable Netlify reCAPTCHA by adding <code>data-netlify-recaptcha="true"</code> and a <code>&lt;div data-netlify-recaptcha="true"&gt;</code> (update the CSP if you do).</p>'

    faq_items = []
    for i, (q, a) in enumerate(FAQS_JOIN):
        fid = f"faq-jn-{i+1}"
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

    body = f'''{page_hero("Join Us","Join Us","Every act counts. Collective action multiplies its impact.","show-panel-2.jpg",f"Rice fields in Kerala — join {ORG}, environmental nonprofit India","join-us.html")}
{subnav([("Ways to Join","ways-to-join"),("CSR Focus","csr"),("Partner","partner"),("Call to Action","cta"),("Volunteer","volunteer"),("Project Interest Forms","forms"),("FAQ","join-faq")])}
<section class="section paper-white tight" id="ways-to-join" aria-labelledby="ways-h"><div class="wrap"><h2 id="ways-h" class="sr-only">Ways to join</h2><ul class="join-paths">
 <li><a href="#csr"><span class="k">01</span><h3>CSR Focus</h3><p>For businesses and CSR teams.</p><span class="link-arrow">Read more {ARROW}</span></a></li>
 <li><a href="#partner"><span class="k">02</span><h3>Partner</h3><p>Partner With Us.</p><span class="link-arrow">Read more {ARROW}</span></a></li>
 <li><a href="#volunteer"><span class="k">03</span><h3>Volunteer</h3><p>Volunteer form.</p><span class="link-arrow">Go to form {ARROW}</span></a></li>
 <li><a href="#forms"><span class="k">04</span><h3>Project Interest Forms</h3><p>Other forms (e.g., Plantation).</p><span class="link-arrow">Go to form {ARROW}</span></a></li>
</ul></div></section>
<section class="section paper" id="csr" aria-labelledby="csr-h"><div class="wrap editorial"><div class="side">{eyebrow("No. 01","left")}<h2 id="csr-h">CSR Focus</h2></div>
 <div><p class="lede strong">We also believe that sustainability and profitability can go hand in hand, and we work with businesses to identify practical pathways to go green, reduce environmental impact, create value and build long-term sustainable growth.</p>
 <p>{ORG} also holds NITI Aayog's NGO Darpan registration and 12A registration under the Government of India's Income Tax Act, and CSR-1 Certification from the Ministry of Corporate Affairs.</p>
 <p class="notice">CSR focus areas and details to be supplied by the client.</p>
 <div class="xlinks"><a class="btn solid-navy" href="#forms" data-track="CTA: CSR enquiry">CSR enquiry {ARROW}</a></div></div></div></section>
<section class="section paper-white" id="partner" aria-labelledby="par-h"><div class="wrap editorial"><div class="side">{eyebrow("No. 02","left")}<h2 id="par-h">Partner With Us</h2><a class="btn" href="#forms" data-track="CTA: Partner form">Partner form {ARROW}</a></div>
 <div><p class="dropcap">{ORG} has worked with and engaged more than 130 organisations across the corporate, government, education, research, nonprofit and community sectors. These include the Ministry of Environment, Forest and Climate Change, UNICEF, UNESCO-MGIEP, the National Service Scheme, National Cadet Corps, WWF, TERI, the Centre for Environment Education, Tata Power, ITC, UPS, BBC Media Action, United Way India, SEWA, the Energy Swaraj Foundation, Oxford University (Said School of Business), KIIT and Banaras Hindu University.</p>
 <p>Our partnerships bring technical expertise, institutional networks, community knowledge and on-the-ground implementation. We welcome partners who can help expand meaningful programmes, strengthen measurable outcomes and replicate successful approaches across India.</p>
 <h3 class="mt-l">Among the organisations we have worked with</h3><ul class="partner-names">{names}</ul></div></div></section>
<section class="section navy" id="cta" aria-labelledby="cta-h"><div class="wrap center narrow">
 {eyebrow("Call to Action")}<h2 id="cta-h">Every act counts. Collective action multiplies its impact.</h2>
 <figure class="mb-0"><blockquote class="pull">We need all hands on deck—and many more green actions—to build a healthier, more sustainable world that benefits everyone, today and for generations to come.</blockquote></figure>
 <p class="lede mt-l">Whether you are an individual, educational institution, community organisation, business or funder, you can help advance practical environmental action across India. Join a programme, share your expertise, support an initiative or partner with us to take proven solutions further.</p>
 <div class="btns btns-center"><a class="btn" href="#forms" data-track="CTA: Partner With Us (Join)">Partner With Us {ARROW}</a><a class="btn ghost" href="#volunteer" data-track="CTA: Volunteer">Volunteer</a></div>
</div></section>
<section class="section paper-white" id="volunteer" aria-labelledby="vol-h"><div class="wrap editorial"><div class="side">{eyebrow("No. 03","left")}<h2 id="vol-h">Volunteer</h2><p>Fields marked <span class="req">*</span> are required. We use your details only to respond — see our <a href="privacy-policy.html">privacy policy</a>.</p></div><div>{netlify_form("volunteer","v",vol,"Send volunteer form")}</div></div></section>
<section class="section paper" id="forms" aria-labelledby="pif-h"><div class="wrap editorial"><div class="side">{eyebrow("No. 04","left")}<h2 id="pif-h">Project Interest Forms</h2><p>Partner (common link), CSR and other forms (e.g., Plantation).</p></div><div>{netlify_form("partner","p",par,"Send enquiry",note=recaptcha)}</div></div></section>

<!-- COMPREHENSIVE FAQ ACCORDION -->
<section class="section paper-white" id="join-faq" aria-labelledby="jfaq-h"><div class="wrap narrow">
 <div class="section-head center"><span class="num">No. 05</span>{eyebrow("Frequently Asked Questions")}<h2 id="jfaq-h">Frequently Asked Questions</h2><p class="lede">Common questions about partnering, volunteering, CSR eligibility and projects with {ORG}.</p></div>
 <div class="faq-accordion" data-accordion>{faq_html}</div>
</div></section>
'''
    extra_ld = faq_ld(FAQS_JOIN)
    page("join-us.html", f"Join Us | Partner, CSR & Volunteer — {ORG}",
         f"Join {ORG}, an environmental NGO in India: CSR focus, partner with us, volunteer and project interest forms. Every act counts.",
         "join-us.html", body, crumbs=[("Home","index.html"),("Join Us","join-us.html")], extra_ld=extra_ld, priority="0.9")
