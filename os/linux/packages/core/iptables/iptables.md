# iptables

- Masquerade the connection, so that the request coming from a namespace is thought as if it came from the host itself

```shell
# List rules
iptables -nvL -t "nat"

# IP Masquerade
iptables \
  -t "nat" \
  -A "POSTROUTING" \
  -j "MASQUERADE" \
  -s "192.168.15.0/24"

# Port forwarding
iptables \
  -t "nat" \
  -A "PREROUTING" \
  -j "DNAT" \
  --dport "8080" \ # req coming to port ...
  --todestination "80" # goes to port ...

# Port forwarding in docker
iptables \
  -t "nat" \
  -A "DOCKER" \
  -j "DNAT" \
  --dport "8080" \
  --todestination "172.17.0.3" \ # goes to port 80 in the container
```
