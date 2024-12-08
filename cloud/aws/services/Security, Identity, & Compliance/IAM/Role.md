# AWS::IAM::Role

- <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>
- `Role` is an identity intended to be used/assumed by another entity
  - E.g., give an EC2 instance permission to access an S3 bucket (in this case the same could also be achieved with resource-based policies)
- Roles have `short term credentials` (differently from users that have long term credentials)
- A role is associated with `policies`

- <arn:aws:iam:123456789012:role:my-role>

## Revoking active sessions

- You can all current `revoke active sessions` and void the generated temporary credentials
- When you do that, IAM attaches an inline policy named `AWSRevokeOlderSessions` to the role that denies all permissions to all actions
- It includes a condition that applies the restrictions `only if the user assumed the role before the point in time` when you revoke the permissions
- If the user assumes the role after you revoked the permissions, then the deny policy does not apply to that user.

```json
// Inline policy to be attached to the role
{
  "Version": "2012-10-17",
  "Statement": {
    "Effect": "Deny",
    "Action": "*",
    "Resource": "*",
    "Condition": {
      "DateLessThan": {"aws:TokenIssueTime": "2014-05-07T23:47:00Z"}
    }
  }
}
```

## Properties

- <https://docs.aws.amazon.com/pt_br/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>

```yaml
Type: AWS::IAM::Role
Properties:
  AssumeRolePolicyDocument: Json
  Description: String
  ManagedPolicyArns:
    - String
  MaxSessionDuration: Integer
  Path: String
  PermissionsBoundary: String
  Policies:
    - Policy
  RoleName: String
  Tags:
    - Tag
```

### PermissionsBoundary

- Supported for `users` and `roles` (not groups)
- Define the `maximum permissions` that an `IAM entity` (role in this case) can get

```json
// Permission Boundary
// This is the maximum permission that this role can get even if other policies define more
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:*",
        "cloudwatch:*",
        "ec2:*"
      ],
      "Resource": "*"
    }
  ]
}
```

- **Use cases**
  - Delete responsibilities to non administrators within their permissions boundaries. For example to create new IAM users
  - Allow developers to self-assign policies and manage their own permissions, while making sure they can't escalate their privileges
  - Restrict one specific user (instead of of whole account using Organization Policies & SCP)

### ManagedPolicyArns (Permission policies)

- This is where you attach `managed policies` to the role (by its arn)

```shell
aws iam list-attached-role-policies --role-name henrique.vitoi-dev-role
```

### Policies (Permission policies)

- This is where you define `inline policies` directly attached to the role
- These inline policies cannot be reused in other roles

```shell
aws iam list-role-policies --role-name henrique.vitoi-dev-role
```

### AssumeRolePolicyDocument (Trust Policy)

- It's the document that describes what/how entities that can assume this role
- It specifies the conditions under which an entity (like an AWS service, another IAM role, or a user) can take on the permissions associated with the role.
- It specifies the `principal` (the AWS service or account) that is allowed to assume the role (Access Advisor feature)

```shell
# Creating an assumable role via cli
aws iam create-role \
  --role-name MyRole \
  --assume-role-policy-document "file://trust-policy.json"
```

#### Action

##### sts:AssumeRole

- Allow an AWS entity (e.g, an EKS cluster resource, another IAM role) to assume the role

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": [
          "eks.amazonaws.com"
        ]
      }
    }
  ]
}
```

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::123456789012s:role/foo"
    }
  ]
}
```

##### sts:AssumeRoleWithSAML

- Allow an `IdP` (e.g., Okta) to authentication a user via SAML
- The trusted entity is an `Identity Provider` (e.g., `arn:aws:iam::123456789012:saml-provider/okta`)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRoleWithSAML",
      "Principal": {
        "Federated": "arn:aws:iam::123456789012:saml-provider/okta"
      },
      "Condition": {
        "StringEquals": {
          "SAML:sub": "henrique.vitoi",
          "SAML:aud": "https://signin.aws.amazon.com/saml"
        }
      }
    }
  ]
}
```

##### sts:AssumeRoleWithWebIdentity

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Principal": {
        "Federated": "arn:aws:iam::123456789012:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/0123456789ABCDEF0123456789ABCDEF"
      },
      "Condition": {
        "StringEquals": {
          "oidc.eks.us-east-1.amazonaws.com/id/7B4887CC1B7841B1BAEB98263BC64B9C:aud": "sts.amazonaws.com",
          "oidc.eks.us-east-1.amazonaws.com/id/7B4887CC1B7841B1BAEB98263BC64B9C:sub": "system:serviceaccount:kube-system:aws-load-balancer-controller"
        }
      }
    }
  ]
}
```

#### Principal

- The principal is the `trusted entity`. It's "who" can assume a role

##### Service

- Allow AWS services like EC2, Lambda, or others to perform actions in this account

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": [
          "eks.amazonaws.com"
        ]
      }
    }
  ]
}
```

##### Federated

- **SAML 2.0 federation** or **Web identity**

```json
// SAML 2.0 federation (AWS::IAM::SAMLProvider)
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRoleWithSAML",
      "Principal": {
        "Federated": "arn:aws:iam::123456789012:saml-provider/okta"
      },
      "Condition": {
        "StringEquals": {
          "SAML:sub": "henrique.vitoi",
          "SAML:aud": "https://signin.aws.amazon.com/saml"
        }
      }
    }
  ]
}
```

```json
// Web identity (OIDC Provider)
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Principal": {
        "Federated": "arn:aws:iam::123456789012:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/0123456789ABCDEF0123456789ABCDEF"
      },
      "Condition": {
        "StringEquals": {
          "oidc.eks.us-east-1.amazonaws.com/id/7B4887CC1B7841B1BAEB98263BC64B9C:aud": "sts.amazonaws.com",
          "oidc.eks.us-east-1.amazonaws.com/id/7B4887CC1B7841B1BAEB98263BC64B9C:sub": "system:serviceaccount:kube-system:aws-load-balancer-controller"
        }
      }
    }
  ]
}
```

##### AWS

- Allow entities in other `AWS accounts` to assume the role

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:root" // if set to the self account id this allows anything in this account to assume this role
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:root", // ID of the other AWS account
        "Service": [
          "edgelambda.amazonaws.com",
          "lambda.amazonaws.com"
        ]
      }
    }
  ]
}
```
