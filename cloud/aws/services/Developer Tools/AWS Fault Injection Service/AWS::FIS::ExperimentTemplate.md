# AWS::FIS::ExperimentTemplate

- **Fault Injection Simulator** is a managed `chaos engineering service`
- It's about injecting faults in a controlled environment (with guardrails)
- FIS provides templates that `generate disruptions`
- To run experiments, you first create an experiment template, which is a blueprint of the experiment.

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

### RoleArn

- It's the IAM role that grants AWS FIS the permissions required so that it can run experiments on your behalf
- E.g., permissions to stress pods on EKS cluster
- For a `single-account experiment`, the IAM policy for the experiment role must grant permission to modify the resources that you specify as targets in your experiment template
- For a `multi-account experiment`, the experiment role must grant the orchestrator role permission to assume the IAM role for each target account.

### Targets

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

### Actions

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

### StopConditions

```yaml
Source: String
Value: String
```

- When to stop the experiment
- Can be based on CloudWatch alarms

### ExperimentOptions

```yaml
AccountTargeting: String
EmptyTargetResolutionMode: String
```

- `AccountTargeting`
  - _single-account_: the target lives in the same aws account as the template
  - _multi-account_: the target lives in another aws account other

### LogConfiguration

- Specifies the configuration for experiment logging.

```yaml
CloudWatchLogsConfiguration:
  CloudWatchLogsConfiguration
LogSchemaVersion: Integer
S3Configuration:
  S3Configuration
```
