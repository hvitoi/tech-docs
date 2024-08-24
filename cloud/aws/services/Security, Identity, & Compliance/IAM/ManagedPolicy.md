# AWS::IAM::ManagedPolicy

- `Permission Policy` is a JSON document that define a set permissions for making requests to AWS services
- Policies can be applied to `Users`, `Groups` and `Roles`

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

## Examples

### AdministratorAccess

- Provides full access to AWS services and resources

```json
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

### PowerUserAccess

```json
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
