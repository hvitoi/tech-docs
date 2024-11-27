# nmap

- Network mapping tool
- It works by sending various network messages to the IP addresses in the subnet
- `nmap` commands need to run as root user or with `sudo`

```shell
# List of active IP addresses
nmap -sn "192.168.1.0/24"

# Detailed summary
nmap "192.168.1.0/24"

# Aggressive scan
nmap -A -T4 "192.168.1.11"
```
