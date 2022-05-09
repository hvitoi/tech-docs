# AWS::IAM::Policy

- **Inline policy**!

- An `inline policy` can be created on the fly, so that the policy is created only for that entity and cannot be reused

```yaml
Type: AWS::IAM::Policy
Properties:
  Groups:
    - String
  PolicyDocument: Json
  PolicyName: String
  Roles:
    - String
  Users:
    - String
```
