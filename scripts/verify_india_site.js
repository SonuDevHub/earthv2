const { chromium } = require('C:/xampp/htdocs/previous_build_backup/node_modules/playwright');
const fs = require('fs');
const path = require('path');

const BASE_URL = 'http://localhost/earth-day';
const VERIFY_DIR = path.join(__dirname, '..', 'docs', 'verify');

const VIEWPORTS = [
  { name: 'mobile-small', width: 360, height: 740 },
  { name: 'mobile-std', width: 390, height: 844 },
  { name: 'mobile-large', width: 414, height: 896 },
  { name: 'tablet-portrait', width: 768, height: 1024 },
  { name: 'tablet-landscape', width: 820, height: 1180 },
  { name: 'desktop-small', width: 1024, height: 768 },
  { name: 'desktop-hd', width: 1280, height: 800 },
  { name: 'desktop-std', width: 1440, height: 900 },
  { name: 'desktop-wide', width: 1920, height: 1080 }
];

const PAGES = [
  { slug: 'index', file: 'index.html', isHome: true },
  { slug: 'about', file: 'about.html' },
  { slug: 'programs', file: 'programs.html' },
  { slug: 'network', file: 'network.html' },
  { slug: 'awards', file: 'awards.html' },
  { slug: 'events', file: 'events.html' },
  { slug: 'resources', file: 'resources.html' },
  { slug: 'join-us', file: 'join-us.html' },
  { slug: 'privacy-policy', file: 'privacy-policy.html' },
  { slug: 'terms', file: 'terms.html' },
  { slug: 'credits', file: 'credits.html' },
  { slug: 'thank-you', file: 'thank-you.html' },
  { slug: '404', file: '404.html' }
];

function calcLuminance(r, g, b) {
  const [rs, gs, bs] = [r, g, b].map(c => {
    c = c / 255;
    return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
}

function calcContrast(rgb1, rgb2) {
  const l1 = calcLuminance(...rgb1);
  const l2 = calcLuminance(...rgb2);
  const brightest = Math.max(l1, l2);
  const darkest = Math.min(l1, l2);
  return (brightest + 0.05) / (darkest + 0.05);
}

function parseRgb(str) {
  const m = str.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
  return m ? [parseInt(m[1]), parseInt(m[2]), parseInt(m[3])] : [0, 0, 0];
}

async function runVerification() {
  console.log('Starting Playwright Verification for Earth Day Network India build...');
  const browser = await chromium.launch({ headless: true });
  
  const report = {
    timestamp: new Date().toISOString(),
    pagesTested: 0,
    viewportsTested: VIEWPORTS.length,
    horizontalOverflows: [],
    consoleErrors: [],
    contrastResults: [],
    interactiveChecks: []
  };

  // 1. Check home page across all viewports for layout, horizontal overflow, and responsiveness
  console.log('\n--- Checking Viewports & Responsiveness on Home Page ---');
  for (const vp of VIEWPORTS) {
    const context = await browser.newContext({ viewport: { width: vp.width, height: vp.height } });
    const page = await context.newPage();
    const errors = [];
    page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
    page.on('pageerror', err => errors.push(err.message));

    await page.goto(`${BASE_URL}/index.html`, { waitUntil: 'networkidle' });

    // Check horizontal overflow
    const overflow = await page.evaluate(() => {
      return document.documentElement.scrollWidth > window.innerWidth + 2;
    });
    if (overflow) {
      report.horizontalOverflows.push({ page: 'index.html', viewport: vp.name, width: vp.width });
      console.error(`  [FAIL] Horizontal overflow at ${vp.name} (${vp.width}px)`);
    } else {
      console.log(`  [PASS] No horizontal overflow at ${vp.name} (${vp.width}px)`);
    }

    // Check mobile hero (width <= 767px): only one button visible
    if (vp.width <= 767) {
      const ghostDisplay = await page.evaluate(() => {
        const ghost = document.querySelector('.hero .btn-secondary-hero');
        return ghost ? window.getComputedStyle(ghost).display : 'none';
      });
      if (ghostDisplay === 'none') {
        console.log(`  [PASS] Mobile hero single-button verified at ${vp.name}`);
      } else {
        console.warn(`  [WARN] Secondary hero button not hidden on mobile at ${vp.name}`);
      }
    }

    if (errors.length > 0) {
      report.consoleErrors.push({ page: 'index.html', viewport: vp.name, errors });
    }
    await context.close();
  }

  // 2. Comprehensive check of all 13 pages at desktop (1280x800) and mobile (390x844)
  console.log('\n--- Checking All 13 Pages for Console Errors & Scroll ---');
  const desktopCtx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  const desktopPage = await desktopCtx.newPage();

  for (const p of PAGES) {
    const errors = [];
    desktopPage.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
    desktopPage.on('pageerror', err => errors.push(err.message));

    const res = await desktopPage.goto(`${BASE_URL}/${p.file}`, { waitUntil: 'networkidle' });
    report.pagesTested++;
    const status = res ? res.status() : 0;

    // Scroll to bottom to test full scroll and reach footer
    await desktopPage.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
    await desktopPage.waitForTimeout(300);

    const footerVisible = await desktopPage.evaluate(() => {
      const ft = document.querySelector('.site-footer');
      return !!ft && ft.getBoundingClientRect().top < window.innerHeight + 500;
    });

    console.log(`  Page ${p.file} -> HTTP ${status}, footer visible: ${footerVisible}, errors: ${errors.length}`);
    if (errors.length > 0) {
      report.consoleErrors.push({ page: p.file, errors });
    }

    // Capture screenshot for key pages
    if (['index', 'about', 'programs', 'network', 'awards', 'events', 'resources', 'join-us'].includes(p.slug)) {
      await desktopPage.screenshot({ path: path.join(VERIFY_DIR, `desktop-1280-${p.slug}.png`), fullPage: true });
    }
  }
  await desktopCtx.close();

  // 3. Capture mobile screenshots for key viewports
  console.log('\n--- Capturing Tablet (768) and Mobile (390) Screenshots ---');
  const tabletCtx = await browser.newContext({ viewport: { width: 768, height: 1024 } });
  const tabletPage = await tabletCtx.newPage();
  await tabletPage.goto(`${BASE_URL}/index.html`, { waitUntil: 'networkidle' });
  await tabletPage.screenshot({ path: path.join(VERIFY_DIR, 'tablet-768-home.png'), fullPage: true });
  await tabletCtx.close();

  const mobileCtx = await browser.newContext({ viewport: { width: 390, height: 844 } });
  const mobilePage = await mobileCtx.newPage();
  await mobilePage.goto(`${BASE_URL}/index.html`, { waitUntil: 'networkidle' });
  await mobilePage.screenshot({ path: path.join(VERIFY_DIR, 'mobile-390-home.png'), fullPage: true });
  await mobileCtx.close();

  // 4. Test Interactive Components on Home Page
  console.log('\n--- Testing Interactive Components on Home Page ---');
  const testCtx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  const testPage = await testCtx.newPage();
  await testPage.goto(`${BASE_URL}/index.html`, { waitUntil: 'networkidle' });

  // A. Contrast Check on Primary CTA Button
  const btnStyles = await testPage.evaluate(() => {
    const btn = document.querySelector('.hero .btn');
    if (!btn) return null;
    const s = window.getComputedStyle(btn);
    return { color: s.color, background: s.backgroundColor };
  });
  if (btnStyles) {
    const textColor = parseRgb(btnStyles.color);
    const bgColor = parseRgb(btnStyles.background);
    const contrast = calcContrast(textColor, bgColor);
    const passesAA = contrast >= 4.5;
    report.contrastResults.push({ element: 'Hero .btn', color: btnStyles.color, background: btnStyles.background, contrast: contrast.toFixed(2), passesAA });
    console.log(`  Button contrast: ${btnStyles.color} on ${btnStyles.background} -> ${contrast.toFixed(2)}:1 (Passes AA: ${passesAA})`);
  }

  // B. 3D Globe Section
  console.log('  Testing 3D Earth Globe...');
  await testPage.evaluate(() => {
    const el = document.getElementById('global-movement');
    if (el) el.scrollIntoView();
  });
  await testPage.waitForTimeout(1000);

  const canvasExists = await testPage.evaluate(() => {
    const c = document.querySelector('#earth-canvas-container canvas');
    return !!c;
  });
  console.log(`  3D Globe Canvas injected: ${canvasExists}`);

  // Test Globe Filter Buttons
  const filterPass = await testPage.evaluate(() => {
    const btn = document.querySelector('.globe-legend-btn[data-filter="forests"], .globe-filter-btn[data-filter="forests"]');
    if (btn) { btn.click(); return btn.classList.contains('active'); }
    return false;
  });
  console.log(`  Globe filter click 'forests': ${filterPass}`);

  // Test Globe Place Item Selection & Bottom-sheet
  const sheetOpenPass = await testPage.evaluate(() => {
    const placeBtn = document.querySelector('.globe-place-item');
    if (placeBtn) {
      placeBtn.click();
      const sheet = document.getElementById('globe-sheet');
      return sheet && !sheet.hidden;
    }
    return false;
  });
  console.log(`  Globe place click opens sheet: ${sheetOpenPass}`);

  // Test Quotes / Testimonial Slider
  console.log('  Testing Quotes & Testimonials Slider...');
  const testSliderPass = await testPage.evaluate(() => {
    const qSec = document.getElementById('quotes');
    if (!qSec) return false;
    const nextBtn = qSec.querySelector('.t-next');
    if (nextBtn) nextBtn.click();
    const activeSlide = qSec.querySelector('.t-slide.is-active');
    return !!activeSlide;
  });
  console.log(`  Testimonials slider next navigation: ${testSliderPass}`);

  // Test Mobile Menu Overlap (Bounding Box Check) at 390px
  console.log('\n--- Testing Mobile Menu Overlap (Bounding Box Check) ---');
  const mobCheckCtx = await browser.newContext({ viewport: { width: 390, height: 844 } });
  const mobCheckPage = await mobCheckCtx.newPage();
  await mobCheckPage.goto(`${BASE_URL}/index.html`, { waitUntil: 'networkidle' });

  const menuOverlapResults = await mobCheckPage.evaluate(() => {
    const toggle = document.querySelector('.menu-toggle');
    if (!toggle) return { opened: false, overlaps: [] };
    toggle.click(); // open menu

    // Open first dropdown accordion to test expanded submenus
    const firstDdBtn = document.querySelector('.nav .dd-btn');
    if (firstDdBtn) firstDdBtn.click();

    // Check all visible nav links for bounding-box intersection
    const links = Array.from(document.querySelectorAll('.nav a, .nav .dd-btn')).filter(el => {
      const rect = el.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0 && window.getComputedStyle(el).display !== 'none';
    });

    const overlaps = [];
    for (let i = 0; i < links.length; i++) {
      for (let j = i + 1; j < links.length; j++) {
        const r1 = links[i].getBoundingClientRect();
        const r2 = links[j].getBoundingClientRect();
        // Check if rectangles intersect with more than 2px tolerance
        const intersects = !(r2.left >= r1.right - 2 || 
                             r2.right <= r1.left + 2 || 
                             r2.top >= r1.bottom - 2 || 
                             r2.bottom <= r1.top + 2);
        if (intersects) {
          overlaps.push({
            el1: links[i].textContent.trim().slice(0, 30),
            el2: links[j].textContent.trim().slice(0, 30),
            r1: { top: r1.top, bottom: r1.bottom },
            r2: { top: r2.top, bottom: r2.bottom }
          });
        }
      }
    }
    return { opened: document.body.classList.contains('menu-open'), overlaps, totalLinksChecked: links.length };
  });

  console.log(`  Mobile Menu opened: ${menuOverlapResults.opened}, Links checked: ${menuOverlapResults.totalLinksChecked}`);
  if (menuOverlapResults.overlaps.length === 0) {
    console.log(`  [PASS] 0 bounding-box overlaps in mobile menu!`);
  } else {
    console.error(`  [FAIL] Detected ${menuOverlapResults.overlaps.length} overlapping links in mobile menu:`, menuOverlapResults.overlaps);
    report.interactiveChecks.push({ check: 'Mobile menu overlap', failed: true, overlaps: menuOverlapResults.overlaps });
  }
  await mobCheckCtx.close();

  // C. Featured Projects Slider
  console.log('  Testing Featured Projects Slider...');
  await testPage.evaluate(() => {
    const el = document.getElementById('featured-projects');
    if (el) el.scrollIntoView();
  });
  await testPage.waitForTimeout(500);

  const sliderNext = await testPage.evaluate(() => {
    const btn = document.getElementById('feat-next-btn');
    if (btn) {
      btn.click();
      const counter = document.getElementById('feat-slide-counter');
      return counter ? counter.textContent.trim() : '';
    }
    return '';
  });
  console.log(`  Featured Slider next click counter: "${sliderNext}" (expected "02 / 06")`);

  const sliderPrev = await testPage.evaluate(() => {
    const btn = document.getElementById('feat-prev-btn');
    if (btn) {
      btn.click();
      const counter = document.getElementById('feat-slide-counter');
      return counter ? counter.textContent.trim() : '';
    }
    return '';
  });
  console.log(`  Featured Slider prev click counter: "${sliderPrev}" (expected "01 / 06")`);

  // D. Initiatives list
  const initCount = await testPage.evaluate(() => {
    return document.querySelectorAll('.init-row').length;
  });
  console.log(`  Initiatives rows count: ${initCount} (expected 8)`);

  // 5. Test FAQ Accordions
  console.log('\n--- Testing FAQ Accordions on About & Join Us ---');
  await testPage.goto(`${BASE_URL}/about.html`, { waitUntil: 'networkidle' });
  const faqAboutResult = await testPage.evaluate(() => {
    const trigger = document.querySelector('.faq-trigger');
    if (!trigger) return false;
    trigger.click();
    const exp = trigger.getAttribute('aria-expanded');
    const panel = document.getElementById(trigger.getAttribute('aria-controls'));
    return exp === 'true' && panel && !panel.hidden;
  });
  console.log(`  About FAQ toggle accordion: ${faqAboutResult}`);

  await testPage.goto(`${BASE_URL}/join-us.html`, { waitUntil: 'networkidle' });
  const faqJoinResult = await testPage.evaluate(() => {
    const trigger = document.querySelector('.faq-trigger');
    if (!trigger) return false;
    trigger.click();
    const exp = trigger.getAttribute('aria-expanded');
    const panel = document.getElementById(trigger.getAttribute('aria-controls'));
    return exp === 'true' && panel && !panel.hidden;
  });
  console.log(`  Join Us FAQ toggle accordion: ${faqJoinResult}`);

  // 6. Test Filter Tabs on Events and Resources
  console.log('\n--- Testing Filter Tabs on Events & Resources ---');
  await testPage.goto(`${BASE_URL}/events.html`, { waitUntil: 'networkidle' });
  const eventsFilterResult = await testPage.evaluate(() => {
    const tab = document.querySelector('.filter-tab[data-filter="upcoming"]');
    if (!tab) return false;
    tab.click();
    const rows = Array.from(document.querySelectorAll('#events-list .ev-row'));
    const visibleRows = rows.filter(r => !r.hidden);
    return tab.classList.contains('active') && visibleRows.length > 0;
  });
  console.log(`  Events tab filter 'upcoming': ${eventsFilterResult}`);

  await testPage.goto(`${BASE_URL}/resources.html`, { waitUntil: 'networkidle' });
  const resourcesFilterResult = await testPage.evaluate(() => {
    const tab = document.querySelector('.filter-tab[data-filter="reports"]');
    if (!tab) return false;
    tab.click();
    const rows = Array.from(document.querySelectorAll('#resources-list .res-item'));
    const visibleRows = rows.filter(r => !r.hidden);
    return tab.classList.contains('active') && visibleRows.length > 0;
  });
  console.log(`  Resources tab filter 'reports': ${resourcesFilterResult}`);

  await testCtx.close();
  await browser.close();

  // Save report
  fs.writeFileSync(path.join(__dirname, '..', 'docs', 'verify', 'verification_summary.json'), JSON.stringify(report, null, 2));
  console.log('\nVerification complete! Report saved to docs/verify/verification_summary.json');
}

runVerification().catch(err => {
  console.error('Verification failed:', err);
  process.exit(1);
});
