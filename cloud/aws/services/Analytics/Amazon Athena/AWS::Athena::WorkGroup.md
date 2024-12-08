# AWS::Athena::WorkGroup

- `Athena` performs `analytics` from a S3 bucket
- A SQL layer on top of S3
- Data queries can be performed using `SQL` or `JDBC`
- Charge per query
- The query results are stored as a database in S3

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html>

```yaml
Type: AWS::Athena::WorkGroup
Properties:
  Description: String
  Name: String
  RecursiveDeleteOption: Boolean
  State: String
  Tags:
    - Tag
  WorkGroupConfiguration:
    WorkGroupConfiguration
```

### WorkGroupConfiguration

- **Athena Database** defines the `query result location` is the s3 bucket to store the databases

```sql
-- Create a datbase in Athena
CREATE DATABASE s3_access_logs_db;

-- Create a new table in db s3_access_log_db
CREATE EXTERNAL TABLE IF NOT EXISTS s3_access_logs_db.mybucket_logs(
  BucketOwner STRING,
  Bucket STRING,
  RequestDateTime STRING,
  RemoteIP STRING,
  Requester STRING,
  RequestID STRING,
  Operation STRING,
  Key STRING,
  RequestURI_operation STRING,
  RequestURI_key STRING,
  RequestURI_httpProtoversion STRING,
  HTTPstatus STRING,
  ErrorCode STRING,
  BytesSent BIGINT,
  ObjectSize BIGINT,
  TotalTime STRING,
  TurnAroundTime STRING,
  Referrer STRING,
  UserAgent STRING,
  VersionId STRING,
  HostId STRING,
  SigV STRING,
  CipherSuite STRING,
  AuthType STRING,
  EndPoint STRING,
  TLSVersion STRING
) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe' WITH SERDEPROPERTIES (
  'serialization.format' = '1',
  'input.regex' = '([^ ]*) ([^ ]*) \\[(.*?)\\] ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) \\\"([^ ]*) ([^ ]*) (- |[^ ]*)\\\" (-|[0-9]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) (\"[^\"]*\") ([^ ]*)(?: ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*))?.*$'
) LOCATION 's3://hvitoi/prefix/'; -- where to query results from
```
