# AWS::Elasticsearch::Domain

- Allows search by any field in a database (normally you can only search by the primary key)
- Elasticsearch is used as a complement for other databases, using it for searching only
- It's a common use for `big data` applications
- Comes with `Kibana` (visualization) and `Logstash` (log ingestion)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html>

```yaml
Type: AWS::Elasticsearch::Domain
Properties:
  AccessPolicies: Json
  AdvancedOptions:
    Key: Value
  AdvancedSecurityOptions:
    AdvancedSecurityOptionsInput
  CognitoOptions:
    CognitoOptions
  DomainEndpointOptions:
    DomainEndpointOptions
  DomainName: String
  EBSOptions:
    EBSOptions
  ElasticsearchClusterConfig:
    ElasticsearchClusterConfig
  ElasticsearchVersion: String
  EncryptionAtRestOptions:
    EncryptionAtRestOptions
  LogPublishingOptions:
    Key: Value
  NodeToNodeEncryptionOptions:
    NodeToNodeEncryptionOptions
  SnapshotOptions:
    SnapshotOptions
  Tags:
    - Tag
  VPCOptions:
    VPCOptions
```
