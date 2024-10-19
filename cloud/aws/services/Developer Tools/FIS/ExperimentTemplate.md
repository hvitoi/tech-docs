# AWS::FIS::ExperimentTemplate

- **Fault Injection Simulator** is a managed `chaos engineering service`
- It's about injecting faults in a controlled environment (with guardrails)
- FIS provides templates that `generate disruptions`

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html>

```yaml
Type: AWS::FIS::ExperimentTemplate
Properties:
  Actions:
    Key: Value
  Description: String
  ExperimentOptions:
    ExperimentTemplateExperimentOptions
  LogConfiguration:
    ExperimentTemplateLogConfiguration
  RoleArn: String
  StopConditions:
    - ExperimentTemplateStopCondition
  Tags:
    Key: Value
  Targets:
    Key: Value
```

## Targets

```yaml
Filters:
  - ExperimentTemplateTargetFilter
Parameters:
  Key: Value
ResourceArns:
  - String
ResourceTags:
  Key: Value
ResourceType: String
SelectionMode: String
```

- A target is a specific resource in your AWS environment
  - EC2
  - Databases
  - Networking
  - Storage
- Can be matched by tags
- Can be defined a population (percentage or count)

## Actions

```yaml
ActionId: String
Description: String
Parameters:
  Key: Value
StartAfter:
  - String
Targets:
  Key: Value
```

- The actions to carry out on the target
- `Action Types`
  - CLOUDWATCH
  - EBS
  - EC2
    - aws:ec2:reboot-instances
    - aws:ec2:send-spot-instance-interruptions
    - aws:ec2:stop-instances
    - aws:ec2:terminate-instances
  - EC2/SSm
  - ECS
  - EKS
  - FIS
  - NETWORK
  - RDS
  - SSM

## StopConditions

```yaml
Source: String
Value: String
```

- When to stop the experiment
- Can be based on CloudWatch alarms

## ExperimentOptions

```yaml
AccountTargeting: String
EmptyTargetResolutionMode: String
```

## LogConfiguration

- Specifies the configuration for experiment logging.

```yaml
CloudWatchLogsConfiguration:
  CloudWatchLogsConfiguration
LogSchemaVersion: Integer
S3Configuration:
  S3Configuration
```
