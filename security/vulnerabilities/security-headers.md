# Security Headers

- HTTP response headers that tell the browser to enforce security policies
- Defense in depth — they reduce blast radius when something else fails
- Audit: <https://securityheaders.com> or `curl -I`

## CSP (Content Security Policy)

- `Content-Security-Policy: ...` — allowlist sources for scripts/styles/images/frames/connections
- Primary defense against [XSS](xss.md): injected `<script>` won't run unless source is allowlisted

```http
Content-Security-Policy:
  default-src 'self';
  script-src 'self' 'nonce-r4nd0m';
  frame-ancestors 'none';
  object-src 'none'
```

- `'self'` — same origin
- `'nonce-<random>'` — allow specific inline scripts (per-response random)
- `'unsafe-inline'` / `'unsafe-eval'` — avoid; defeats most of CSP
- Roll out with `Content-Security-Policy-Report-Only` first

## X-Frame-Options

- `X-Frame-Options: DENY` or `SAMEORIGIN`
- Prevents `clickjacking` — your site embedded in `evil.com`'s invisible iframe
- Superseded by CSP `frame-ancestors`; set both for coverage

## HSTS (HTTP Strict Transport Security)

- `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`
- Browser refuses plain-HTTP to this host for `max-age` seconds
- Defeats SSL-stripping MITM
- `preload` → <https://hstspreload.org> hard-codes into browsers. Hard to reverse

## CORS

- `Access-Control-Allow-Origin/Methods/Headers/Credentials`
- Relaxes Same-Origin Policy so a frontend on another origin can call your API
- Not a security boundary for the API — non-browser clients ignore it
- Pitfalls
  - `Allow-Origin: *` + `Allow-Credentials: true` → browser rejects. Echo a validated `Origin` instead
  - Reflecting arbitrary `Origin` → CORS becomes the vulnerability

## X-Content-Type-Options

- `X-Content-Type-Options: nosniff`
- Disables MIME sniffing — `.txt` won't be reinterpreted as HTML/JS
- Cheap; set everywhere

## Other worth setting

- `Referrer-Policy: strict-origin-when-cross-origin` — limits `Referer` leaks
- `Permissions-Policy: geolocation=(), microphone=(), camera=()` — disable powerful APIs
- `Cross-Origin-Opener-Policy` + `Cross-Origin-Embedder-Policy` — cross-origin isolation (mitigates Spectre)
- `Cache-Control: no-store` on authenticated pages

## X-Forwarded-For (not a security header — beware)

- Request header from proxies/CDNs with the original client IP
- Syntax: `X-Forwarded-For: <client>, <proxy1>, <proxy2>`
- Any client can send it. If your app trusts it blindly, attackers spoof their IP → bypass logging, rate limits, IP allowlists
- Trust only values added by your known proxies — count hops from the right
- Configure trusted proxies explicitly (Django `SECURE_PROXY_SSL_HEADER`, Express `trust proxy`, Rails `trusted_proxies`)
- Broken here = [login rate limiting](brute-force.md) is trivially bypassable
