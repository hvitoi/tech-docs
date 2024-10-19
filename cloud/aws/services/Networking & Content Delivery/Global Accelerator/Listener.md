# AWS::GlobalAccelerator::Listener

- 2 external IPs need to be whitelisted
- DDoS protection with `AWS Shield`

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html>

```yaml
Type: AWS::GlobalAccelerator::Listener
Properties:
  AcceleratorArn: String
  ClientAffinity: String
  PortRanges:
    - PortRange
  Protocol: String
```
