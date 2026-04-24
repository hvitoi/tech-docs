# SSRF (Server-Side Request Forgery)

- App takes a URL from the user and fetches it server-side (URL preview, webhook, image proxy)
- Attacker points it at internal infra the user can't reach directly
- Capital One 2019: SSRF → AWS metadata → IAM creds

## Targets

- **Cloud metadata**
  - AWS IMDSv1: `http://169.254.169.254/latest/meta-data/iam/security-credentials/<role>`
  - GCP: `http://metadata.google.internal/...` (`Metadata-Flavor: Google`)
  - Azure: `http://169.254.169.254/metadata/instance` (`Metadata: true`)
- **Internal services** — admin panels, Redis, Elasticsearch, k8s API, localhost DBs
- **Port scanning** — response time / error differences
- **Local files** — `file://`
- **Protocol smuggling** — `gopher://`, `dict://` craft raw TCP (Redis RCE classic)

## Prevention

1. **Allowlist destinations** when possible
1. **Block private IPs after DNS resolution** — `10/8`, `172.16/12`, `192.168/16`, `127/8`, `169.254/16`, `::1`, `fc00::/7`, `fe80::/10`
    - Validate the `resolved IP`, not the hostname
    - DNS rebinding: resolve once, connect to that IP (don't resolve twice)
1. **Restrict schemes** to `http(s)` only
1. **Disable redirects** or re-validate each hop
1. **Use IMDSv2** on AWS (token flow most SSRFs can't do) + hop-limit 1
1. **Network egress controls** — deny workload → metadata IP at the VPC level
1. **Drop response details** — don't echo fetched body/errors back

## Bypass tricks to test

- `127.0.0.1` vs `127.1` vs `0` vs `[::1]` vs `2130706433` (decimal)
- `127.0.0.1.nip.io` — public DNS to internal IPs
- `http://user@evil.com@127.0.0.1/` — parser confusion
- IPv6 shorthand, percent-encoding, Unicode

## Note

- CORS is browser-side; doesn't help against SSRF (your server makes the request)
