# AWS::XRay::Group

- X-Ray provides an `end-to-end view of requests` as they travel through your application
- Show a map of your application’s underlying components
- You can use X-Ray to collect data `across AWS Accounts`

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html>

```yaml
Type: AWS::XRay::Group
Properties:
  FilterExpression: String
  GroupName: String
  InsightsConfiguration:
    InsightsConfiguration
  Tags:
    - Tag
```
