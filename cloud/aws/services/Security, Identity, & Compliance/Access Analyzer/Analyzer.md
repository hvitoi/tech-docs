# AWS::AccessAnalyzer::Analyzer

- Find out which resources are shared externally
  - S3 buckets
  - IAM roles
  - KMS keys
  - Lambda functions and layers
  - SQS queues
  - Secrets Manager secrets

- Define a `Zone of Trust` (aws account or aws organization)
  - Any access of outside the zone of trust will be reported as findings

## Features

- **IAM Credentials Report**
  - Account-level
  - Report of all users and their statuses

- **IAM Access Advisor**
  - User-level
  - Show services accessed by a user in a time period

- **Policy Validation**
  - Validate the policies against IAM policy grammar
  - Give recommendations on actions and best practices

- **Policy Generation**
  - Generate policies directly from AccessAnalyzer
  - Based on access activity (uses CloudTrail logs as access data)

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
