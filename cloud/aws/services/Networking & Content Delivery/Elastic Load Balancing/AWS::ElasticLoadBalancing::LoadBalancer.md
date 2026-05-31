# AWS::ElasticLoadBalancing::LoadBalancer

- It's a deprecated LB. Use `AWS::ElasticLoadBalancingV2::LoadBalancer` instead

- **Classic LB** (CLB)
  - v1 (2009)
  - Types
    - TCP & SSL (Layer 4)
    - HTTP & HTTPS (Layer 7)
  - Health checks TCP-based or HTTP-based
  - `Fixed hostname` xxx.region.elb.amazonaws.com
  - Client -> LB -> App (app receives LB ip, not client's)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancing-loadbalancer.html>

