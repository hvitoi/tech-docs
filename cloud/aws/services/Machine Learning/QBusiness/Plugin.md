# AWS::QBusiness::Plugin

- Connect to data sources not natively supported

![Plugins](.images/plugins.png)

```yaml
Type: AWS::QBusiness::Plugin
Properties:
  ApplicationId: String
  AuthConfiguration:
    PluginAuthConfiguration
  CustomPluginConfiguration:
    CustomPluginConfiguration
  DisplayName: String
  ServerUrl: String
  State: String
  Tags:
    - Tag
  Type: String
```
