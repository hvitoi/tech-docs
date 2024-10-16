# kinesis

## put-record

```shell
# Produce (returns the ShardId and SequenceNumber)
aws kinesis put-record \
  --stream-name "test" \
  --partition-key "user1" \
  --data "user signup example" \
  --cli-binary-format "raw-in-base64-out" # --cli-binary-format not needed for cli v1
```

## describe-stream

```shell
# Describe (show shards)
aws kinesis describe-stream \
  --stream-name "test"
```

## get-shard-iterator

```shell
# Get the iterator to consume from
aws kinesis get-shard-iterator \
  --stream-name "test" \
  --shard-id "shardId-000000000000" \
  --shard-iterator-type "TRIM_HORIZON"
```

## get-records

```shell
# Consume messages from a shard using the iterator
aws kinesis get-records \
  --shard-iterator "shard-iterator-id"
```
