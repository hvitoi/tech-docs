# AWS::OpsWorks::App

- Managed `Chef` & `Puppet`
- Manage `configuration as code`
- They leverage `recipes` (`manifests`)
- Perform server configuration automatically
- Alternative to SSM

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html>

```yaml
Type: AWS::OpsWorks::App
Properties:
  AppSource:
    Source
  Attributes:
    Key: Value
  DataSources:
    - DataSource
  Description: String
  Domains:
    - String
  EnableSsl: Boolean
  Environment:
    - EnvironmentVariable
  Name: String
  Shortname: String
  SslConfiguration:
    SslConfiguration
  StackId: String
  Type: String
```
