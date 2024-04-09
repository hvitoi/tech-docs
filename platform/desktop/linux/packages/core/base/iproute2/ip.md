# IP command

- All configuration made with this command are lost after reboot
- Use a network manager for persistent configuration
- You the parameter `-c` to add color

## link

- `link/ether` is the MAC address of the interface

### show

```shell
ip link show # all interface (ip link)
ip link show "wlp3s0" # specific interface
```

### set

```shell
ip link set "wlp3s0" up # activate
ip link set "wlp3s0" down # deactivate
ip link set "wlp3s0" address "00:11:22:33:44:55" # change MAC address (must be down first)
```

### add

```shell
ip link add "wlp3s0" type "bridge"
ip link add "veth-red" type "veth" peer name "veth-blue" # veth cable
```

### del

```shell
ip link del "wlp3s0"
```

### Create a virtual Ethernet Pair (veth cable)

```shell
# Create virtual ethernet pair (a "cable" to connect 2 namespaces)
ip link add "veth-red" type "veth" peer name "veth-blue"

# Attach each veth to its corresponding namespaces
ip link set "veth-red" netns "red"
ip link set "veth-blue" netns "blue"

# Deleting one link, the other is deleted automatically (veth-blue)
ip link del "veth-red" -n "red"
ip link del "veth-blue" -n "blue" # not necessary
```

### Create bridge interface

```shell
# Add new interface of type bridge
ip link add "v-net-0" type "bridge"
ip link set "v-net-0" up
ip link add "veth-red" type "veth" peer name "veth-red-br" # connects to the bridge
```

## address

```shell
# List IP addresses assigned for each interface
ip address # addr or a

# Assign an IP to an interface (temporary)
ip address add "192.168.1.10/24" dev "interface-id"
ip address add "192.168.1.10/24" dev "veth-red" -n "red" # interface in a namespace
```

## route

- Routing tables are used to force traffic going to another network to pass through a gateway
- The gateway joins every network. A gateway is assigned an IP for each network it is part of.

```shell
# show routing tables
ip route

# add entries into the routing table
ip route add "192.168.2.0/24" via "192.168.1.1"
```

## netns

```shell
# list network namespaces
ip netns

# create namespace
ip netns add "red"
ip netns add "blue"

# execute a command in the namespace
ip netns exec "blue" "ip link"
ip link -n "blue" # same effect
```

## Concepts

- `IP`: Identifies each computer using Internet Protocol
- `Subnetmask`: Masks the IP. Divide the IP into network address and host address
- `Gateway`: Which route to take to send the traffic out or to receive traffic
- `Static IP`: IP does not change for a machine
- `DHCP`: Takes the address from a pool of IPs and assign to a machine upon connection
- `Interface`: a NIC (Network Interface Controller) card. Ethernet, Wi-Fi, etc. Always have a MAC address that never changes (E.g, 3A-34-52-C4-69-B8)

## Interface configuration files

- `/etc/nsswitch.conf`
  - Tells the system where it should resolve some functionalities of the system (E.g, resolve the hostname to ip address -> hosts: files mdns4_minimal [NOTFOUND=return] dns)
- `/etc/hosts`: resolve hostname to ip address
- `/etc/hostname`: current hostname
- `/etc/network/interfaces`: Interfaces
- `/etc/resolv.conf`: IP to the DNS server! Resolve hostname-ip, ip-hostname, hostname-hostname
- `/etc/sysconfig/network-scripts/ifcfg-nic`: Static IP configuration

## Protocols or clients to access the system

- Windows: Remote Desktop RDP (for Windows)
- VMware ESC: vSphere client (for Windows)
- Linux: Putty (for Windows), SecureCRT, SSH from Linux to Linux

## NIC (Network Interface Card)

- `NICs` in `ip addr`

  - `lo`: Loopback device. Interface for the computer to communicate with itself
  - `virb0`: Virtual bridge is used for NAT (Network Address Translation )
  - `enp`: Cabled network
  - `wlp`: Wireless network

- enp2s0: Wired connection
- wlp3s0: Wireless connection
