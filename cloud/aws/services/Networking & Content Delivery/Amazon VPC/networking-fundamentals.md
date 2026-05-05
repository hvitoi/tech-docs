# VPC Networking Fundamentals

## VPC (AWS::EC2::VPC)

- A **VPC** (Virtual Private Cloud) is a private network inside AWS. Anything inside it can reach other things inside it; the outside world cannot reach in unless explicitly allowed.
- A VPC owns a **CIDR** block — a range of IPs (e.g. `10.0.0.0/16`). The `/N` is how many leading bits are fixed; the rest are yours (in this case the last 2 numbers - 8 bytes each)
- A VPC lives in **one region**. VPCs in different regions cannot talk directly without extra wiring.

## Subnet (AWS::EC2::Subnet)

- A **subnet** is a slice of the VPC's CIDR, scoped to a single **Availability Zone** (AZ).
- AZs are isolated data centers within a region. Spread subnets across AZs for redundancy.
- AWS reserves 5 IPs per subnet for its own use, so a `/28` (16 IPs) gives you ~11 usable.

Example:

```text
VPC:  10.0.0.0/16
  ├── 10.0.1.0/24   → subnet in az1
  ├── 10.0.2.0/24   → subnet in az2
  └── 10.0.3.0/24   → subnet in az3

VPC:  10.32.3.0/24   (256 IPs total)
  ├── 10.32.3.0/28   (16 IPs) → subnet in az1 (255.255.255.240) (10.32.3.0000XXXX)
  ├── 10.32.3.16/28  (16 IPs) → subnet in az2 (255.255.255.240) (10.32.3.0001XXXX)
  └── 10.32.3.32/28  (16 IPs) → subnet in az4 (255.255.255.240) (10.32.3.0010XXXX)
```

- **Public subnet**: has a route to an Internet Gateway. Reachable from / can reach the internet.
- **Private subnet**: no internet route. Used for internal workloads.

## Route table (AWS::EC2::RouteTable)

- Every subnet is associated with a **route table** that maps destination CIDRs to a target (gateway, peering, endpoint, etc.).
- Default behavior: subnets only know how to reach other things inside the VPC. Anything else needs an explicit route.
- One route table can be shared across subnets, or each subnet can have its own (more flexible, common convention in larger orgs).

## ENI (AWS::EC2::NetworkInterface)

- An **Elastic Network Interface (ENI)** is a virtual network card.
- Anything that "lives in a VPC" — EC2 instance, Lambda, RDS, PrivateLink endpoint, NAT — does so by having an ENI in one of the VPC's subnets.
- The ENI gets an IP from the subnet's CIDR.

## Connecting two VPCs

### VPC peering (AWS::EC2::VPCPeeringConnection)

- Direct point-to-point link between two VPCs.
- Simple, but doesn't scale: N VPCs needing full mesh require N² peerings.
- Cross-region peering exists but adds setup overhead.

### Transit Gateway (AWS::EC2::TransitGateway)

- Regional hub. VPCs (and on-prem links) attach to it; it routes between them.
- Scales linearly — one attachment per VPC.
- Limited to a single region; connecting TGWs across regions requires inter-region peering between them.

### CloudWAN (AWS::NetworkManager::CoreNetwork)

- Managed multi-region equivalent of Transit Gateway: one logical core network spanning regions.
- VPCs in any region attach to the same core network and can route to each other.
- Solves the cross-region problem cleanly without TGW peering.

### PrivateLink (AWS::EC2::VPCEndpoint (interface) + AWS::EC2::VPCEndpointService)

- Not a VPC-to-VPC link. Exposes **one specific service** from a producer VPC into a consumer VPC as an endpoint.
- The consumer sees an ENI in its own subnet; traffic tunnels to the producer's service.
- Properties:
  - No routing-table changes between VPCs.
  - No overlapping-CIDR issues — each side keeps its own address space.
  - Locked down — only the exposed service is reachable, not the whole producer VPC.

### When to use which

| Need                                              | Use                  |
| ------------------------------------------------- | -------------------- |
| Two VPCs, same region, full network connectivity  | Peering              |
| Many VPCs in one region, hub-and-spoke            | Transit Gateway      |
| Many VPCs across regions, hub-and-spoke           | CloudWAN             |
| Expose a single service to another VPC, locked down | PrivateLink        |

CloudWAN/TGW and PrivateLink are often combined: the hub provides the route, PrivateLink exposes the specific service.

## Attaching a VPC to a hub (TGW or CloudWAN)

A VPC attachment does two things:

1. Creates an ENI in each listed subnet — the hub uses these as on-ramps.
2. Adds routes:
   - A default route (`0.0.0.0/0` or similar) sending non-local traffic to the hub.
   - Return routes (often via **prefix lists** — named bags of CIDR ranges) so the other side knows how to reach this VPC.

In multi-account setups, the attachment is typically created from the network-management account that owns the hub, since only it can authorize new attachments.
