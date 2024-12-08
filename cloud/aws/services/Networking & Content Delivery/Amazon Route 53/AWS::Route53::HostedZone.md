# AWS::Route53::HostedZone

- A container for the records
- Define how to traffic to a domain a subdomains
- `$0.50` per month per hosted zone on Route 53
- `Public Hosted Zone`: how to route traffic on the internet
- `Private hosted Zone`: how to route traffic within one or more PVCs (private domain names)
- Domains registered in Route53 are automatically added to a HostedZone, but you can also register a domain somewhere else (e.g. godaddy) and create a hosted zone for it in Route 53 manually

## Private vs. Public Hosted Zones

![DNS Zones](.images/dns-zone.png)

- In order to use `private hosted zone`, the VPC must:
  - `enableDnsSupport` set to true
  - `enableDnsHostname` set to true
- A private hosted zone is accessible within a VPC

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html>

```yaml
Type: AWS::Route53::HostedZone
Properties:
  HostedZoneConfig:
    HostedZoneConfig
  HostedZoneTags:
    - HostedZoneTag
  Name: String
  QueryLoggingConfig:
    QueryLoggingConfig
  VPCs:
    - VPC
```
