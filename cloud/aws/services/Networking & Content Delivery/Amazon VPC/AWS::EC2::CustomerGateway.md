# AWS::EC2::CustomerGateway

- Software application or physical device
- Must be configured and installed at the `corporation` but added to aws vpc with its `ip address`

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customergateway.html>

```yaml
Type: AWS::EC2::CustomerGateway
Properties:
  BgpAsn: Integer
  BgpAsnExtended: Number
  CertificateArn: String
  DeviceName: String
  IpAddress: String
  Tags:
    - Tag
  Type: String
```
