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
