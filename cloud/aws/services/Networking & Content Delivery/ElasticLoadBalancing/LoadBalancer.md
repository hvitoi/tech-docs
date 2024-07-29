# AWS::ElasticLoadBalancing::LoadBalancer

- **Classic LB** (CLB)

  - v1 (2009) - Deprecated
  - TCP & SSL (L4), HTTP & HTTPS (L7)
  - Health checks TCP-based or HTTP-based
  - `Fixed hostname` xxx.region.elb.amazonaws.com
  - Client -> LB -> App (app receives LB ip, not client's)
