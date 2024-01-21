# DNS (Domain Name System)

- Performs (not only) name resolution (translates hostnames to IP addresses)

- **Terminology**

  - `Domain Name System` (DNS) translates hostnames
  - `Domain Registrar`: GoDaddy, Route53, etc
  - `DNS Record Types`: A, AAAA, CNAME, NS, ...
  - `Zone File`: Contains all the DNS records
  - `Name Server`: Servers that resolve the DNS query (authoritative or non-authoritative)

## DNS Record Types

- `A`: hostname to IPv4
  - webserver 192.168.1.1
- `AAAA`: hostname to IPv6
  - webserver 2804:14d:1:0:181:213:132:4
- `CNAME`: hostname to hostname (aliases)
  - food.web-server eat.web-server,hungry.web-server
- `NS`: name server. e.g., .com, .net

- Others: `CAA`, `DS`, `MX`, `NAPTR`, `PTR`, `SOA`, `TXT`, `SPF`, `SRV`

## Domain Registrar

- `Domain Registrar` is a company who can provide internet domain names
- Examples:
  - GoDaddy
  - Wix
  - Namecheap
  - AWS Route53
- They verify if the domain is available and allow you to purchase it
- Once the domain is registered, you are the `legal owner` of the domain name

## DNS Server

- A `DNS server` manages dns tables centrally. Then all hosts must look up that server.
- The host must configure the file `/etc/resolv.conf` with the dns server URL to fetch from
- Add dns entries locally to `/etc/hosts`

```conf
search mycompany.com prod.mycompany.com # append domain names to the requests
nameserver 192.168.1.100 # ip of a dns server
nameserver 8.8.8.8 # another dns server (google)
```

- `DNS Lookup Order`: 1st /etc/hosts, 2nd DNS server.
  - The order can be modified at `/etc/nsswitch.conf` (line with hosts entry)

- **Authoritative DNS Server**

  - A DNS Server where the customer (you) can modify the DNS records
  - For instance, Route53 is both an `authoritative DNS server` and a `domain registrar`

## Domain Names & Levels

- `Root`: .
- `Top Level Domain` (TLD): .com, .net, .gov
- `Second Level Domain` (SLD): amazon.com, google.com
- `Sub Domain`: api.amazon.com. It is managed by the domain registrar

![Domain Name](./images/domain-name.png)

![DNS Flow](./images/dns-flow.png)

- Resolving steps
  1. Hit the local dns server
  1. Hit the root dns server
  1. Hit the .com dns server
  1. Hit the google dns server: serve you with the IP of the apps subdomain

![Gateway](./images/dns-caching.png)
