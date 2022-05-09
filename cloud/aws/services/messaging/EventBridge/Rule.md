# AWS::Events::Rule

- Rules are definitions on how to process the events from an event bus
- Rules are defined in JSON documents
- Rules can be constructed based on a `event pattern` or `scheduled`

```yaml
Type: AWS::Events::Rule
Properties:
  Description: String
  EventBusName: String
  EventPattern: Json
  Name: String
  RoleArn: String
  ScheduleExpression: String
  State: String
  Targets:
    - Target
```
