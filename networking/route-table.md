# Route Table

- A route table is a data structure used by network devices (such as routers, firewalls, and computers) to determine `how to forward packets to their destination`
- It contains a set of rules (routes) that specify how packets should be directed based on their destination IP address.

## Structure

| Destination | Netmask       | Gateway     | Interface | Metric |
| -           | -             | -           | -         | -      |
|0.0.0.0      | 0.0.0.0       | 192.168.1.1 | eth0      | 0      |
|192.168.1.0  | 255.255.255.0 | 0.0.0.0     | eth0      | 0      |

```shell
ip route show

# default via 192.168.1.1 dev eth0
# 192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```

## 0.0.0.0/0

- `0.0.0.0/0` represents a network route that matches any IP address. It's a shorthand notation for "any destination"
- In routing terms it is called the `default route`, meaning it catches all traffic that doesn't match a more specific route in the routing table
