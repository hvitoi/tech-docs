# AWS::GlobalAccelerator::EndpointGroup

- Information about how you create an `endpoint group` for the specified `listener`
- Use `endpoint weights` to determine the proportion of traffic that is directed to endpoints in an endpoint group

```yaml
Type: AWS::GlobalAccelerator::EndpointGroup
Properties:
  EndpointConfigurations:
    - EndpointConfiguration
  EndpointGroupRegion: String
  HealthCheckIntervalSeconds: Integer
  HealthCheckPath: String
  HealthCheckPort: Integer
  HealthCheckProtocol: String
  ListenerArn: String
  PortOverrides:
    - PortOverride
  ThresholdCount: Integer
  TrafficDialPercentage: Double
```

## EndpointConfigurations

- Elastic IP
- EC2 Instances
- ALB/NLB

## EndpointGroupRegion

- The `endpoint group` is scoped to a region. Within that region, you can select the aws resource (elb, ec2, etc)
