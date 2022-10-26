# tracepath

- Used to map the journey that a packet of information undertakes from its source to its destination
- Useful to locate when data loss occurs throughout the network
- Identify slow points that may adversely affect the network traffic
- The first route is usually the `modem` (`192.168.1.1`)

```sh
# Trace the route of a package
tracepath "url/ip"
tracepath www.google.com

# Print both name and ip
tracepath "ip" -b
```
