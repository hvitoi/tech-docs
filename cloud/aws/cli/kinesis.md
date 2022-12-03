# kinesis

```shell
# Produce (returns the ShardId and SequenceNumber)
aws kinesis put-record \
  --stream-name "test" \
  --partition-key "user1" \
  --data "user signup example" \
  --cli-binary-format "raw-in-base64-out" # --cli-binary-format not needed for cli v1

# Describe (show shards)
aws kinesis describe-stream \
  --stream-name "test"

# Get the iterator to consume from
aws kinesis get-shard-iterator \
  --stream-name "test" \
  --shard-id "shardId-000000000000" \
  --shard-iterator-type "TRIM_HORIZON"

# Consume messages from a shard using the iterator
aws kinesis get-records \
  --shard-iterator "shard-iterator-id"
```
