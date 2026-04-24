# Brute-Force Attacks on Auth

- Attacker tries many credentials against a login endpoint to guess one

## Shapes

- `Brute force` — many passwords, one account. Fix: account lockout
- `Credential stuffing` — one leaked password, many accounts. Fix: per-IP rate limit, breach-check, MFA
- `Password spraying` — a few common passwords across many accounts. Defeats per-account lockout

Applies to any guessable secret: login, password reset, MFA code, API token, coupon code.

## Login rate limiting

- Stack multiple dimensions
  - Per username — targeted brute force
  - Per IP — stuffing / spraying from one source
  - Per IP + username — tightest
  - Global — last-resort backstop
- Response: `429` with `Retry-After`, or exponential backoff (1s, 2s, 4s, ...)
- Same response for valid/invalid usernames (prevent enumeration)

### Pitfalls

- Blindly trusting [`X-Forwarded-For`](security-headers.md) → attacker spoofs it, limit is useless
- IPv6 — rotate through a `/64` cheaply. Rate-limit on prefix (`/64` for v6)
- Residential proxy networks — per-IP limits miss; need device fingerprinting

## Account lockout

- After N failures, disable login for a period
- Typical: `5–10` failures in `15–30 min` → lock `15 min`
- **DoS trap**: attacker knowing usernames can lock everyone out. Mitigations:
  - Lock on `IP + account`, not account alone
  - Soft lock: require CAPTCHA / MFA instead of hard block
  - Alert the user via email with "this wasn't me" link
- Useless against credential stuffing (one try per account)
- NIST SP 800-63B prefers `throttling` over hard lockouts

## Layered defense (what works)

1. Rate limit per IP and per account
1. CAPTCHA after a few failures
1. **MFA** — biggest lever; leaked passwords don't grant access
1. Breach-check passwords at signup (Have I Been Pwned k-anonymity API)
1. Anomaly detection — new-device confirmation, impossible-travel alerts
1. Strong hashing — `argon2id` / `bcrypt` / `scrypt`, that takes processing power to hash
1. Constant response time — don't leak `user exists` via timing (see [timing-attacks](../hacking/timing-attacks.md))

## Also protect

- Password reset tokens
- MFA codes (6 digits = 1M possibilities)
- Email/phone verification codes
- API keys, share links, invite codes
