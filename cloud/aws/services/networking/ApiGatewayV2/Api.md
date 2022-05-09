# AWS::ApiGatewayV2::Api

- Serverless API Gateway

![API Gateway](../../../images/api-gateway.png)

- Handle versioning
- Handle different environment (dev, test, prod, ...)
- Handle security (authentication & authorization)
- Request throttling
- Transform and validate requests and responses
- Cache API responses

```yaml
Type: AWS::ApiGatewayV2::Api
Properties:
  ApiKeySelectionExpression: String
  BasePath: String
  Body: Json
  BodyS3Location: BodyS3Location
  CorsConfiguration: Cors
  CredentialsArn: String
  Description: String
  DisableExecuteApiEndpoint: Boolean
  DisableSchemaValidation: Boolean
  FailOnWarnings: Boolean
  Name: String
  ProtocolType: String
  RouteKey: String
  RouteSelectionExpression: String
  Tags: Json
  Target: String
  Version: String
```

- Endpoint Types

  - **Edge-Optimized** (default)
    - For global clients
    - Requests are routed through `CloudFront Edges`
    - But the API Gateway service itself is still bound to a region
  - **Regional**
    - Clients within same region
    - Can manually combine with cloudfront
  - **Private**
    - Accessed from within VPC

- `Request Flow`
  - Client -> Method Request -> Integration Request -> Service
  - Service -> Integration Response -> Method Response -> Client

## ProtocolType

- `HTTP API`: e.g., apps with cors, oauth, oidc
- `WebSocket API`: e.g., chats, dashboards
- `REST API`
