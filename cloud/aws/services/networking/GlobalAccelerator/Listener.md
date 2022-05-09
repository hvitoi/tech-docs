# AWS::GlobalAccelerator::Listener

- 2 external IPs need to be whitelisted
- DDoS protection with `AWS Shield`

```yaml
Type: AWS::GlobalAccelerator::Listener
Properties:
  AcceleratorArn: String
  ClientAffinity: String
  PortRanges:
    - PortRange
  Protocol: String
```
