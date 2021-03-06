# Properties

- The server has 3 types of properties

  - `read-only`: inside server.properties (requires broker restart)
  - `per-broker`: inside server.properties (may be updated dynamically)
  - `cluster-wide`: inside zookeeper, common config for all brokers (may be updated on-the-fly)

## Broker configs

- Broker configuration is stored at _config/server.properties_

- **Topics**
  - `auto.create.topics.enable`: create topic when producing to it and it doesn't exist
  - `delete.topic.enable`: allow topics to be deleted
  - `replication.factor`: replication factor for automatically created topics
  - `offset.retention.minutes`: time after which an offset will be deleted
  - `allow.everyone.if.no.acl.found`: .... Good value: ?
- **Logs**
  - `message.max.bytes`: topic default. Good value: "512000"
  - `message.bytes.ms`: topic default
- **Transactions**
  - `transactional.id.expiration.ms`. Good value: "720000"
  - `unclear.leader.election`: process of leader election. If true, any partition can be elected as a leader (even those with low watermark). It's a topic config. Good value: "false"

## Topic configs

- Topic configuration is defined upon creation
- If no configuration is passed, kafka uses the deafult topic configuration stored at _config/server.properties_

- **General**
  - `cleanup.policy`
    - delete (default): delete old messages based on time or size
    - compact: compact old messages (by key) based on time or size. When compact policy is used, the events must have partition key, otherwise it's rejected
  - `compression.type`: compression format. Default: "producer" (compression defined by the producer)
- **Logs**
  - `retention.bytes`: Delete or compact old logs after X bytes in partition is reached. Maximum size of a partition
  - `retention.ms`: Delete or compact old logs after X milliseconds in partition is reached. Only if the segment is closed
  - `min.cleanable.dirty.ratio`: how frequent to compact the log (if log.compactation is enabled). 0,...1: 0 to 100% if log is duplicated
  - `min.compactation.lag.ms`: minimum time to compact the log
  - `delete.retention.ms`: Delete message after x milliseconds. Even is cleanup.policy=compact
- **Flush**
  - `flush.messages`: flushing is not recommended! use replication instead
    - 1: flush every message to disk before acking it. Slow!
    - 5: fsync after 5 messages
  - `flush.ms`: flushing is not recommended! use replication instead
    - 1000: flush to disk after 1 second
- **Message**
  - `message.timestamp.type`
    - CreateTime: Timestamp created by the producer
    - LogAppendTime: Timestamp created by the server
  - `max.message.bytes`: largest record batch size allowed by kafka. This is also the limit size of a message. Default to 1 MB
  - `segment.bytes`: Size of the segment, which is a subdivision of the partition. Segment is like a file which is append only and remains open until it reaches size limit
  - `segment.ms`: Each X milliseconds, the segment is closed and a new is created
- **Consistency**
  - `min.insync.replicas`: minimum replicas in sync before acking (only for the case ack=all)
    - 1: the leader received the message
    - 2: the leader + one replica received the message
    - replication.factor=3,min.insync=2,acks=all then only 1 broker can go down, otherwise the producer will receive an exception (NotEnoughReplicasException)

## Producer configs

- Producer properties is placed at _config/producer.properties_

- **General**
  - `partitioner.class`: class to decide to which partitioner to send the message. E.g., round robin
- **Compression**
  - `compression.type`: way to compress the message. Producer compression is highly recommended
    - none
    - gzip: best but slow
    - snappy: good
    - lz4: good
    - zstd
- **Retry**
  - `delivery.timeout.ms`: upper bound time to retrying (default 2min)
  - `retry.backoff.ms`: time to wait before attempting to retry a failed request to a given topic. Avoids repeatedly sending requests in a tight loop under failure scenarios
- **Batches**
  - `batch.size`: max size of a batch of messages to be sent at once. It's the compressed size! It can be exceeded to send a single message that is bigger than the batch size. The hard limit is the max.message.bytes defined in the topic. Defaults to 16 KB (32 or 64 is also good - increases throughput)
  - `linger.ms`: Extend the time to send a batch to kafka so that the batch does not contain very few messages. The linger is the time to wait to collect more messages and avoid sending batches with a single message Good between 5 and 20 ms
- **Buffer**
  - `buffer.memory`: total bytes the producer can use to buffer records to be sent to the server (when producer produces faster than the broker can take). Defaults to 32 MB. If this memory is reached, the .send() will hang.
  - `max.block.ms`: max time to block (hang) the .send() before throwing an exception. Defaults to 1min
- **Security**
  - `security.protocol`
    - plaintext
    - ssl
    - sasl_plaintext
    - sasl_ssl: encrypted (tls) + sasl
- **Transactions**
  - Transaction guarantees no duplicity of a batch (all or none)
  - `transactional.id`: guarantee that transactions using the same transactional.id have been completed prior to starting any new transaction. Each instance has its own transactional id!
  - `transaction.timeout.ms`: max time to wait for a transaction status update from the producer before aborting it

## Consumer configs

- Consumer configuration is placed at _config/consumer.properties_

- **General**

  - `allow.auto.create.topics`: try to create topic if trying to consuming from a inexistent topic. auto.create.topics.enable must be set true the server

- **Security**
  - `security.protocol`
- **Pooling**

  - `fetch.min.bytes`: minimum size of the batch to be consumed. Less than that consumer waits. Defaults to 1
  - `fetch.max.bytes`: maximum size of the batch to be consumed (covers multiple partitions). Defaults to 50MB

  - `max.partitions.fetch.bytes`: maximum data to receive per partition (broker). If you have 100 partitions, you will need a lot of RAM

- **Quota**
  - `Limit the bandwidth` for producer and consumers per clientid or consumer group
    - quota.consumer.default
    - quota.producer.default
