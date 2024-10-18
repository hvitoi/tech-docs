# AWS::IAM::AccessKey

- **Access Keys** can be generated per IAM user or root user under `Security credentials`

- Ways to access AWS
  - `Management Console`: password + MFA
  - `Command Line Interface`: access key id + secret access key or with cloud shell
  - `Software Development Kit`: access key id + secret access key

## Properties

- <https://docs.aws.amazon.com/pt_br/AWSCloudFormation/latest/UserGuide/aws-resource-iam-accesskey.html>

```yaml
Type: AWS::IAM::AccessKey
Properties:
  Serial: Integer
  Status: String
  UserName: String
```
