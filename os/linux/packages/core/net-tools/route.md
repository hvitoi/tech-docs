# route

- Deprecated: use `ip route`
- Routing tables
- Traffic going to any IP not specified in the routing table goes to the `default gateway`

```sh
# list routing tables
route

# list routing table in a namespace
ip netns exec "namespace" "route"
```

- A `destination 0.0.0.0 (default)` means destination to any IP
- A `gateway 0.0.0.0` means you don't need a gateway (for connections inside the same network)

- By default, `package forwarding` is not allowed.
