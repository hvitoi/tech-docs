# Network Load Balancer (NLB)

- Layer 4
- Ideal for TCP and UDP traffic
- v2 (2017)
- TCP & SSL (L4), UDP (L4)
- High performance (millions of requests per second)
- 100ms latency (400ms in ALB)
- Provides `Static IPs` for each AZ (differently from ALB that provides only the hostname)
- There is not termination in NLB, the request simply `pass through`
- There's no SG for NLB. This way, the only network security is the VPC NACL

![NLB](.images/nlb.png)
