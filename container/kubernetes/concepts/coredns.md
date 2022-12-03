# CoreDNS

- DNS server
- Listens by default on port `53`

## Setup

### From scratch

```shell
# Download coredns binary
wget "https://github.com/coredns/coredns/releases/download/v1.4.0/coredns_1.4.0_linux_amd64.tgz"
tar -xzvf "coredns_1.4.0_linux_amd64.tgz"
```

```shell
# Run
./coredns
```

## IP to hostname mappings

- Put all entries on `/etc/hosts`
- Change configuration file `Corefile` to point to /etc/hosts

```conf
. {
    hosts /etc/hosts
}
```
