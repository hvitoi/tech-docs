# Classless Inter-Domain Routing (CIDR)

- CIDR is an IP address allocation method that improves data routing efficiency on the internet.
- An IP address is composed of two parts
  - The `network address` is a series of numerical digits pointing to the network's unique identifier
  - The `host address` is a series of numbers indicating the host or individual device identifier on the network
- An IPv4 address consists of `32 bits`

## Classful Notation

### Class A

- 8 network prefix bits
- `255.0.0.0/8`: `11111111.00000000.00000000.00000000`
- Support `16,777,214` hosts
- Example: 44.0.0.1

### Class B

- 16 network prefix bits
- Support 65,534 hosts
- `255.255.0.0/16`: `11111111.11111111.00000000.00000000`
- Example: 128.16.0.2

### Class C

- 24 network prefix bits
- `255.255.255.0/24`: `11111111.11111111.11111111.00000000`
- Support 254 hosts
- Example: 192.168.1.100

## CIDR Notation

- The classful arrangement was inefficient when allocating IP addresses and led to a waste of IP address spaces
  - For example, an organization with 300 devices couldn't have used a Class C IP address, which only permitted 254 devices. So, the organization would've been forced to apply for a Class B IP address, which provided 65,534 unique host addresses
- CIDR addresses use `variable length subnet masking` (VLSM) to alter the ratio between the network and host address bits in an IP address. Therefore it is not limited to the classes A, B, C (classful), in fact the proportion is adjusted as needed
- First bits defined by `/nn` are dedicated to the `network portion of the address` while the remainin bits are the `host portion of the address`

- `255.255.240.0/12`: `11111111.11110000.00000000.00000000`
  - 12 network prefix bits
- `255.255.255.240/28`: `11111111.11111111.11111111.11110000`
  - 28 network prefix bits
