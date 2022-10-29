# Kafka topics

- Create, delete, describe or change a topic
- Default topic configuration is stored at `config/server.properties`

## List

```sh
# List all the topics in the kafka cluster
kafka-topics.sh --list \
  --bootstrap-server "localhost:9092"
```

## Create

- `replication-factor`
  - 1: no duplicity, only the leader
  - 3: leader + two replicas
  - Each instance goes into a different broker

```sh
# Create topic
kafka-topics.sh --create \
  --bootstrap-server "localhost:9092" \
  --topic "my-topic" \
  --partitions "3" \
  --replication-factor "3" # must be <= the number of brokers

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

```sh
# Describe all topics
kafka-topics.sh --describe \
  --bootstrap-server "localhost:9092"

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

- The replication factor of the topic cannot be defined here (only at topic creation)

```sh
# Change the number of partitions for a topic
kafka-topics.sh --alter \
  --bootstrap-server "localhost:9092" \
  --topic "my-topic" \
  --partitions "3" \
  --replication-factor "2"
```

## Delete

```sh
# Delete a topic
kafka-topics.sh --delete \
  --bootstrap-server "localhost:9092" \
  --topic "my-topic"
```
