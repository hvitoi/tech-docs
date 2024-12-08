# AWS::AppSync::GraphQLApi

- Store `sync data` across `mobile` and `webapps` in real-time
- It's a managed `GraphQL backend`
- Offline data synchronization (replaces cognito sync)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html>

```yaml
Type: AWS::AppSync::GraphQLApi
Properties:
  AdditionalAuthenticationProviders:
    - AdditionalAuthenticationProvider
  ApiType: String
  AuthenticationType: String
  EnhancedMetricsConfig:
    EnhancedMetricsConfig
  EnvironmentVariables: Json
  IntrospectionConfig: String
  LambdaAuthorizerConfig:
    LambdaAuthorizerConfig
  LogConfig:
    LogConfig
  MergedApiExecutionRoleArn: String
  Name: String
  OpenIDConnectConfig:
    OpenIDConnectConfig
  OwnerContact: String
  QueryDepthLimit: Integer
  ResolverCountLimit: Integer
  Tags:
    - Tag
  UserPoolConfig:
    UserPoolConfig
  Visibility: String
  XrayEnabled: Boolean
```
