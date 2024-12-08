# AWS::Organizations::Organization

- Allow managing multiple AWS accounts
- In AWS either you have one organization or have none, you cannot have multiple organizations. Instead you can have multiple Organizational Units (OU) for your organization
- An organization always have a `management account` (formerly known as "master account") and optionally multiple `member accounts`

## Hierarchy

- An `Organization` contains `Organization Units` which contains `Accounts`
- The `Root OU` of an organization is automatically created and cannot be removed

## Consolidated Billing

- An account `consolidates billing` across all accounts (single payment method)
- With that you benefit from volume discounts for EC2, S3, etc

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organization.html>

```yaml
Type: AWS::Organizations::Organization
Properties:
  FeatureSet: String
```
