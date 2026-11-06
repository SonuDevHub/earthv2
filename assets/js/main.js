/* Earth Day Network India — site script (vanilla JS; minified into assets/js at build time) */
(function () {
  "use strict";
  var d = document, root = d.documentElement, body = d.body;
  root.classList.add("js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $$ = function (s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); };

  /* ---------- Analytics hooks (cookieless; no-op until Umami/Plausible is enabled) ---------- */
  function track(name, props) {
    try {
      if (window.umami && typeof window.umami.track === "function") window.umami.track(name, props);
      else if (typeof window.plausible === "function") window.plausible(name, { props: props });
    } catch (e) { /* never break the page for analytics */ }
  }
  window.ednTrack = track;
  d.addEventListener("click", function (e) {
    var a = e.target.closest ? e.target.closest("a,button") : null;
    if (!a) return;
    if (a.dataset.track) track(a.dataset.track, { label: (a.textContent || "").trim().slice(0, 60), page: location.pathname });
    var href = a.getAttribute("href") || "";
    if (href.indexOf("tel:") === 0) track("Phone tap", { page: location.pathname });
    else if (href.indexOf("mailto:") === 0) track("Email tap", { page: location.pathname });
    else if (a.dataset.social) track("Outbound social", { network: a.dataset.social });
    else if (/^https?:/i.test(href) && a.host !== location.host) track("Outbound link", { url: href });
  });

  /* ---------- Placeholder socials: don't jump to top ---------- */
  $$("a[data-social][href='#']").forEach(function (a) {
    a.addEventListener("click", function (e) { e.preventDefault(); });
  });
  var yr = d.getElementById("year"); if (yr) yr.textContent = new Date().getFullYear();

  /* ---------- Navigation: mobile panel + disclosure dropdowns ---------- */
  var toggle = d.querySelector(".menu-toggle");
  var siteHeader = d.querySelector(".site-header");
  function updateNavTop() {
    if (siteHeader) {
      var rect = siteHeader.getBoundingClientRect();
      var topVal = Math.max(0, Math.round(rect.bottom));
      root.style.setProperty("--nav-top", topVal + "px");
    }
  }
  updateNavTop();
  window.addEventListener("resize", updateNavTop);
  window.addEventListener("scroll", updateNavTop, { passive: true });

  function closeMenu() { body.classList.remove("menu-open"); if (toggle) { toggle.setAttribute("aria-expanded", "false"); toggle.setAttribute("aria-label", "Open menu"); } }
  if (toggle) toggle.addEventListener("click", function () {
    updateNavTop();
    var open = body.classList.toggle("menu-open");
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  });
  function closeAllDD(except) {
    $$(".nav li.has-dd.open").forEach(function (li) {
      if (li === except) return;
      li.classList.remove("open");
      var b = li.querySelector(".dd-btn"); if (b) b.setAttribute("aria-expanded", "false");
    });
  }
  $$(".nav .dd-btn").forEach(function (btn) {
    var li = btn.parentElement;
    btn.addEventListener("click", function () {
      var open = !li.classList.contains("open");
      closeAllDD(li);
      li.classList.toggle("open", open);
      btn.setAttribute("aria-expanded", String(open));
      if (open && window.innerWidth > 980) { var f = li.querySelector(".dropdown a"); if (f) f.focus(); }
    });
    li.addEventListener("keydown", function (e) {
      var links = $$(".dropdown a", li), i = links.indexOf(d.activeElement);
      if (e.key === "Escape" && li.classList.contains("open")) { li.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); btn.focus(); e.stopPropagation(); }
      else if (e.key === "ArrowDown" && li.classList.contains("open")) { e.preventDefault(); (links[i + 1] || links[0]).focus(); }
      else if (e.key === "ArrowUp" && li.classList.contains("open")) { e.preventDefault(); (links[i - 1] || links[links.length - 1]).focus(); }
    });
    li.addEventListener("focusout", function (e) { if (!li.contains(e.relatedTarget) && window.innerWidth > 980) { li.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); } });
  });
  d.addEventListener("click", function (e) { if (!e.target.closest(".nav") && !e.target.closest(".menu-toggle")) closeAllDD(); });
  d.addEventListener("keydown", function (e) { if (e.key === "Escape") { closeAllDD(); if (body.classList.contains("menu-open")) { closeMenu(); if (toggle) toggle.focus(); } } });
  $$(".nav a").forEach(function (a) {
    a.addEventListener("click", function () {
      closeMenu();
      closeAllDD();
    });
  });
  $$(".nav-contact-link, a[href='#contact']").forEach(function (link) {
    link.addEventListener("click", function (e) {
      closeMenu();
      closeAllDD();
      var target = d.getElementById("contact");
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: reduce ? "auto" : "smooth" });
      }
    });
  });
  window.addEventListener("resize", function () {
    if (window.innerWidth > 980 && body.classList.contains("menu-open")) {
      closeMenu();
      closeAllDD();
    }
  });

  /* ---------- Hero slider (video slide 0 support, keyboard, reduced motion) ---------- */
  var hero = d.querySelector(".hero");
  if (hero) {
    var slides = $$(".slide", hero), dots = $$(".hero-dots button", hero);
    var label = hero.querySelector(".slide-label b"), live = hero.querySelector(".hero-live");
    var pauseBtn = hero.querySelector(".ctl.pause"), idx = 0, timer = null, paused = reduce, hover = false, warm = false;
    var show = function (n, announce) {
      idx = (n + slides.length) % slides.length;
      slides[idx].classList.add("prep"); if (warm) slides[(idx + 1) % slides.length].classList.add("prep");
      slides.forEach(function (s, i) { var on = i === idx; s.classList.toggle("is-active", on); s.setAttribute("aria-hidden", String(!on)); });
      dots.forEach(function (b, i) { b.setAttribute("aria-current", String(i === idx)); });
      if (label) label.textContent = slides[idx].dataset.label;
      if (announce && live) live.textContent = "Slide " + (idx + 1) + " of " + slides.length + ": " + slides[idx].dataset.label;
    };
    var stop = function () { clearInterval(timer); timer = null; };
    var play = function () { stop(); if (!paused && !hover) timer = setInterval(function () { show(idx + 1, false); }, 7500); };
    dots.forEach(function (b, i) { b.addEventListener("click", function () { show(i, true); play(); }); });
    var prevBtn = hero.querySelector(".ctl.prev"), nextBtn = hero.querySelector(".ctl.next");
    if (prevBtn) prevBtn.addEventListener("click", function () { show(idx - 1, true); play(); });
    if (nextBtn) nextBtn.addEventListener("click", function () { show(idx + 1, true); play(); });
    if (pauseBtn) {
      pauseBtn.setAttribute("aria-pressed", String(paused));
      pauseBtn.setAttribute("aria-label", paused ? "Play slideshow" : "Pause slideshow");
      pauseBtn.addEventListener("click", function () {
        paused = !paused;
        pauseBtn.setAttribute("aria-pressed", String(paused));
        pauseBtn.setAttribute("aria-label", paused ? "Play slideshow" : "Pause slideshow");
        play();
      });
    }
    hero.addEventListener("mouseenter", function () { hover = true; stop(); });
    hero.addEventListener("mouseleave", function () { hover = false; play(); });
    hero.addEventListener("focusin", function () { hover = true; stop(); });
    hero.addEventListener("focusout", function () { hover = false; play(); });
    hero.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") { show(idx + 1, true); } else if (e.key === "ArrowLeft") { show(idx - 1, true); }
    });
    d.addEventListener("visibilitychange", function () { if (d.hidden) stop(); else play(); });
    show(0, false); play();
    window.addEventListener("load", function () { setTimeout(function () { warm = true; if (slides.length > 1) slides[1].classList.add("prep"); }, 1500); });
  }

  /* ---------- Count-up (Indian digit grouping) ---------- */
  var fmt = function (v, dec) { return v.toLocaleString("en-IN", { minimumFractionDigits: dec, maximumFractionDigits: dec }); };
  function countUp(el) {
    var target = parseFloat(el.dataset.count || el.dataset.target), dec = parseInt(el.dataset.dec || "0", 10), pre = el.dataset.prefix || "", suf = el.dataset.suffix || "";
    if (isNaN(target)) return;
    var out = el.querySelector("[aria-hidden]") || el;
    if (reduce) { if (el.dataset.final) out.textContent = el.dataset.final; return; }
    var start = null, dur = 1400;
    var step = function (t) {
      if (!start) start = t;
      var p = Math.min((t - start) / dur, 1), k = 1 - Math.pow(1 - p, 3);
      if (el.dataset.final && p >= 1) { out.textContent = el.dataset.final; return; }
      out.textContent = pre + fmt(dec ? target * k : Math.round(target * k), dec) + suf;
      if (p < 1) requestAnimationFrame(step);
      else if (el.dataset.final) out.textContent = el.dataset.final;
    };
    requestAnimationFrame(step);
  }

  /* ---------- Reveal + counters + lazy map ---------- */
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      var t = en.target;
      t.classList.add("in");
      if (t.dataset.count || t.dataset.target) countUp(t);
      if (t.id === "map") initMap(t);
      if (t.id === "earth-canvas-container") initGlobe();
      io.unobserve(t);
    });
  }, { rootMargin: "0px 0px -6% 0px", threshold: 0.08 }) : null;

  $$(".reveal,[data-count],.counter,#map,#earth-canvas-container").forEach(function (el) {
    if (io) io.observe(el); else { el.classList.add("in"); if (el.dataset.count || el.dataset.target) countUp(el); if (el.id === "map") initMap(el); if (el.id === "earth-canvas-container") initGlobe(); }
  });

  /* ---------- Programme carousel ---------- */
  $$(".carousel-track").forEach(function (track) {
    var by = function () { var li = track.querySelector("li"); return li ? li.getBoundingClientRect().width + 20 : 300; };
    var prev = d.querySelector('.c-prev[aria-controls="' + track.id + '"]'), next = d.querySelector('.c-next[aria-controls="' + track.id + '"]');
    var beh = reduce ? "auto" : "smooth";
    if (prev) prev.addEventListener("click", function () { track.scrollBy({ left: -by(), behavior: beh }); });
    if (next) next.addEventListener("click", function () {
      if (track.scrollLeft + track.clientWidth >= track.scrollWidth - 4) track.scrollTo({ left: 0, behavior: beh });
      else track.scrollBy({ left: by(), behavior: beh });
    });
  });

  /* ---------- Map (Leaflet + OSM tiles), loaded only when scrolled into view ---------- */
  function initMap(el) {
    if (el.dataset.ready) return; el.dataset.ready = "1";
    var css = d.createElement("link"); css.rel = "stylesheet"; css.href = el.dataset.css; d.head.appendChild(css);
    var s = d.createElement("script"); s.src = el.dataset.js; s.defer = true;
    s.onload = function () {
      var L = window.L; if (!L) return;
      L.Icon.Default.imagePath = el.dataset.img;
      var map = L.map(el, { scrollWheelZoom: false }).setView([22.5, 80.5], 4);
      L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", { maxZoom: 18, attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors' }).addTo(map);
      JSON.parse(el.dataset.pins).forEach(function (p) {
        L.marker([p[0], p[1]], { alt: p[2], title: p[2], keyboard: true }).addTo(map).bindPopup("<strong>" + p[2] + "</strong><br>" + p[3]);
      });
      el.setAttribute("tabindex", "0");
    };
    s.onerror = function () { el.innerHTML = '<p class="map-fallback">The map could not be loaded.</p>'; };
    d.body.appendChild(s);
  }

  /* ---------- Click-to-load embeds ---------- */
  $$("button.facade").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var src = btn.dataset.src, box = btn.parentElement;
      if (!src) { var f = btn.querySelector(".fine"); if (f) f.textContent = "Not connected yet — the client's channel/post URL still needs to be added."; return; }
      var ifr = d.createElement("iframe");
      ifr.src = src; ifr.title = btn.dataset.title || "Embedded media"; ifr.loading = "lazy";
      ifr.allow = "accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen";
      ifr.referrerPolicy = "strict-origin-when-cross-origin";
      box.replaceChild(ifr, btn); ifr.focus && ifr.focus();
      track("Embed loaded", { type: btn.dataset.kind });
    });
  });

  /* ---------- Forms: progressive validation ---------- */
  $$("form[data-validate]").forEach(function (form) {
    form.setAttribute("novalidate", "");
    var fields = $$("input,textarea,select", form).filter(function (f) { return f.name && f.type !== "hidden" && !f.closest(".hp"); });
    function msg(f) {
      if (f.validity.valueMissing) return f.type === "checkbox" ? "Please tick this box to continue." : "This field is required.";
      if (f.validity.typeMismatch && f.type === "email") return "Please enter a valid email address.";
      if (f.validity.patternMismatch) return f.dataset.patternMsg || "Please check the format.";
      if (f.validity.tooShort) return "Please enter at least " + f.minLength + " characters.";
      return "";
    }
    function check(f) {
      var wrap = f.closest(".field"), err = wrap && wrap.querySelector(".err"), m = msg(f);
      if (wrap) wrap.classList.toggle("invalid", !!m);
      f.setAttribute("aria-invalid", String(!!m));
      if (err) err.textContent = m;
      return !m;
    }
    fields.forEach(function (f) {
      f.addEventListener("blur", function () { if (f.value || f.type === "checkbox") check(f); });
      f.addEventListener("input", function () { if (f.closest(".field.invalid")) check(f); });
    });
    form.addEventListener("submit", function (e) {
      var firstBad = null;
      fields.forEach(function (f) { if (!check(f) && !firstBad) firstBad = f; });
      if (firstBad) { e.preventDefault(); firstBad.focus(); var st = form.querySelector(".form-status"); if (st) st.textContent = "Please correct the highlighted fields."; return; }
      track("Form submit", { form: form.getAttribute("name") });
    });
  });

  /* ---------- Interactive 3D Earth Globe ---------- */
  function initGlobe() {
    var container = d.getElementById("earth-canvas-container");
    if (!container || container.dataset.ready) return;
    container.dataset.ready = "1";

    function loadScript(src) {
      return new Promise(function (resolve, reject) {
        var s = d.createElement("script");
        s.src = src; s.defer = true;
        s.onload = resolve; s.onerror = reject;
        d.body.appendChild(s);
      });
    }

    loadScript("assets/vendor/three/three.min.js").then(function () {
      if (typeof THREE === "undefined") return;
      setupThreeGlobe(container);
    }).catch(function (err) {
      console.warn("Could not load Three.js, fallback shown.", err);
    });
  }

  function setupThreeGlobe(container) {
    var width = container.clientWidth || 600, height = container.clientHeight || 500;
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    camera.position.z = 2.9;

    var renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, powerPreference: "high-performance" });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    var canvas = renderer.domElement;
    canvas.className = "earth-canvas";
    canvas.style.touchAction = "pan-y";
    container.appendChild(canvas);

    var globeGroup = new THREE.Group();
    scene.add(globeGroup);

    // Lights
    var ambient = new THREE.AmbientLight(0xdde8f5, 0.7);
    scene.add(ambient);
    var sun = new THREE.DirectionalLight(0xffffff, 1.2);
    sun.position.set(5, 3, 5);
    scene.add(sun);
    var fill = new THREE.DirectionalLight(0x2f83a6, 0.4);
    fill.position.set(-5, -2, -3);
    scene.add(fill);

    // Textures & Earth Sphere
    var loader = new THREE.TextureLoader();
    var earthTex = loader.load("assets/earth/earth-day.jpg");
    var earthMat = new THREE.MeshPhongMaterial({ map: earthTex, shininess: 12, specular: new THREE.Color(0x223344) });
    var earthMesh = new THREE.Mesh(new THREE.SphereGeometry(1.0, 48, 48), earthMat);
    globeGroup.add(earthMesh);

    // Clouds
    var cloudsTex = loader.load("assets/earth/earth-clouds.png");
    var cloudsMat = new THREE.MeshLambertMaterial({ map: cloudsTex, transparent: true, opacity: 0.35, blending: THREE.AdditiveBlending });
    var cloudsMesh = new THREE.Mesh(new THREE.SphereGeometry(1.012, 48, 48), cloudsMat);
    globeGroup.add(cloudsMesh);

    // Atmosphere Rim
    var atmosMat = new THREE.ShaderMaterial({
      vertexShader: "varying vec3 vN; void main(){ vN = normalize(normalMatrix * normal); gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }",
      fragmentShader: "varying vec3 vN; void main(){ float i = pow(0.65 - dot(vN, vec3(0,0,1.0)), 2.0); gl_FragColor = vec4(0.447, 0.71, 0.725, 1.0) * i * 0.7; }",
      blending: THREE.AdditiveBlending, side: THREE.BackSide, transparent: true
    });
    var atmosMesh = new THREE.Mesh(new THREE.SphereGeometry(1.11, 36, 36), atmosMat);
    scene.add(atmosMesh);

    // Markers
    var markersGroup = new THREE.Group();
    globeGroup.add(markersGroup);
    var markerObjs = [];

    fetch("assets/earth/markers.json").then(function (r) { return r.json(); }).then(function (data) {
      data.forEach(function (m, idx) {
        var phi = (90 - m.lat) * (Math.PI / 180);
        var theta = (m.lng + 180) * (Math.PI / 180);
        var x = -(1.0 * Math.sin(phi) * Math.cos(theta));
        var z = (1.0 * Math.sin(phi) * Math.sin(theta));
        var y = (1.0 * Math.cos(phi));

        var col = 0xF37321; // Orange
        var cat = (m.category || m.type || "").toLowerCase();
        if (cat.indexOf("forest") !== -1 || cat.indexOf("canopy") !== -1) col = 0x72B5B9;
        else if (cat.indexOf("cleanup") !== -1) col = 0x2F83A6;
        else if (cat.indexOf("education") !== -1) col = 0xFDB714;
        else if (cat.indexOf("agriculture") !== -1) col = 0x47A87A;
        else if (cat.indexOf("energy") !== -1) col = 0xFDB714;
        else if (cat.indexOf("youth") !== -1) col = 0xF37321;

        var ringMat = new THREE.MeshBasicMaterial({ color: col, side: THREE.DoubleSide, transparent: true, opacity: 0.9 });
        var ring = new THREE.Mesh(new THREE.RingGeometry(0.02, 0.038, 20), ringMat);
        ring.position.set(x * 1.008, y * 1.008, z * 1.008);
        ring.lookAt(x * 2, y * 2, z * 2);

        var coreMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
        var core = new THREE.Mesh(new THREE.SphereGeometry(0.015, 12, 12), coreMat);
        core.position.set(x * 1.012, y * 1.012, z * 1.012);

        var pin = new THREE.Group();
        pin.add(ring); pin.add(core);
        pin.userData = { data: m, index: idx };
        markersGroup.add(pin);
        markerObjs.push(pin);
      });
    }).catch(function (e) { console.warn("Markers could not be loaded", e); });

    // Interaction state
    var isDragging = false, dragDistance = 0, prevMouse = { x: 0, y: 0 };
    var targetRot = { x: 0.25, y: -1.2 }, currRot = { x: 0.25, y: -1.2 };
    var activeMarker = null, isVisible = true, animId = null;

    var raycaster = new THREE.Raycaster(), mouseVec = new THREE.Vector2();
    var sheet = d.getElementById("globe-sheet"), sheetContent = d.getElementById("globe-sheet-content");
    var sheetClose = d.getElementById("globe-sheet-close");

    if (sheetClose) sheetClose.addEventListener("click", function () {
      activeMarker = null;
      if (sheet) sheet.hidden = true;
      $$(".globe-place-item").forEach(function (b) { b.classList.remove("active"); });
    });

    function showSheet(m) {
      if (!sheet || !sheetContent) return;
      var anc = m.anchor || "programs.html";
      var catLabel = (m.category || m.type || "Programme").toUpperCase();
      sheetContent.innerHTML =
        '<span class="globe-sheet-tag" style="display:inline-block;font-size:0.7rem;font-weight:700;letter-spacing:0.1em;color:var(--orange);text-transform:uppercase;margin-bottom:6px;">' + catLabel + '</span>' +
        '<h4>' + (m.name || "") + '</h4>' +
        '<p class="globe-sheet-loc" style="font-size:0.82rem;color:rgba(255,255,255,0.7);margin-bottom:8px;">' + (m.place || "") + '</p>' +
        '<p class="globe-sheet-desc">' + (m.description || "") + '</p>' +
        (m.stats ? '<p class="globe-sheet-stats" style="font-size:0.8rem;color:var(--yellow);font-weight:700;margin-top:8px;">' + m.stats + '</p>' : '') +
        '<div style="margin-top:14px;"><a class="btn" style="padding:8px 18px;font-size:0.75rem;" href="' + anc + '">Explore in Programmes →</a></div>';
      sheet.hidden = false;
    }

    canvas.addEventListener("pointerdown", function (e) {
      isDragging = true; dragDistance = 0;
      prevMouse = { x: e.clientX, y: e.clientY };
      canvas.style.cursor = "grabbing";
    });

    window.addEventListener("pointermove", function (e) {
      if (!isDragging) {
        var rect = canvas.getBoundingClientRect();
        if (e.clientX >= rect.left && e.clientX <= rect.right && e.clientY >= rect.top && e.clientY <= rect.bottom) {
          mouseVec.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
          mouseVec.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;
          raycaster.setFromCamera(mouseVec, camera);
          var hits = raycaster.intersectObjects(markersGroup.children, true);
          canvas.style.cursor = hits.length > 0 ? "pointer" : "grab";
        }
        return;
      }
      var dx = e.clientX - prevMouse.x, dy = e.clientY - prevMouse.y;
      dragDistance += Math.abs(dx) + Math.abs(dy);
      targetRot.y += dx * 0.005;
      targetRot.x = Math.max(-1.1, Math.min(1.1, targetRot.x + dy * 0.005));
      prevMouse = { x: e.clientX, y: e.clientY };
    });

    window.addEventListener("pointerup", function () {
      isDragging = false; canvas.style.cursor = "grab";
    });

    canvas.addEventListener("click", function (e) {
      if (dragDistance > 6) return;
      var rect = canvas.getBoundingClientRect();
      mouseVec.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
      mouseVec.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;
      raycaster.setFromCamera(mouseVec, camera);
      var hits = raycaster.intersectObjects(markersGroup.children, true);
      if (hits.length > 0) {
        var obj = hits[0].object;
        while (obj && !obj.userData.data && obj.parent) obj = obj.parent;
        if (obj && obj.userData.data) {
          var m = obj.userData.data;
          activeMarker = m;
          var phi = (90 - m.lat) * (Math.PI / 180);
          var theta = (m.lng + 180) * (Math.PI / 180);
          targetRot.x = (phi - Math.PI / 2);
          targetRot.y = -(theta - Math.PI / 2);
          showSheet(m);

          // Highlight corresponding place item
          $$(".globe-place-item").forEach(function (btn) {
            var isThis = btn.dataset.id === m.id || btn.dataset.name === m.name;
            btn.classList.toggle("active", isThis);
            if (isThis && btn.scrollIntoView) {
              btn.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "nearest" });
            }
          });
        }
      }
    });

    // Map Legend Programme Group Filters
    $$(".globe-legend-btn, .globe-filter-btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        $$(".globe-legend-btn, .globe-filter-btn").forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
        var cat = (btn.dataset.filter || "all").toLowerCase();

        var visibleCount = 0;
        var firstMatch = null;
        markerObjs.forEach(function (pin) {
          var m = pin.userData.data; if (!m) return;
          var match = (cat === "all" || m.category === cat || m.category === "all");
          pin.visible = match;
          if (match && !firstMatch && m.lat !== undefined && m.category !== "all") firstMatch = m;
        });

        $$(".globe-place-item").forEach(function (it) {
          var itemCat = (it.dataset.cat || "").toLowerCase();
          var match = (cat === "all" || itemCat === cat || itemCat === "all");
          it.style.display = match ? "flex" : "none";
          if (match) visibleCount++;
        });

        var countEl = d.getElementById("globe-places-count");
        if (countEl) countEl.textContent = visibleCount + (visibleCount === 1 ? " location" : " locations");

        if (firstMatch && cat !== "all") {
          var phi = (90 - firstMatch.lat) * (Math.PI / 180);
          var theta = (firstMatch.lng + 180) * (Math.PI / 180);
          targetRot.x = (phi - Math.PI / 2);
          targetRot.y = -(theta - Math.PI / 2);
        }
      });
    });

    // Interactive Places Directory items
    $$(".globe-place-item").forEach(function (btn) {
      btn.addEventListener("click", function () {
        $$(".globe-place-item").forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
        var lat = parseFloat(btn.dataset.lat), lng = parseFloat(btn.dataset.lng);
        if (!isNaN(lat) && !isNaN(lng)) {
          var phi = (90 - lat) * (Math.PI / 180);
          var theta = (lng + 180) * (Math.PI / 180);
          targetRot.x = (phi - Math.PI / 2);
          targetRot.y = -(theta - Math.PI / 2);
        }
        var m = {
          name: btn.dataset.name,
          place: btn.dataset.place,
          category: btn.dataset.cat,
          description: btn.dataset.desc,
          stats: btn.dataset.stats,
          anchor: btn.dataset.anchor
        };
        activeMarker = m;
        showSheet(m);
      });
    });

    // Visibility observer for pausing Three.js loop
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        isVisible = entry.isIntersecting;
        if (isVisible && !animId) loop();
      });
    }, { threshold: 0.05 });
    obs.observe(container);

    window.addEventListener("resize", function () {
      var w = container.clientWidth, h = container.clientHeight;
      if (!w || !h) return;
      camera.aspect = w / h; camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    });

    function loop() {
      if (!isVisible) { animId = null; return; }
      animId = requestAnimationFrame(loop);
      if (!isDragging && !activeMarker && !reduce) {
        targetRot.y += 0.0012;
      }
      currRot.x += (targetRot.x - currRot.x) * 0.08;
      currRot.y += (targetRot.y - currRot.y) * 0.08;
      globeGroup.rotation.x = currRot.x;
      globeGroup.rotation.y = currRot.y;
      if (cloudsMesh && !reduce) cloudsMesh.rotation.y += 0.0003;

      if (markerObjs.length > 0 && !reduce) {
        var s = 1.0 + Math.sin(Date.now() * 0.0035) * 0.18;
        markerObjs.forEach(function (p) { if (p.children[0]) p.children[0].scale.set(s, s, 1); });
      }
      renderer.render(scene, camera);
    }
    loop();
  }

  /* ---------- Featured Projects Slider ---------- */
  var featWrap = d.getElementById("featured-projects");
  if (featWrap) {
    var fSlides = $$(".feat-slide", featWrap), fTotal = fSlides.length;
    var fPrev = d.getElementById("feat-prev-btn"), fNext = d.getElementById("feat-next-btn");
    var fCounter = d.getElementById("feat-slide-counter"), fTrack = d.getElementById("feat-progress-track");
    var fIdx = 0;

    function updateFeat(idx) {
      fIdx = (idx + fTotal) % fTotal;
      fSlides.forEach(function (s, i) {
        var on = i === fIdx;
        s.classList.toggle("is-active", on);
        s.setAttribute("aria-hidden", String(!on));
      });
      if (fCounter) fCounter.textContent = (fIdx + 1 < 10 ? "0" : "") + (fIdx + 1) + " / " + (fTotal < 10 ? "0" : "") + fTotal;
      if (fTrack) {
        var pct = 100 / fTotal;
        fTrack.style.width = pct + "%";
        fTrack.style.left = (fIdx * pct) + "%";
      }
    }
    if (fPrev) fPrev.addEventListener("click", function () { updateFeat(fIdx - 1); });
    if (fNext) fNext.addEventListener("click", function () { updateFeat(fIdx + 1); });

    // Touch swipe for featured slider
    var touchStartX = 0;
    featWrap.addEventListener("touchstart", function (e) {
      if (e.touches && e.touches[0]) touchStartX = e.touches[0].clientX;
    }, { passive: true });
    featWrap.addEventListener("touchend", function (e) {
      if (!e.changedTouches || !e.changedTouches[0]) return;
      var diffX = e.changedTouches[0].clientX - touchStartX;
      if (Math.abs(diffX) > 45) {
        if (diffX < 0) updateFeat(fIdx + 1); else updateFeat(fIdx - 1);
      }
    }, { passive: true });
  }

  /* ---------- Initiatives Desktop Hover Preview ---------- */
  var initPreview = d.getElementById("init-hover-preview"), initImg = d.getElementById("init-preview-img");
  if (initPreview && initImg && window.innerWidth >= 1024) {
    $$(".init-row").forEach(function (row) {
      row.addEventListener("mouseenter", function () {
        var src = row.dataset.preview;
        if (src) { initImg.src = src; initPreview.classList.add("is-visible"); }
      });
      row.addEventListener("mousemove", function (e) {
        initPreview.style.left = (e.clientX + 24) + "px";
        initPreview.style.top = (e.clientY - 95) + "px";
      });
      row.addEventListener("mouseleave", function () {
        initPreview.classList.remove("is-visible");
      });
    });
  }

  /* ---------- FAQ Accordion ---------- */
  $$(".faq-trigger").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var isExp = btn.getAttribute("aria-expanded") === "true";
      var panelId = btn.getAttribute("aria-controls");
      var panel = d.getElementById(panelId);
      btn.setAttribute("aria-expanded", String(!isExp));
      if (panel) panel.hidden = isExp;
    });
  });

  /* ---------- Filter Tabs (Events & Resources) ---------- */
  $$(".filter-tabs").forEach(function (tablist) {
    var tabs = $$(".filter-tab", tablist);
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        tabs.forEach(function (t) { t.classList.remove("active"); t.setAttribute("aria-selected", "false"); });
        tab.classList.add("active"); tab.setAttribute("aria-selected", "true");
        var filter = tab.dataset.filter;

        // Events filter
        var evItems = $$("#events-list .ev-row");
        if (evItems.length > 0) {
          evItems.forEach(function (it) {
            var cat = it.dataset.category;
            it.hidden = !(filter === "all" || cat === filter);
          });
        }

        // Resources filter
        var resItems = $$("#resources-list .res-item");
        if (resItems.length > 0) {
          resItems.forEach(function (it) {
            var grp = it.dataset.filterGroup;
            it.hidden = !(filter === "all" || grp === filter);
          });
        }
      });
    });
  });

  /* ---------- Testimonials Slider ---------- */
  var tSection = d.getElementById("quotes");
  if (tSection) {
    var tSlides = $$(".t-slide", tSection), tDots = $$(".t-dot", tSection);
    var tPrev = tSection.querySelector(".t-prev"), tNext = tSection.querySelector(".t-next");
    var tTotal = tSlides.length, tIdx = 0, tTimer = null, tHover = false;

    function showTestimonial(idx) {
      tIdx = (idx + tTotal) % tTotal;
      tSlides.forEach(function (s, i) {
        var on = i === tIdx;
        s.classList.toggle("is-active", on);
        s.setAttribute("aria-hidden", String(!on));
      });
      tDots.forEach(function (dot, i) {
        var on = i === tIdx;
        dot.setAttribute("aria-current", String(on));
      });
    }

    function stopTestimonial() { clearInterval(tTimer); tTimer = null; }
    function playTestimonial() {
      stopTestimonial();
      if (!reduce && !tHover && tTotal > 1) {
        tTimer = setInterval(function () { showTestimonial(tIdx + 1); }, 7500);
      }
    }

    if (tPrev) tPrev.addEventListener("click", function () { showTestimonial(tIdx - 1); playTestimonial(); });
    if (tNext) tNext.addEventListener("click", function () { showTestimonial(tIdx + 1); playTestimonial(); });

    tDots.forEach(function (dot, i) {
      dot.addEventListener("click", function () {
        showTestimonial(i);
        playTestimonial();
      });
    });

    tSection.addEventListener("mouseenter", function () { tHover = true; stopTestimonial(); });
    tSection.addEventListener("mouseleave", function () { tHover = false; playTestimonial(); });
    tSection.addEventListener("focusin", function () { tHover = true; stopTestimonial(); });
    tSection.addEventListener("focusout", function () { tHover = false; playTestimonial(); });

    tSection.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") { showTestimonial(tIdx - 1); playTestimonial(); }
      else if (e.key === "ArrowRight") { showTestimonial(tIdx + 1); playTestimonial(); }
    });

    // Touch swipe
    var tTouchX = 0;
    tSection.addEventListener("touchstart", function (e) {
      if (e.touches && e.touches[0]) tTouchX = e.touches[0].clientX;
    }, { passive: true });
    tSection.addEventListener("touchend", function (e) {
      if (!e.changedTouches || !e.changedTouches[0]) return;
      var diffX = e.changedTouches[0].clientX - tTouchX;
      if (Math.abs(diffX) > 40) {
        if (diffX < 0) showTestimonial(tIdx + 1);
        else showTestimonial(tIdx - 1);
        playTestimonial();
      }
    }, { passive: true });

    // IntersectionObserver to pause autoplay when offscreen
    if ("IntersectionObserver" in window) {
      var tObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) playTestimonial();
          else stopTestimonial();
        });
      }, { threshold: 0.1 });
      tObserver.observe(tSection);
    }

    showTestimonial(0);
    playTestimonial();
  }

})();
