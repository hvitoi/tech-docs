# Kafka topics

- Create, delete, describe or change a topic
- Default topic configuration is stored at `config/server.properties`

## List

```shell
# List all the topics in the kafka cluster
kafka-topics.sh --list \
  --bootstrap-server "localhost:9092"
```

## Create

- `replication-factor`
  - 1: no duplicity, only the leader
  - 3: leader + two replicas
  - Each instance goes into a different broker

```shell
# Create topic
kafka-topics.sh --create \
  --bootstrap-server "localhost:9092" \
  --topic "my-topic" \
  --partitions "3" \
  --replication-factor "3"

# Create topic with custom config
kafka-topics.sh --create \
  --bootstrap-server "localhost:9092" \
  --topic "my-topic" \
  --partitions "partitions-number" \
  --replication-factor "replicas-number" \
  --config "cleanup.policy=compact" \
  --config "segment.ms=10000"
```

## Describe

```shell
# Describe a topic
kafka-topics.sh --describe \
  --bootstrap-server "localhost:9092" \
  --topic "my-topic"

# Show under replicated replicas
kafka-topics.sh --describe \
  --bootstrap-server "localhost:9092" \
  --under-replicated-partitions

# List partition at minimum in sync
kafka-topics.sh --describe \
  --bootstrap-server "localhost:9092" \
  --at-min-isr-partitions

# List partition under minimum insync
kafka-topics.sh --describe \
  --bootstrap-server "localhost:9092" \
  --under-min-isr-partitions
```

## Alter

```shell
# Change the number of partitions for a topic
kafka-topics.sh --alter \
  --bootstrap-server "localhost:9092" \
  --topic "my-topic" \
  --partitions "3"
```

## Delete

```shell
# Delete a topic
kafka-topics.sh --delete \
  --bootstrap-server "localhost:9092" \
  --topic "my-topic"
```
