# AWS::EMR::Cluster

- Helps creating `Hadoop Clusters` to analyze and process big data
- Hadoop clusters can be made of many `EC2 instances`
- Also supports `Spark`, `HBase`, `Presto`, `Flink`

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-cluster.html>

```yaml
Type: AWS::EMR::Cluster
Properties:
  AdditionalInfo: Json
  Applications:
    - Application
  AutoScalingRole: String
  AutoTerminationPolicy:
    AutoTerminationPolicy
  BootstrapActions:
    - BootstrapActionConfig
  Configurations:
    - Configuration
  CustomAmiId: String
  EbsRootVolumeIops: Integer
  EbsRootVolumeSize: Integer
  EbsRootVolumeThroughput: Integer
  Instances:
    JobFlowInstancesConfig
  JobFlowRole: String
  KerberosAttributes:
    KerberosAttributes
  LogEncryptionKmsKeyId: String
  LogUri: String
  ManagedScalingPolicy:
    ManagedScalingPolicy
  Name: String
  OSReleaseLabel: String
  PlacementGroupConfigs:
    - PlacementGroupConfig
  ReleaseLabel: String
  ScaleDownBehavior: String
  SecurityConfiguration: String
  ServiceRole: String
  StepConcurrencyLevel: Integer
  Steps:
    - StepConfig
  Tags:
    - Tag
  VisibleToAllUsers: Boolean
```
