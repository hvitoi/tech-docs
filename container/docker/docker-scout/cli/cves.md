# cves

- Display CVEs (policies violatons) identified in a software artifact
- `Common Vulnerabilities and Exposures` (CVE) system provides a reference method for publicly known information-security vulnerabilities and exposures
- Each security flaw is assigned a `CVE ID number` and it's assigned by a `CVE Numbering Authority` (CNA)
- Common Vulnerability Scoring System (`CVSS`): from 0 (low) to 10 (critical)

```shell
docker scout cves local://welcome-to-docker:latest
docker scout cves archive://alpine.tar

# output format
docker scout cves \
  --format sarif \ # sarif, markdown, etc
  --output alpine.sarif.json \
  --platform linux/amd64 \
  --only-package-type npm \
  alpine

```

Example: <https://scout.docker.com/vulnerabilities/id/CVE-2023-5363>
