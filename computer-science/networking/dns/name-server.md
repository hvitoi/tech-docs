# Name Server

A `Name Server` is a servers that resolve the DNS query (authoritative or non-authoritative)

- Also known as:
  - `public recursive name server`
  - `authoritative DNS server`
  - `recursive DNS resolver`

- A **DNS server** is any server that implements the DNS protocol
- It manages dns tables centrally. Then all hosts must look up that server.
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

## DNS Server Types

### Plain DNS

- Plain `UDP/53` connection
- Public Servers

  - **Google**
    - `8.8.8.8` & `8.8.4.4` (unfiltered)

  - **Cloudflare**
    - `1.1.1.1` & `1.0.0.1` (unfiltered)
    - `1.1.1.2` e `1.0.0.2` (blocks malware)

  - **AdGuard**
    - <https://adguard-dns.io/en/public-dns.html>
    - `94.140.14.14` & `94.140.15.15` (block ads and trackers )

### DNS over HTTPS (DoH)

- Establishes a TCP connection (instead of UDP) using TLS (encrypted) on port `443`
- Avoids DNS leak
- Improvement: Oblivious DNS over HTTPS (ODoH)

- Public Servers
  - **AdGuard**
    - <https://dns.adguard-dns.com/dns-query>

### DNS over TLS (DoT)

- Plain TCP connection on port `853`
- Public Servers
  - **AdGuard**
    - <tls://dns.adguard-dns.com>
