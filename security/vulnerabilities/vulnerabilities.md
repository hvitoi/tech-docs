# Vulnerabilities

## Injection & XSS

- [SQL Injection (SQLi)](sql-injection.md) — concatenated SQL → data exfil, auth bypass. Fix: parameterized queries
- [XSS (Cross-Site Scripting)](xss.md) — attacker JS runs in victim's browser. Fix: context-aware output encoding + CSP

## Request forgery

- [CSRF (Cross-Site Request Forgery)](csrf.md) — victim's browser fires authenticated request from attacker's page. Fix: `SameSite` cookies + CSRF tokens
- [SSRF (Server-Side Request Forgery)](ssrf.md) — server fetches attacker-chosen URL → cloud metadata, internal services. Fix: allowlist + block private IPs after resolution

## Browser hardening

- [Security Headers](security-headers.md) — CSP, X-Frame-Options, HSTS, CORS, X-Content-Type-Options, and the `X-Forwarded-For` pitfalls

## Authentication

- [Brute-Force Attacks](brute-force.md) — login rate limiting, account lockout, credential stuffing, MFA

## Other kinds

- **Credentials Leakage**
  - Secret keys exposed (committed to git, logged, left in client bundles)
  - Revoke immediately; rotate; audit access logs
  - Principle of least privilege limits blast radius
- **Broken Authentication** — weak passwords, session fixation, missing MFA, insecure password reset flows
- **Broken Access Control** — IDOR (change `/users/123` → `/users/124`), missing authorization checks on APIs
- **Insecure Deserialization** — untrusted data into `pickle` / Java `readObject` / PHP `unserialize` → RCE

## Penetration testing

- Test and exploit vulnerabilities (with authorization)
- **Burp Suite** — intercepting MITM proxy for request tampering
- **OWASP ZAP** — open-source alternative
- Roles
  - `White hat`: authorized
  - `Grey hat`: unauthorized but not malicious
  - `Black hat`: malicious (sell data, ransomware, etc.)

## CIA Triad

- `Confidentiality` — data is readable only by authorized parties (authN/authZ, encryption)
- `Integrity` — data is correct and untampered (signatures, hashes, transactions)
- `Availability` — data / service is reachable when needed (redundancy, DoS protection, rate limiting)
