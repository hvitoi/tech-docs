# AWS::SNS::Subscription

- Subscribers can be
  - SQS
  - HTTPS
  - Lambda
  - Email
  - ...

```yaml
Type: AWS::SNS::Subscription
Properties:
  DeliveryPolicy: Json
  Endpoint: String
  FilterPolicy: Json
  Protocol: String
  RawMessageDelivery: Boolean
  RedrivePolicy: Json
  Region: String
  SubscriptionRoleArn: String
  TopicArn: String
```
