# kafka-configs

## Describe

```shell
# Describe complete config from all brokers
kafka-configs.sh \
  --bootstrap-server "localhost:9092" \
  --describe \
  --all \
  --entity-type "brokers"

# Describe only custom config from all brokers
kafka-configs.sh \
  --bootstrap-server "localhost:9092" \
  --describe \
  --entity-type "brokers"

# Describe complete config from broker 0
kafka-configs.sh \
  --bootstrap-server "localhost:9092" \
  --describe \
  --all \
  --entity-type "brokers" \
  --entity-name "0"
```

```shell
# Describe all configuration from a topic
kafka-configs.sh \
  --bootstrap-server "localhost:9092" \
  --describe \
  --entity-type "topics" \
  --entity-name "my-topic"
```

## Alter

```shell
# add broker config (clusterwide configs only)
kafka-configs.sh \
  --bootstrap-server "localhost:9092" \
  --alter \
  --entity-type "brokers" \
  --entity-default \ # Update config to all the brokers
  --add-config "compression.type=producer,message.max.bytes=512000"
```

```shell
# add topic config
kafka-configs.sh \
  --bootstrap-server "localhost:9092" \
  --alter \
  --entity-type "topics" \
  --entity-name "my-topic" \
  --add-config "min.insync.replicas=2"

# delete topic config
kafka-configs.sh \
  --bootstrap-server "localhost:9092" \
  --alter \
  --entity-type "topics" \
  --entity-name "my-topic" \
  --delete-config "min.insync.replicas"
```
