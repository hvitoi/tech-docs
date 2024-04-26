# Content Delivery Network (CDN)

- Distribute `cached static content`
- Example: movies, images, binary blobs, css, js, html, etc
- Content is delivered from locations/servers very close to where the clients are

- It's NOT applicable for dynamic content (e.g., user information), this info has to be retrieved from the database directly

## CDN Servers

- Often known as `edge servers`
- They are located at different `Points of Presence` (PoP) at strategic locations

## Pull strategy

- The CDN will actively pull the asset from the original server when necessary
- It's configured by setting a `Time To Live` (TTL) property for each asset
- On the end of the TTL, the CDN checks with the server if the content has changed
  - If Not, renew the TTL with the existing asset
  - If Yes, download the new version and renew the TTL

- **Pros**
  - Requires lower maintenance! (everything is taken care by the CDN provider)
- **Cons**
  - The first users to require an asset (miss) will have a longer latency
  - The CDN may try to pull when the server is under maintenance

## Push strategy

- The server actively push a new asset version to the CDN

- **Pros**
  - Reduces the traffic to the server
  - Less traffic to the server

## Implementations

- **Cloudflare**
- **Fastly**
- **Akamai**
- **AWS CloudFront**
- **GCP CDN**
- **Azure Content Delivery Network**
