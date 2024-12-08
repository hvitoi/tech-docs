# AWS::Kinesis::Stream

- Creates a `Kinesis stream` that captures and transports `data records` that are emitted from data sources
- Real-time `streaming` model

- Producer can use `Kinesis Agent`, `AWS SDK` or `Kinesis Producer Library (KPL)`

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html>

```yaml
Type: AWS::Kinesis::Stream
Properties:
  Name: String
  RetentionPeriodHours: Integer
  ShardCount: Integer
  StreamEncryption:
    StreamEncryption
  StreamModeDetails:
    StreamModeDetails
  Tags:
    - Tag
```

### RetentionPeriodHours

- Retention between `1 to 365 days`
- Data cannot be deleted before this period

### ShardCount

- Billing is per `shard` provisioned
- The **partition key** within each record tells to which shard the record will go
- Messages with same partition key go to the same shard
- Each shard supports `1MB/s` incoming data and `2MB/s` outgoing data
