# AWS::DynamoDB::Table

- Serverless `NoSQL database`
- Multi-AZ
- Integration with IAM for authentication & authorization

- DynamoDB is made of `Tables` (Collection)
- Each table has `Partition Key` and a `Sort Key` (optional). The combination of both is the `Primary Key`
- Each table can have infinite number of `Items` (Document). With maximum size of 400KB
- Each item has `Attributes` (Field)

- **Data types**
  - `Scalar Types`: String, Number, Binary, Boolean, Null
  - `Document Types`: List, Map
  - `Set Types`: String Set, Number Set, Binary Set

```yaml
Type: AWS::DynamoDB::Table
Properties:
  AttributeDefinitions:
    - AttributeDefinition
  BillingMode: String
  ContributorInsightsSpecification: ContributorInsightsSpecification
  GlobalSecondaryIndexes:
    - GlobalSecondaryIndex
  KeySchema:
    - KeySchema
  KinesisStreamSpecification: KinesisStreamSpecification
  LocalSecondaryIndexes:
    - LocalSecondaryIndex
  PointInTimeRecoverySpecification: PointInTimeRecoverySpecification
  ProvisionedThroughput: ProvisionedThroughput
  SSESpecification: SSESpecification
  StreamSpecification: StreamSpecification
  TableName: String
  Tags:
    - Tag
  TimeToLiveSpecification: TimeToLiveSpecification
```

- **Transactions**
  - Write to two tables at the same time or none=
    ![Transactions](../../../images/dynamodb-transactions.png)

## BillingMode

- It's how to control the table's `capacity` (read/write throughput)

  - `Provisioned Mode` (default)
    - Specified beforehand
    - Autoscaling can be configured
    - RCU (read capacity unit)
    - WCU (write capacity unit)
  - `On-Demand Mode`
    - Scales automatically based on the workload
    - More expensive!
    - Useful for very unpredictable workloads

## GlobalSecondaryIndexes

- Two types
  - `Global Secondary Indexes` (GSI)
  - `Local Secondary Indexes` (LSI)
- Allows `query on attributes` other than on the Primary Key

![Indexes](../../../images/dynamodb-indexes.png)

## StreamSpecification

- `DynamoDB Streams` offers an ordered stream of modifications in a table (create, update, delete, ...)
- Streams can be sent to
  - Kinesis Data Streams
  - AWS Lambda
  - Kinesis Client Library applications
- Data retention `up to 24 hours`
- Use cases:
  - React to changes in real-time (e.g., welcome new users)
  - Analytics
  - Insert into derivative tables
  - Insert into elasticsearch
  - Implement cross-region replication

![Streams](../../../images/dynamodb-streams.png)

## TimeToLiveSpecification

- Automatically expire an item using its `timestamp` attribute (`ExpTime`)
