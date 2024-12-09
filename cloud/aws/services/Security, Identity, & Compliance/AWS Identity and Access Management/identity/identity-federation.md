# Identity federation

- Give users outside of AWS permissions to access AWS resources in your account
- `Federated users` are not "real users" (AWS::IAM::User), but entities that have signed-in assuming a role (via an `Identity Provider`, e.g., Okta)
- Federated users can log in aws console normally (if the role permits it)
- **Use cases**
  - If your organization already has its own `identity system`, such as a corporate user directory
  - If you are creating a mobile app or web application that requires access to AWS resources directly

```conf
# aws console menu
Account ID: 0000-0000-0000
Federated user: my-role/my-sub

my-role/my-sub @ my-aws-account-alias
```

## Identity Providers (IdP)

- IAM identity providers (IdPs) allow you to manage your identities outside of AWS (no need to create users, groups in aws)
- External IdP must be registered in IAM and thus creating a `trust relationship`

### OpenID Connect (AWS::IAM::OIDCProvider)

- `OIDC` Provider. Also known as `Web Identity Federation`
- In this method, you don't know your customers (e.g., web application in which the user can sign-in directly)
- With that you don’t have to distribute or embed long-term security credentials, such as access keys, in your applications
- Examples:
  - Facebook IdP
  - Google IdP
- The `Cognito` service can be added to the flow before requesting STS. This approach is preferred because:
  - It supports `anonymous users`
  - It supports `MFA`
  - It supports `data synchronization`

![OIDC](.images/idp-oidc.png)
![OIDC with Cognito](.images/idp-oidc-with-cognito.png)

```json
// Allow users to access only their own bucket
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::mybucket",
      "Condition": {
        "StringLike": {
          "s3:prefix": [
            "myapp/${www.amazon.com:user_id}/*"
          ]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": [
        "arn:aws:s3:::mybucket/myapp/${www.amazon.com:user_id}",
        "arn:aws:s3:::mybucket/myapp/${www.amazon.com:user_id}/*"
      ]
    }
  ]
}
```

### SAML 2.0 (AWS::IAM::SAMLProvider)

- `Security Assertion Markup Language 2.0`
- The client uses STS to exchange a `saml assertion` for `temporary credentials`
- Examples:
  - Okta
  - Microsoft Active Directory Federations Services (ADFS)

![AssumeRole via SAML 2.0 for AWS API](.images/idp-saml.png)
![AssumeRole via SAML 2.0 for AWS Console](.images/idp-saml-console.png)

### IAM Identity Center (AWS::SSO::Instance)

- Formerly named `SSO`
- The new recommended way

### Custom Identity Broker

- Old method, not recommended. Use it only if your IdP is not compatible with SAML 2.0
- The IdP talks directly to the STS and give the token to the user. Uses the `assume-role` or `get-federation-token` on behalf of the user

![Custom Identity Broker](.images/idp-custom-identity-broker.png)

## Assumable Role

- To allow users from your IdP to access AWS, `create a role with a trust policy that trusts the IAM identity provider`. Then your users can assume the role to get access to the AWS resources in your account. Example:

```json
// Assumable Role Example
{
  "Path": "/",
  "RoleName": "my-role",
  "RoleId": "ABCDEPAC2724CE5NCJXYZ",
  "Arn": "arn:aws:iam::000000000000:role/my-role",
  "CreateDate": "2024-10-15T13:24:07+00:00",
  "AssumeRolePolicyDocument": {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Federated": "arn:aws:iam::000000000000:saml-provider/okta" // trust the okta identity provider
        },
        "Action": "sts:AssumeRoleWithSAML",
        "Condition": {
          "StringEquals": {
            "SAML:aud": "https://signin.aws.amazon.com/saml",
            "SAML:sub": "john.doe"
          }
        }
      }
    ]
  }
}
```
