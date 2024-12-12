# AWS::Events::Rule

- The basis of EventBridge is to create rules that route events to a target.

## EventBridge

> EventBridge was previously known as CloudWatch Events

- Each AWS Service emits usage information to EventBridge. It's an internal Event Broker for AWS-related events
- With EventBridge, you can create rules that trigger programmatic actions in response to an event.
- For example, you can configure a rule that invokes an SNS topic to send an email notification or invokes a Lambda function to take some action.

![EventBridge S3](.images/eventbridge-s3.png)

```json
// AWS FIS event
{
  "version": "0",
  "id": "77579212-a04a-94b7-97a9-58abdce09593",
  "detail-type": "FIS Experiment State Change",
  "source": "aws.fis",
  "account": "123456789012",
  "time": "2021-12-09T19:20:19Z",
  "region": "us-east-1",
  "resources": [ "arn:aws:fis:us-east-1:123456789012:experiment/EXP123abc123abc123" ],
  "detail": {
    "experiment-id": "EXP123abc123abc123",
    "new-state": {
      "status": "completed",
      "reason": "Experiment completed."
    },
    "old-state": {
      "status": "running",
      "reason": "Experiment is running."
    }
  }
}
```

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html>

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

```yaml
# Example
AWSTemplateFormatVersion: "2010-09-09"
Description: FIS Events Routing
Resources:
  ExperimentStateChangeQueue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: FisExperimentStateChangeQueue
      MessageRetentionPeriod: 300
      SqsManagedSseEnabled: true
  FisExperimentStateChange:
    Type: AWS::Events::Rule
    Properties:
      EventPattern:
        source:
          - aws.fis
        detail-type:
          - FIS Experiment State Change
      Targets:
        - Id: ExperimentStateChangeQueueTarget
          Arn: !GetAtt ExperimentStateChangeQueue.Arn
```

### EventPattern

- Rules are definitions on how to process the events from an event bus
- Rules can be constructed based on a `event pattern` or `scheduled`

### EventBusName

- Uses the `default` Bus (AWS::Events::EventBus) by default
