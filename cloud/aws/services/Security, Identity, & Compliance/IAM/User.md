# AWS::IAM::User

- `User` is an identity intended to be used by a person to access aws
- A `root user` is created by default (although it's not good to use it directly)
- Users have `long term credentials`
- `Password policies` can be set for all users under `Account Settings` s to enforce strong password security

## Properties

- <https://docs.aws.amazon.com/pt_br/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html>

```yaml
Type: AWS::IAM::User
Properties:
  Groups:
    - String
  LoginProfile:
    LoginProfile
  ManagedPolicyArns:
    - String
  Path: String
  PermissionsBoundary: String
  Policies:
    - Policy
  Tags:
    - Tag
  UserName: String
```

### PermissionsBoundary

- Supported for `users` and `roles` (not groups)
- Define the maximum permissions an entity can get
- `Permission boundary` (maximum scope) + `permission policies`

![Permission Boundaries](.images/iam-permission-boundaries.png)

- Use cases
  - Deletate responsabilities to non administrators within their permissions boundaries
  - Allow self-assign policies and manage their own permissions
