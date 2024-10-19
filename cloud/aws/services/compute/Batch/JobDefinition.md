# AWS::Batch::JobDefinition

- `Multi-node` `parallel jobs` that span `multiple EC2 instances`
- The jobs are managed by the batch service
- You can use the `AWS ParallelCluster`, which in an open source management tool to deploy HPC on AWS

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html>

```yaml
Type: AWS::Batch::JobDefinition
Properties:
  ContainerProperties:
    ContainerProperties
  EcsProperties:
    EcsProperties
  EksProperties:
    EksProperties
  JobDefinitionName: String
  NodeProperties:
    NodeProperties
  Parameters: Json
  PlatformCapabilities:
    - String
  PropagateTags: Boolean
  RetryStrategy:
    RetryStrategy
  SchedulingPriority: Integer
  Tags:
    - Tag
  Timeout:
    Timeout
  Type: String
```
