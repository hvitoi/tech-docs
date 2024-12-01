# AWS::IAM::ManagedPolicy

- A policy that can be reused. In contract to inline policies (AWS::IAM::Policy) that cannot eb reused

## Types

- **Customer Managed**
  - This are the policies in fact created with the AWS::IAM::ManagedPolicy resource
  - These are policies defined by the user (you) that can be reused

- **AWS Managed**
  - This are "built-in" policies created by aws
  - Example: `arn:aws:iam::aws:policy/AdministratorAccess`

> "Inline Policy" and "Resource Based Policy" are not managed policies

## Properties

- <https://docs.aws.amazon.com/pt_br/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html>

```yaml
Type: AWS::IAM::ManagedPolicy
Properties:
  Description: String
  Groups:
    - String
  ManagedPolicyName: String
  Path: String
  PolicyDocument: Json
  Roles:
    - String
  Users:
    - String
```

### PolicyDocument

```json
// AdministratorAccess (AWS Managed)
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
```

```json
// AmazonEKSClusterPolicy (AWS Managed)
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Resource": "*",
      "Action": [
        "autoscaling:DescribeAutoScalingGroups",
        "ec2:AttachVolume",
        "elasticloadbalancing:AddTags",
        "elasticloadbalancing:SetLoadBalancerPoliciesOfListener",
        "kms:DescribeKey",
        "..."
      ]
    },
    {
      "Effect": "Allow",
      "Resource": "*",
      "Action": "iam:CreateServiceLinkedRole",
      "Condition": {
        "StringEquals": {
          "iam:AWSServiceName": "elasticloadbalancing.amazonaws.com"
        }
      }
    }
  ]
}
```

```json
// PowerUserAccess (AWS Managed)
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "NotAction": [
        "iam:*",
        "organizations:*",
        "account:*"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:CreateServiceLinkedRole",
        "iam:DeleteServiceLinkedRole",
        "iam:ListRoles",
        "organizations:DescribeOrganizations",
        "account:ListRegions"
      ],
      "Resource": "*"
    }
  ]
}
```
