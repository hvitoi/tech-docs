# AWS::ApiGatewayV2::Authorizer

## IAM through Sig v4

- Leverages `Sig v4` capability where IAM credentials are in headers

![Sig v4](.images/apigateway-sigv4.png)

## Lambda Authorizer (custom authorizer)

- Uses `AWS Lambda` to valdiate the token in the request
- Good when using OAuth, SAML, etc
- The lambda must return an iam policy as a result

![Lambda Authorizer](.images/apigateway-lambda-authorizer.png)

## Cognito User Pools

- `Cognito` manages the user lifecycle
- API gateway will verify identity from `AWS Cognito`
- Only authentication (not authorization)

![Cognito User Pools](.images/apigateway-user-cognito-pools.png)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html>

```yaml
Type: AWS::ApiGatewayV2::Authorizer
Properties:
  ApiId: String
  AuthorizerCredentialsArn: String
  AuthorizerPayloadFormatVersion: String
  AuthorizerResultTtlInSeconds: Integer
  AuthorizerType: String
  AuthorizerUri: String
  EnableSimpleResponses: Boolean
  IdentitySource:
    - String
  IdentityValidationExpression: String
  JwtConfiguration:
    JWTConfiguration
  Name: String
```
