# AWS::EC2::VPCCidrBlock

- Associates a CIDR block with your VPC

```yaml
Type: AWS::EC2::VPCCidrBlock
Properties:
  AmazonProvidedIpv6CidrBlock: Boolean
  CidrBlock: String
  Ipv6CidrBlock: String
  Ipv6Pool: String
  VpcId: String
```

## Ipv6CidrBlock

- `xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx` (8 times - Each x is hexadecimal)
- You can only associate a `single IPv6 CIDR` block with your VPC

- Each IPv6 address only `public` (no private range)
- Even with IPv4, IPv6 cannot be disabled
- `Auto assign IPv6` can be enabled
- The IPv6 CIDR block size is fixed at `/56`
