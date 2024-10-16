# AWS::EC2::NetworkInterface

- **Elastic Network Interface** (ENI)
  - Represents a `Network Card`
  - It can be attached to an EC2 instance
  - ENI can be created independently and attached to EC2 instances on the fly

- IP Types
  - `Private IP`: used within the private network
  - `Public IP`: unique across all web
  - `Elastic IP`: a static public ip. You can only have `5` elastic ip in your aws account

```yaml
Type: AWS::EC2::NetworkInterface
Properties:
  Description: String
  GroupSet:
    - String
  InterfaceType: String
  Ipv6AddressCount: Integer
  Ipv6Addresses:
    - InstanceIpv6Address
  PrivateIpAddress: String
  PrivateIpAddresses:
    - PrivateIpAddressSpecification
  SecondaryPrivateIpAddressCount: Integer
  SourceDestCheck: Boolean
  SubnetId: String
  Tags:
    - Tag
```

## PrivateIpAddress

- Primary `Private IP` (IPv4) + more secondaries (optional)

## InterfaceType

- Enhanced Networking (SR-IOV)

- **Elastic Network Adapter** (ENA)

  - Higher `bandwight`, higher `PPS` (packet per second), lower `latency`
  - Up to 100 Gbps
  - Legacy ENA: Intel 82599 VG (10 Gbps)

- **Elastic Fabric Adapter** (EFA)
  - Improved ENA
  - Linux only
  - Inter-node communication
  - Leverages `Message Passing Interface` (MPI): bypasses the underlying linux OS
  - Low latency, reliable transport
