# dig

- Similar to dnslookup but more verbose
- Dig is newer and shows more info than nslookup

```sh
dig "example.com" # A records by default
dig "example.com" A
dig "example.com" NS
dig "example.com" MX # mail
```

- `Header`
- `Opt Pseudosection`: EDNS (extension system for dns)
- `Question Section`: the query
- `Answer Section`: Domain - TTL - IN (internet) - Record Type - Value
- `Statistics`

```sh
dig "example.com" +short # show only the value of the A record
dig "example.com" +noall +answer # only the answer
dig "example.com" +trace # list of servers the query went through
```

```sh
# Reverse DNS lookup
dig -x "22.22.22.22"
```
