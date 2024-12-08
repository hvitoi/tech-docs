# AWS::SNS::Subscription

- Subscribers can be
  - SQS
  - HTTPS
  - Lambda
  - Email
  - ...

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html>

```yaml
Type: AWS::SNS::Subscription
Properties:
  DeliveryPolicy: Json
  Endpoint: String
  FilterPolicy: Json
  FilterPolicyScope: String
  Protocol: String
  RawMessageDelivery: Boolean
  RedrivePolicy: Json
  Region: String
  ReplayPolicy: Json
  SubscriptionRoleArn: String
  TopicArn: String
```
