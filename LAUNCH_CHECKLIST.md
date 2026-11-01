# Launch checklist — Earth Day Network India website
This file sits outside the site zip on purpose; it is for whoever runs the launch.
- Every DNS, email and account step below changes live infrastructure. Each one needs sign-off from the domain/account owner.
- Values in `<angle brackets>` are placeholders.

## 1. Repository and backups
- [ ] Push `/earthday_site` (already a local git repo with an initial commit) to a **private** GitHub/GitLab repo owned by the organisation, not a personal account.
- [ ] Protect `main` (require PR review). Add at least 2 org admins.
- [ ] Back up: the git remote is the primary copy. Also export a monthly zip to the org's Google Drive, and keep the client's original photos in Drive.

## 2. Netlify deploy from git
- [ ] Netlify → Add new site → Import from Git → select the repo.
- [ ] Build command: *(leave empty)*. Publish directory: `.` (already in `netlify.toml`).
- [ ] If you'd rather Netlify ran `_src/build.py` on deploy, keep the generated files committed anyway. That's the simplest route and has no build dependency.
- [ ] Check the deploy preview: forms detected (Site → Forms shows `volunteer`, `partner`, `contact`, `newsletter`), `_headers` and `_redirects` applied.
- [ ] Before going live, set `BASE_URL` in `_src/common.py` to the final domain, rebuild and commit. This updates canonicals, OG, sitemap and robots.

## 3. Custom domain and DNS (at the registrar / DNS host)
> ⚠️ **Do not touch existing MX, TXT (SPF/DKIM/DMARC) or other mail records** unless you are deliberately changing email. Only add or change the web records below. Screenshot the existing zone before editing.

| Type | Host | Value | Note |
|---|---|---|---|
| A | `@` (apex) | `75.2.60.5` | Netlify load balancer. Confirm the current IP in Netlify's domain panel |
| CNAME | `www` | `<your-site>.netlify.app` | |
| *(or)* ALIAS/ANAME | `@` | `apex-loadbalancer.netlify.com` | If the DNS host supports it |
| MX | `@` | *existing, leave as-is* | e.g. Google Workspace `smtp.google.com` priority 1 |
| TXT | `@` | *existing verification records, leave* | |

- [ ] Set `www` (or the apex) as primary in Netlify, and make the other redirect to it. It must match `BASE_URL`.
- [ ] Lower the TTL to 300 a day before the switch; raise it again afterwards.

## 4. SSL / HTTPS
- [ ] Netlify → Domain management → HTTPS → Verify DNS → Provision certificate (Let's Encrypt, **auto-renews**).
- [ ] Turn on **Force HTTPS**.
- [ ] HSTS is already sent by `_headers` (1 year, includeSubDomains). Only consider `preload` once every subdomain is HTTPS.

## 5. Email authentication (only if the org sends mail from the domain)
Examples only: copy the real values from the email provider's admin console.
- **SPF** `TXT @  "v=spf1 include:_spf.google.com ~all"`. Use one SPF record only; merge with any existing one.
- **DKIM** `TXT google._domainkey  "v=DKIM1; k=rsa; p=<key from provider>"`
- **DMARC** `TXT _dmarc  "v=DMARC1; p=none; rua=mailto:<dmarc-reports@domain>; fo=1"`. Move to `p=quarantine` after 2–4 weeks of clean reports.
- [ ] Check with mail-tester.com or MXToolbox after changing anything.

## 6. Forms
- [ ] Netlify → Forms → Notifications → add an email notification for each form to `<official inbox>`.
- [ ] Optional: enable reCAPTCHA (Forms → Spam). If enabled, update the CSP in `_headers` as its comment explains.
- [ ] Submit a test entry on every form and confirm the email arrives and the visitor lands on `/thank-you`.

## 7. Analytics (cookieless)
- [ ] Pick **Umami** (self-host or cloud) or **Plausible**. Create the site for the final domain.
- [ ] Uncomment the analytics `<script>` slot in `_src/common.py` (`page()` head; Umami line is pre-filled, replace `TODO-UMAMI-ID`, or swap for Plausible), add the host to `script-src` and `connect-src` in `_headers`, then rebuild.
- [ ] Check that events arrive: `CTA: …` clicks, `Form submit` (contact/volunteer/partner), `Phone tap`, `Email tap`, `Outbound social`, `Outbound link`, `Embed loaded`, `Programme card`.
- [ ] Update `privacy-policy.html` to say analytics is now on, and name the provider.

## 8. Search engines
- [ ] **Google Search Console:** add a Domain property (DNS TXT verification; new TXT records are fine alongside existing ones). Submit `https://<domain>/sitemap.xml`.
- [ ] **Bing Webmaster Tools:** import from GSC or verify by DNS/meta, then submit the sitemap.
- [ ] Use URL Inspection on the home page and request indexing.
- [ ] Fill `_redirects` with the real legacy URLs (if there was an old site) so old links 301 to the new pages.

## 9. Google Business Profile
- [ ] Create or claim the profile as a "Non-profit organisation".
- [ ] The **NAP (name, address, phone) must match the website footer exactly**: `Earth Day Network India`, `<address>`, `<phone>`. Supply these in `_src/common.py` (`CONTACT`) first.
- [ ] Add the website URL, hours (if any), logo and photos.

## 10. CDN and performance
- [ ] Netlify's global CDN is included; no extra CDN is needed. If you put Cloudflare in front, use DNS-only (grey cloud) or Netlify's recommended setup, to avoid double TLS and cache conflicts.
- [ ] Re-run Lighthouse / PageSpeed Insights on the live URL (target ≥ 90 on all four categories). Check headers at securityheaders.com.
- [ ] Replace the placeholder photos with the client's photos (same filenames, ≥ 1800 px wide), rebuild and recheck LCP.

## 11. Uptime monitoring
- [ ] UptimeRobot / Better Stack (free tier): an HTTPS check on `/` every 5 min, plus a keyword check for "Earth Day Network India". Send alerts to 2 people.
- [ ] Add an SSL-expiry alert as a backstop to auto-renew.

## 12. Before launch: content and legal
- [ ] Every "Placeholder" / "TODO" tag on the site is resolved (search the generated HTML for `TODO` and `Placeholder`).
- [ ] Privacy Policy and Terms reviewed by a lawyer (DPDP Act 2023). Remove the "Draft" banners.
- [ ] Image credits page updated once the client's photos replace the Wikimedia ones.
