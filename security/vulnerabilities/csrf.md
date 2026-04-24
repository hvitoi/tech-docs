# CSRF (Cross-Site Request Forgery)

- Attacker tricks the victim's browser into sending an authenticated request to his site
- Browser auto-attaches cookies → server sees a legit session → state-changing action fires
- Works because cookie auth is `ambient` — cookies travel with every request to that origin

## Example

- Victim logged into `bank.com` visits `evil.com`
- `evil.com` auto-submits a hidden form to `bank.com/transfer`
- Bank sees the victim's cookie; transfer goes through

## XSS vs CSRF

- `XSS` — runs attacker code in your origin (full control, can read responses)
- `CSRF` — only `fires` a request; can't read the response (Same-Origin Policy). Useful only against state-changing endpoints

## Prevention

1. **`SameSite` cookies** — modern default
    - `Lax` (browser default): not sent on cross-site POST, sent on top-level GET
    - `Strict`: not sent on any cross-site request (safer, worse UX)
    - `None; Secure`: explicit opt-in for cross-site
1. **CSRF tokens** (synchronizer) — random token in session + required in every state-changing request; attacker can't read it (SOP), can't forge it
1. **Double-submit cookie** — token in cookie + header; server checks they match. No session storage needed
1. **Origin / Referer check** — reject cross-origin requests. Cheap layered defense
1. **Re-auth for high-risk actions** (password change, transfers)
1. **Use `Authorization: Bearer` instead of cookies** — browsers don't auto-attach it (but tokens stored in cookies bring CSRF back)

## Not a fix

- CAPTCHA — stops bots, not CSRF (victim is human)
- POST-only — hidden form auto-submits fine
- HTTPS — encrypted CSRF is still CSRF
- User-Agent checks — victim's real browser sends the request

## Related

- `CSWSH` — CSRF for WebSocket handshakes. Fix: check `Origin`
- `Login CSRF` — force victim to log in as attacker's account
