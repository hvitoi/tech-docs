# AWS::ElastiCache::CacheCluster

- Managed `Redis` or `Memcached`
- `In-memory` database
- Ports
  Aurora PostgreSQL: 5432
  Aurora MySQL: 3306

## Authentication

- All caches in ElastiCache `do not support IAM authentication`
- IAM policies are used for api-level security only
- Redis
  - `Redis auth` can be used with a `password/token` to connect to the cache
  - For extra security use security groups
  - Add SSL encryption
- Memcached
  - Support `SASL-based` authentication

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-cachecluster.html>

```yaml
Type: AWS::ElastiCache::CacheCluster
Properties:
  AutoMinorVersionUpgrade: Boolean
  AZMode: String
  CacheNodeType: String
  CacheParameterGroupName: String
  CacheSecurityGroupNames:
    - String
  CacheSubnetGroupName: String
  ClusterName: String
  Engine: String
  EngineVersion: String
  IpDiscovery: String
  LogDeliveryConfigurations:
    - LogDeliveryConfigurationRequest
  NetworkType: String
  NotificationTopicArn: String
  NumCacheNodes: Integer
  Port: Integer
  PreferredAvailabilityZone: String
  PreferredAvailabilityZones:
    - String
  PreferredMaintenanceWindow: String
  SnapshotArns:
    - String
  SnapshotName: String
  SnapshotRetentionLimit: Integer
  SnapshotWindow: String
  Tags:
    - Tag
  TransitEncryptionEnabled: Boolean
  VpcSecurityGroupIds:
    - String
```

### Engine

- `Redis`
  - Multi-AZ with auto-failover
  - Supports read replicas
  - Data durability using AOF
  - Backup and restore features
  - HIPAA compliant
- `Memcached`
  - Multi-node for partioning data (`sharding`)
  - No replication!
  - Non persistent
  - No backup and restore
  - Multi-threaded architecture
