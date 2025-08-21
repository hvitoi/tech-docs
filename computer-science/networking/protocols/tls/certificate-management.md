# Certificate Management

## SSL/TLS certificates

- These certificates are used to secure network communications by enabling HTTPS connections and encrypting data transmitted between users and applications.
- You can use wildcards to match all the subdomains in a domain. E.g., `*.example.com`
- The certificate is trusted by a CA

## Certificate Authority (CA)

- `DigiCert`
- `GlobalSign`
- `Sectigo` (formerly Comodo CA)
- `Entrust`
- `GoDaddy` (also a domain registrar)
- `Amazon Trust Services`

## Certificate Management Services

- `Let's Encrypt` (it's also a CA)
- `AWS Certificate Manager (ACM)`
- `Google Cloud Certificate Manager`
- `Azure App Service Certificates`
- `Cloudflare SSL for SaaS`

- `OpenSSL` (self-managed)
- `HashiCorp Vault` (self-managed)
- `Certbot` (self-managed)

### Let's Encrypt

- [Let's Encrypt](https://letsencrypt.org/) is a Linux Foundation project
- It provides HTTPS certificates for free, in an automated way
- These certificates use all the standard cryptographic security, and are short-lived (about 3 months)
- The domains are securely verified and the certificates are generated automatically. This also allows automating the renewal of these certificates.
- The idea is to automate the acquisition and renewal of these certificates so that you can have secure HTTPS, for free, forever.
