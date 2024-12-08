# AWS::Neptune::DBCluster

- Managed `graph database`
- Use cases for graph databases
  - High relationship data
  - Social networking (users with friends and comments)
  - Knowledge graphs (wikipedia)
- `Multi-AZ`, up to `15 read replicas`

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html>

```yaml
Type: AWS::Neptune::DBCluster
Properties:
  AssociatedRoles:
    - DBClusterRole
  AvailabilityZones:
    - String
  BackupRetentionPeriod: Integer
  CopyTagsToSnapshot: Boolean
  DBClusterIdentifier: String
  DBClusterParameterGroupName: String
  DBInstanceParameterGroupName: String
  DBPort: Integer
  DBSubnetGroupName: String
  DeletionProtection: Boolean
  EnableCloudwatchLogsExports:
    - String
  EngineVersion: String
  IamAuthEnabled: Boolean
  KmsKeyId: String
  Port: String
  PreferredBackupWindow: String
  PreferredMaintenanceWindow: String
  RestoreToTime: String
  RestoreType: String
  ServerlessScalingConfiguration:
    ServerlessScalingConfiguration
  SnapshotIdentifier: String
  SourceDBClusterIdentifier: String
  StorageEncrypted: Boolean
  Tags:
    - Tag
  UseLatestRestorableTime: Boolean
  VpcSecurityGroupIds:
    - String
```
