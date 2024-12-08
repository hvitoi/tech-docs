# AWS::AccessAnalyzer::Analyzer

- Simplify your journey to least privilege
- Workflow
  1. Create an analyzer
  1. Review findings
  1. Take action

## Features

### External access findings

- Define a **Zone of Trust** within the `AWS Account` and `AWS Organization` that you own
- Any access from outside the zone of trust (3rd parties) will be reported as `findings`
- Monitored resources
  - S3 buckets
  - IAM roles
  - KMS keys
  - Lambda functions and layers
  - SQS queues
  - Secrets Manager secrets

### Unused access findings

- Previously known as `Access Advisor`
- Inspect IAM users and roles with unused access to refine permissions.
- Useful to spot policies not used for a long time (and remove it)

### Custom policy check (policy validation)

- Validate the policies against IAM policy grammar
- Validate that your policies adhere to your security standards ahead of deployments
- Give recommendations on actions and best practices with actionable recommendations

### Policy generation

- Generate policies directly from AccessAnalyzer
- Uses `CloudTrail Logs` to get the access activity on the resource and elaborate a `fine-grained policy` based on minimum permissions captured by CloudTrail.
- Reviews logs for up to 90 days

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
