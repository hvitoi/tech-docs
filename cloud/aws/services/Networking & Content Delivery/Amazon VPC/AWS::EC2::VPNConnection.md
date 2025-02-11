# AWS::EC2::VPNConnection

- **Site to Site VPN (S2S VPN)**
- Links `VPN Gateway` (aws side) to the `Customer Gateway` (corporation side)
- If the Customer Gateway is `public`, use its public ip
- If the Customer Gateway is `private`, use its NAT public IP
- `Route propagation` must be enabled in the VPC

![S2S](.images/vpc-s2s.png)

## CloudHub

- Links `VPN Gateway` (aws side) to the _multiple_ `Customer Gateway` (corporation side)
- `Hub and spoke` model. Hub can communicate with one another

![CloudHub](.images/vpc-s2s-cloudhub.png)

- To set it up, a `Customer Gateway` must be created for each hub
- `Dynamic routing` must be enabled for the s2s connections

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnection.html>

```yaml
Type: AWS::EC2::VPNConnection
Properties:
  CustomerGatewayId: String
  EnableAcceleration: Boolean
  LocalIpv4NetworkCidr: String
  LocalIpv6NetworkCidr: String
  OutsideIpAddressType: String
  RemoteIpv4NetworkCidr: String
  RemoteIpv6NetworkCidr: String
  StaticRoutesOnly: Boolean
  Tags:
    - Tag
  TransitGatewayId: String
  TransportTransitGatewayAttachmentId: String
  TunnelInsideIpVersion: String
  Type: String
  VpnGatewayId: String
  VpnTunnelOptionsSpecifications:
    - VpnTunnelOptionsSpecification
```
