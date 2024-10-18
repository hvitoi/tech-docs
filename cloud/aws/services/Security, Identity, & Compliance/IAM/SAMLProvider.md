# AWS::IAM::SAMLProvider

- Creates an IAM resource that describes an identity provider (IdP) that supports `SAML 2.0`.
- The `SAML provider` resource that you create with this operation can be used as a `principal` in an IAM role's trust policy. Such a policy can enable federated users who sign in using the SAML IdP to assume the role. You can create an IAM role that supports `Web-based single sign-on (SSO)` to the AWS Management Console or one that supports API access to AWS.

- ARN example: `arn:aws:iam::000000000000:saml-provider/okta`

## Identity Providers (IdP)

- IAM identity providers (IdPs) allow you to manage your identities outside of AWS (no need to create users, groups in aws)
- External IdP must be registered in IAM by creating an `IAM identity provider resource`
- To allow users from your IdP to access AWS, `create a role and then trust the IAM identity provider`. Then your users can assume the role to get access to the AWS resources in your account. Example:

```json
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

Using an IdP might be helpful if your organization already has its own identity system, such as a corporate user directory. Also, if you are creating a mobile app or web application that requires access to AWS resources, an IdP can help keep your AWS account secure. You don’t have to distribute or embed long-term security credentials, such as access keys, in your applications.

IAM supports IdPs that are compatible with `OpenID Connect (OIDC)` or `Security Assertion Markup Language 2.0 (SAML 2.0)`

- Identity Providers
  - _SAML 2.0_: the client exchange a saml token for an sts token
  - _Custom Identity Broker_: the IdP talks directly to the sts and give the token to the user
  - _Web Identity Federation_: login on fb, google, etc (not recommended! Use Cognito instead)
  - _SSO_
  - _AD_: database of objects (users, files, printers, etc)

## STS

- `Security Token Service` (STS) is the service used to endorse the roles and get the short term credentials (temporary credentials)
- Generate token with limited and temporary access to AWS resources. The token is valid up to 1 hour, must be refreshed after this
- Identity Providers authenticate with AWS by means of STS. Example: Okta via SAML

- APIs
  - **AssumeRole**
    - User will use a role within your account or cross-account
    ![AssumeRole](.images/sts-assume-role.png)
  - **AssumeRoleWithSaml**: return credentials for users logged in SAML
  - **AssumeRoleWitWebIdentity**: returns credentials for users logged with IdP (fb, google, etc)
  - **GetSessionToken**: for MFA

## Federated Users

- Federated users are not "real users" (AWS::IAM::User), but people that have signed-in assuming a role (via an Identity Provider, e.g., Okta)
- Federated users can log in aws console normally (if the role permits it)
- On the console it appears as follows

```txt
Account ID: 0000-0000-0000
Federated user: my-role/my-sub

my-role/my-sub @ my-aws-account-alias
```

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.html>

```yaml
Type: AWS::IAM::SAMLProvider
Properties:
  Name: String
  SamlMetadataDocument: String
  Tags:
    - Tag
```
