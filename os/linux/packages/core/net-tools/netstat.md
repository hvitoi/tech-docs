# netstat

- This program is mostly obsolete. Replacements:
  - `netstat` -> `ss`
  - `netstat -r` -> `ip route`
  - `netstat -i` -> `ip -s link`
  - `netstat -g` -> `ip maddr`

```sh
# Print network connections
netstat
netstat -rnv # Show the gateways

# Print all ports currently open and listening
netstat -tunlp
  # listening sockets (-l)
  # port number (-n)
  # TCP ports (-t)
  # UDP ports (-u)
  # display PID/Program name for sockets
```
