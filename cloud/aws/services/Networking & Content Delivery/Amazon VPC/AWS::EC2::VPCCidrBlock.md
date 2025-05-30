# AWS::EC2::VPCCidrBlock

- Associates a CIDR block with your VPC

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html>

```yaml
Type: AWS::EC2::VPCCidrBlock
Properties:
  AmazonProvidedIpv6CidrBlock: Boolean
  CidrBlock: String
  Ipv4IpamPoolId: String
  Ipv4NetmaskLength: Integer
  Ipv6CidrBlock: String
  Ipv6IpamPoolId: String
  Ipv6NetmaskLength: Integer
  Ipv6Pool: String
  VpcId: String
```

### Ipv6CidrBlock

- `xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx` (8 times - Each x is hexadecimal)
- You can only associate a `single IPv6 CIDR` block with your VPC

- Each IPv6 address only `public` (no private range)
- Even with IPv4, IPv6 cannot be disabled
- `Auto assign IPv6` can be enabled
- The IPv6 CIDR block size is fixed at `/56`
