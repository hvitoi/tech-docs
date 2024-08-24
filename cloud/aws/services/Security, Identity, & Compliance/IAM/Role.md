# AWS::IAM::Role

- `Role` is an identity intended to be used/assumed by another aws service (trusted entity - E.g., ec2, s3)
  - E.g., give an EC2 instance permission to access an S3 bucket
- Roles have `short term credentials` (differently from users that have long term credentials)

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

- When you assume a role (user, application or service), you give up your original permissions and take the permissions assigned to the role
  - Differently from `resource based policies` in which the policies adds up to your already possessed permissions

## AssumeRolePolicyDocument

- **Security Token Service** (STS)
  - Service used to endorse the roles and get the short term credentials (temporary credentials)

- Generate token with `limited` and `temporary` access to AWS resources
- Token is valid up to `1 hour`, must be `refreshed` after this
- `Identity Providers` (IdP) can be used to authenticate with AWS (by means of STS)

- Identity Providers (`IdP`)
  - _SAML 2.0_: the client exchange a saml token for an sts token
  - _Custom Identity Broker_: the IdP talks directly to the sts and give the token to the user
  - _Web Identity Federation_: login on fb, google, etc (not recommended! Use Cognito instead)
  - _SSO_
  - _AD_: database of objects (users, files, printers, etc)

- APIs
  - **AssumeRole API**
    - User will use a role within your account or cross-account
    ![AssumeRole](.images/sts-assume-role.png)
  - **AssumeRoleWithSaml API**: return credentials for users logged in SAML
  - **AssumeRoleWitWebIdentity API**: returns credentials for users logged with IdP (fb, google, etc)
  - **GetSessionToken API**: for MFA

## PermissionsBoundary

- Supported for `users` and `roles` (not groups)
- Define the maximum permissions an entity can get
- `Permission boundary` (maximum scope) + `permission policies`

![Permission Boundaries](.images/iam-permission-boundaries.png)

- Use cases
  - Delete responsibilities to non administrators within their permissions boundaries
  - Allow self-assign policies and manage their own permissions
