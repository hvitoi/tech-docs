# AWS::ApiGatewayV2::Integration

- Integrations
  - `Lambda Function`
  - `HTTP`
  - `Mock`
  - `AWS Service`
  - `VPC Link`

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html>

```yaml
Type: AWS::ApiGatewayV2::Integration
Properties:
  ApiId: String
  ConnectionId: String
  ConnectionType: String
  ContentHandlingStrategy: String
  CredentialsArn: String
  Description: String
  IntegrationMethod: String
  IntegrationSubtype: String
  IntegrationType: String
  IntegrationUri: String
  PassthroughBehavior: String
  PayloadFormatVersion: String
  RequestParameters:
    Key: Value
  RequestTemplates:
    Key: Value
  ResponseParameters:
    Key: Value
  TemplateSelectionExpression: String
  TimeoutInMillis: Integer
  TlsConfig:
    TlsConfig
```
