# AWS::FIS::ExperimentTemplate

- **Fault Injection Simulator** is a managed `chaos engineering service`
- It's about injecting faults in a controlled environment (with guardrails)
- FIS provides templates that `generate disruptions`

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

## Actions

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

- When to stop the experiment
- Can be based on CloudWatch alarms

## Targets

- A target is a specific resource in your AWS environment
  - EC2
  - Databases
  - Networking
  - Storage
- Can be matched by tags
- Can be defined a population (percentage or count)
