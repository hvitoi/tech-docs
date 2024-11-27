# DNS (Domain Name System)

- DNS servers are crucial for the functioning of the internet as they facilitate the resolution of `domain names` to `IP addresses`.
- A UDP package is sent over `UDP` (unencrypted) to the `DNS Resolver` on port `53`
- `ICANN`: nonprofit organization that oversees the use of internet domains
  - WHOIS info: <https://lookup.icann.org/> (includes registrar and nameserver config)

## DNS Record Types

- The DNS records are sotred at a `Zone File` and it is hosted at the name server

### A (Address record)

- `hostname` -> `IPv4`
- webserver 192.168.1.1

### AAAA (IPv6 address record)

- `hostname` -> `IPv6`
- webserver 2804:14d:1:0:181:213:132:4

### CNAME (Canonical name record)

- `hostname` -> `hostname`
- E.g, food.web-server eat.web-server,hungry.web-server

### MX (Mail server record)

- Specify mail servers for the domain

### NS (Name server record)

- Defines `which name servers are authoritative` for the domain
- Delegates a DNS zone to use the given authoritative name servers
- The NS records are pointers to the `authoritative name servers` for a particular domain or subdomain.
- When using a Registrar that has DNS server support, this config is usually automatically configured
- You can also use a registrar and configure a different NS (custom name server)

### TXT

- Store arbitrary text (e.g., for email verification or security)

### Others

- `CAA`
- `DS`
- `MX`
- `NAPTR`
- `PTR`
- `SOA`
- `TXT`
- `SPF`
- `SRV`

## DNSSEC (DNS Security Extensions)

- Protect your domain from threats
  - DNS cache poisoning attacks
  - DNS spoofing
