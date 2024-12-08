# AWS::ElasticLoadBalancingV2::LoadBalancer

- Forwards traffic to multiple servers (or EC2 instances)
- **Benefits**
  - `Spread load` evenly across multiple downstream instances
  - Expose a single hostname that balances between of the backends in the target groups
  - Handle failure of downstream instances (regular `health check`)
  - `SSL` termination (HTTPS)
  - Enforce `stickiness` with cookies

## Static IPs

- By default the LB is exposed as a hostname that balances between of the backends in the target groups
- Optionally it's also possible to assign an EIP to the Load Balancer and access it via an Static IP
- It's necessary 1 EIP for each AZ in which the LB is deployed
- ALBs do not support EIPs because they operate at Layer 7 and they manage dynamically their networking resources (including Network Interfaces)
- NLBs on the other hand operate at Layer 4 and allow for specific EIP and ENI associations

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html>

```yaml
Type: AWS::ElasticLoadBalancingV2::LoadBalancer
Properties:
  EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: String
  IpAddressType: String
  LoadBalancerAttributes:
    - LoadBalancerAttribute
  Name: String
  Scheme: String
  SecurityGroups:
    - String
  SubnetMappings:
    - SubnetMapping
  Subnets:
    - String
  Tags:
    - Tag
  Type: String
```

### SecurityGroups

- With a LB, the EC2 can have an inbound rule to restricting access only from the LB (instead of allowing from anywhere)

![LB SG](.images/lb-security-group.png)

### LoadBalancerAttributes

- **load_balancing.cross_zone.enabled**
  - Balance between instances in different AZs
  - However, a LB in a region cannot forward load to another region (in this case one LB in each region is necessary)
  - `With Cross-Zone balancing` load is distributed evenly across all instances (in all AZs)
    - It's always enabled for ALB (cannot be disabled). It's free
    - It's enabled (by default) for CLB. It's free
    - It's disabled (by default) for NLB. It's paid
  - `Without Cross-Zone balancing` load is distributed for the AZ, and not for the total of instances itself
    ![Cross-Zone Load Balancing](.images/cross-zone-balancing.png)

### Scheme

- LB can be **internal** or **internet-facing**

### Type

- Application Load Balancer (ALB)
- Network Load Balancer (NLB)
- Gateway Load Balancer (GWLB)

> Classic Load Balancer (CLB) is created with AWS::ElasticLoadBalancing::LoadBalancer
