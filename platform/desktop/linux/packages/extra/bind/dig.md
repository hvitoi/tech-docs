# dig

- Similar to dnslookup but more verbose
- Dig is newer and shows more info than nslookup

```shell
dig "example.com" # A records by default
dig "example.com" A
dig "example.com" NS
dig "example.com" MX # mail

# CNAME
dig www.example.com +nostats +nocomments +nocmd

# A
dig example.com +noall +answer -t A

# AAAA
dig example.com +noall +answer -t AAAA
```

- `Header`
- `Opt Pseudosection`: EDNS (extension system for dns)
- `Question Section`: the query
- `Answer Section`: Domain - TTL - IN (internet) - Record Type - Value
- `Statistics`

```shell
dig "example.com" +short # show only the value of the A record
dig "example.com" +noall +answer # only the answer
dig "example.com" +trace # list of servers the query went through
```

```shell
# Reverse DNS lookup
dig -x "22.22.22.22"
```
