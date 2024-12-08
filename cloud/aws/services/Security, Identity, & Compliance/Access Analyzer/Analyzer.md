# AWS::AccessAnalyzer::Analyzer

- Simplify your journey to least privilege
- Workflow
  1. Create an analyzer
  1. Review findings
  1. Take action

## Features

### External access findings

- Verify that external access granted to a resource in your account or organization is required.
- Find out which resources are shared externally
  - S3 buckets
  - IAM roles
  - KMS keys
  - Lambda functions and layers
  - SQS queues
  - Secrets Manager secrets
- Define a `Zone of Trust` (aws account or aws organization)
- Any access of outside the zone of trust will be reported as findings

### Unused access findings

- Previously known as `Access Advisor`
- Inspect IAM users and roles with unused access to refine permissions.
- Useful to spot policies not used for a long time (and remove it)

### Custom policy check (policy validation)

- Validate the policies against IAM policy grammar
- Validate that your policies adhere to your security standards ahead of deployments
- Give recommendations on actions and best practices

### Policy generation

- Generate policies directly from AccessAnalyzer
- Based on access activity (uses CloudTrail logs as access data)
- Generate a fine-grained policy based on the access activity captured in your CloudTrail logs.

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html>

```yaml
Type: AWS::AccessAnalyzer::Analyzer
Properties:
  AnalyzerConfiguration:
    AnalyzerConfiguration
  AnalyzerName: String
  ArchiveRules:
    - ArchiveRule
  Tags:
    - Tag
  Type: String
```

### Type

- `External access` or `Unused access`
