# AWS::ElasticLoadBalancing::LoadBalancer

- It's a deprecated LB. Use `AWS::ElasticLoadBalancingV2::LoadBalancer` instead

- **Classic LB** (CLB)
  - v1 (2009)
  - TCP & SSL (L4), HTTP & HTTPS (L7)
  - Health checks TCP-based or HTTP-based
  - `Fixed hostname` xxx.region.elb.amazonaws.com
  - Client -> LB -> App (app receives LB ip, not client's)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancing-loadbalancer.html>

```yaml
Type: AWS::ElasticLoadBalancing::LoadBalancer
Properties:
  AccessLoggingPolicy:
    AccessLoggingPolicy
  AppCookieStickinessPolicy:
    - AppCookieStickinessPolicy
  AvailabilityZones:
    - String
  ConnectionDrainingPolicy:
    ConnectionDrainingPolicy
  ConnectionSettings:
    ConnectionSettings
  CrossZone: Boolean
  HealthCheck:
    HealthCheck
  Instances:
    - String
  LBCookieStickinessPolicy:
    - LBCookieStickinessPolicy
  Listeners:
    - Listeners
  LoadBalancerName: String
  Policies:
    - Policies
  Scheme: String
  SecurityGroups:
    - String
  Subnets:
    - String
  Tags:
    - Tag
```
