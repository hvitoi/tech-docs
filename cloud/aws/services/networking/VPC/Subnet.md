# AWS::EC2::Subnet

- Usually a VPC contains 3 subnets by default. One for each AZ
- The subnet is associated with a VPC and has a CIDR within the range of the CIDR of the VPC
- A subnet is tied to an `AZ`
- AWS reserves the `first 4` and `last 1` IPs in each subnet

- `Private Subnets` usually have a wider range, usually smaller than `/20`
- `Public Subnets` do not need wide range, usually `/24`

- Subnets can have `auto-assign Public IP` to automatically request a public IP for each service within that subnet

```yaml
Type: AWS::EC2::Subnet
Properties:
  AssignIpv6AddressOnCreation: Boolean
  AvailabilityZone: String
  CidrBlock: String
  Ipv6CidrBlock: String
  MapPublicIpOnLaunch: Boolean
  OutpostArn: String
  Tags:
    - Tag
  VpcId: String
```
