# AWS::IAM::Role

- <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>
- `Role` is an identity intended to be used/assumed by another entity
  - E.g., give an EC2 instance permission to access an S3 bucket (in this case the same could also be achieved with resource-based policies)
- Roles have `short term credentials` (differently from users that have long term credentials)
- A role is associated with `policies`

- <arn:aws:iam:123456789012:role:my-role>

## Assuming a role

- When a role is assumed, the entity assuming the role `gives up the original permissions` and take the permissions assigned to the assumed role
- In order to assume a role and get a token with the permissions defined in the role, an `Identity Provider` (see AWS::IAM::SAMLProvider or AWS::IAM::OIDCProvider) is needed to guarantee that whoever is trying to assume a role is indeed the person/entity
- An assumable role is defined by the `AssumeRolePolicyDocument` property (see below)

- The assumed role is represented by the ARN `arn:aws:sts::<aws-account>:assumed-role/<role-name>/<sub>`
  - Where "sub" is the sub/principal/session name

- When assuming a role (e.g., via `aws sts assume-role` or `aws sts assume-role-with-saml`) temporary credentials are returned. These credentials can be used to access aws resources
- The AWS `Security Token Service` (STS) is used to assume a role and get the temporary credentials

```json
// temp-credentials.json
{
  "Credentials": {
    "AccessKeyId": "...",
    "SecretAccessKey": "...",
    "SessionToken": "...",
    "Expiration": "2024-11-16T16:57:39+00:00"
  },
  "AssumedRoleUser": {
    "AssumedRoleId": "1234:henrique.vitoi",
    "Arn": "arn:aws:sts::123456789012:assumed-role/my-role/henrique.vitoi"
  },
  "Subject": "henrique.vitoi",
  "SubjectType": "urn:oasis:names:tc:SAML:1.1:nameid-format:x509SubjectName",
  "Issuer": "http://www.okta.com/asdf",
  "Audience": "https://signin.aws.amazon.com/saml",
  "NameQualifier": "..."
}
```

```shell
export AWS_ACCESS_KEY_ID=$(jq -r '.Credentials.AccessKeyId' temp-credentials.json)
export AWS_SECRET_ACCESS_KEY=$(jq -r '.Credentials.SecretAccessKey' temp-credentials.json)
export AWS_SESSION_TOKEN=$(jq -r '.Credentials.SessionToken' temp-credentials.json)

cat >> ~/.aws/credentials <<EOL
[default]
aws_access_key_id = $AWS_ACCESS_KEY_ID
aws_secret_access_key = $AWS_SECRET_ACCESS_KEY
aws_session_token = $AWS_SESSION_TOKEN
EOL
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

### Policies

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

- Allow entities in `AWS accounts` belonging to you or a 3rd party to perform actions in this account

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
