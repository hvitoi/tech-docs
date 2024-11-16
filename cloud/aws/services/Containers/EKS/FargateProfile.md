# AWS::EKS::FargateProfile

- Run workloads on `Serverless Fargate Profiles` (instead of EC2 instances)
- With fargate, it's not necessary to configure and manage node groups (and auto scaling groups)

## Properties

```yaml
Type: AWS::EKS::FargateProfile
Properties:
  ClusterName: String
  FargateProfileName: String
  PodExecutionRoleArn: String
  Selectors:
    - Selector
  Subnets:
    - String
  Tags:
    - Tag
```
