# Identity Providers (IdP)

- IAM identity providers (IdPs) allow you to manage your identities outside of AWS (no need to create users, groups in aws)
- External IdP must be registered in IAM by creating an `IAM identity provider resource`
- Using an IdP might be helpful if your organization already has its own identity system, such as a corporate user directory. Also, if you are creating a mobile app or web application that requires access to AWS resources, an IdP can help keep your AWS account secure. You don’t have to distribute or embed long-term security credentials, such as access keys, in your applications.

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

## IdP Types

IAM supports IdPs that are compatible with:

- **OpenID Connect (OIDC)** (AWS::IAM::OIDCProvider)
  - Also known as `Web Identity Federation`
  - E.g., Facebook IdP, Google IdP, etc (not recommended!)
  - E.g., Cognito (AWS IdP)

- **Security Assertion Markup Language 2.0 (SAML 2.0)** (AWS::IAM::SAMLProvider)
  - The client uses STS to exchange a `saml assertion` for `temporary credentials`

- **Custom Identity Broker**
  - The IdP talks directly to the sts and give the token to the user

- _**AD_**
  - Database of objects (users, files, printers, etc)

- _**SSO_**
