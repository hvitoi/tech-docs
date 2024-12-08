# AWS::EC2::Host

- It's a `Dedicated Host`
- Book an entire `physical server`
- Control instance placement
- Address `compliance requirements`
- Use existing `server-bound software licenses`
- Minimum of `3 years`

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html>

```yaml
Type: AWS::EC2::Host
Properties:
  AssetId: String
  AutoPlacement: String
  AvailabilityZone: String
  HostMaintenance: String
  HostRecovery: String
  InstanceFamily: String
  InstanceType: String
  OutpostArn: String
```
