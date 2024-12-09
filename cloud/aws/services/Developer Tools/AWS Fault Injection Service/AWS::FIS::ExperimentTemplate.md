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

A target is a specific resource in your AWS environment

- **ResourceType**
  - EKS
    - `aws:eks:cluster`
    - `aws:eks:nodegroup`
    - `aws:eks:pod`

  - EC2
    - `aws:ec2:autoscaling-group`
    - `aws:ec2:ebs-volume`
    - `aws:ec2:instance`
    - `aws:ec2:spot-instance`
    - `aws:ec2:subnet`
    - `aws:ec2:transit-gateway`

  - ECS
    - `aws:ecs:cluster`
    - `aws:ecs:task`

  - IAM
    - `aws:iam:role`

  - Lambda
    - `aws:lambda:function`

  - DynamoDB
    - `aws:dynamodb:global-table`

  - S3
    - `aws:s3:bucket`

  - Elasticache
    - `aws:elasticache:redis-replicationgroup`

  - RDS
    - `aws:rds:cluster`
    - `aws:rds:db`

- **SelectionMode**
  - COUNT(1)
  - PERCENT(50)
  - ALL

- **parameters**
  - It's a resource-specific
  - For EKS, it can be matched by labels or deployment name

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

The actions to carry out on the target

- _ActionId_

  - **CloudWatch**
    - `aws:cloudwatch:assert-alarm-state`: Assert that teh CloudWatch alarms are in the expected states

  - **DynamoDB**
    - `aws:dynamodb:global-table-pause-replication`: Pause data replication of the replica tables in current region to/from other regions

  - **EBS**
    - `aws:ebs:pause-volume-io`: Pauses IO for a set of EBS volumes

  - **EC2**
    - `aws:ec2:api-insufficient-instance-capacity-error`: Cause the EC2 service to return insufficient capacity error responses for specific callers
    - `aws:ec2:asg-insufficient-instance-capacity-error`: Cause the targeted AutoScaling Groups to receive insufficient instance capacity errors when attempting to provision new instances
    - `aws:ec2:reboot-instances`: Reboot the specified EC2 instances
    - `aws:ec2:send-spot-instance-interruptions`: Interrupt the specified EC2 Spot instances
    - `aws:ec2:stop-instances`: Stop the specified EC2 instances
    - `aws:ec2:terminate-instances`: Terminate the specified EC2 instances

  - **ECS**
    - `aws:ecs:drain-container-instances`: Drain percentage of underlying EC2 instances on an ECS cluster
    - `aws:ecs:stop-task`: Stop the specified EC2 tasks of an ECS cluster
    - `aws:ecs:task-cpu-stress`: It runs CPU stress via stress-ng tool
    - `aws:ecs:task-io-stress`: It runs IO stress via stress-ng tool
    - `aws:ecs:task-kill-process`: It kills a particular process by name, using the killall command
    - `aws:ecs:task-network-blackhole-port`: It drops incoming or outgoing traffic for a configurable protocol (tcp or udp) and port which is useful for simulating dependency failures
    - `aws:ecs:task-network-latency`: It adds latency, with jitter, to outgoing or incoming traffic from a configurable list of sources (Supported: IPv4, IPv4/CIDR, domain name, DYNAMODB|S3)
    - `aws:ecs:task-network-packet-loss`: It adds packet loss to outgoing or incoming traffic from a configurable list of sources (Supported: IPv4, IPv4/CIDR, domain name, DYNAMODB|S3)

  - **EKS**
    - `aws:eks:inject-kubernetes-custom-resource`: Injects the specified kubernetes custom resource in the target EKS cluster
    - `aws:eks:pod-cpu-stress`: Runs CPU stress on the target pods
    - `aws:eks:pod-delete`: Deletes pods of a given Kubernetes namespace using pod identifying information such as label selectors, deployment names or pod names
    - `aws:eks:pod-io-stress`: Runs IO stress on the target pods
    - `aws:eks:pod-memory-stress`: Runs memory stress on the target pods
    - `aws:eks:pod-network-blackhole-port`: Drops incoming or outgoing traffic for a configurable protocol (tcp or udp) and port which is useful for simulating dependency failures
    - `aws:eks:pod-network-latency`: Adds latency, with jitter, to outgoing or incoming traffic from a configurable list of sources (Supported: IPv4, IPv4/CIDR, domain name, DYNAMODB|S3)
    - `aws:eks:pod-network-packet-loss`: Adds packet loss to outgoing or incoming traffic from a configurable list of sources (Supported: IPv4, IPv4/CIDR, domain name, DYNAMODB|S3)
    - `aws:eks:terminate-nodegroup-instances`: Terminates a percentage of the underlying EC2 instances in an EKS cluster

  - **Elasticache**
    - `aws:elasticache:interrupt-cluster-az-power`: Simulate AZ outage in ElastiCache Clusters

  - **FIS**
    - `aws:fis:inject-api-internal-error`: Cause an AWS service to return internal error responses for specific caller and operations
    - `aws:fis:inject-api-throttle-error`: Cause an AWS service to return throttled responses for specific caller and operations
    - `aws:fis:inject-api-unavailable-error`: Cause an AWS service to return unavailable error responses for specific caller and operations
    - `aws:fis:wait`: Wait for the specified duration. Stop condition monitoring will continue during this time

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
