# Kafka Console Consumer

```sh
# Subscribe to a topic
kafka-console-consumer.sh \
  --bootstrap-server "localhost:9092" \ # When no consumer-group is specified, a random group is created. E.g., console-consumer-58262
  --topic "my-topic" # read only new messages

# From beginning
kafka-console-consumer.sh \
  --bootstrap-server "localhost:9092" \
  --topic "my-topic" \
  --from-beginning # read starting from last committed offset

# Subscribe from a consumer group
kafka-console-consumer.sh \
  --bootstrap-server "localhost:9092" \
  --topic "my-topic" \
  --group "consumer-group" # Usually the name of the application # Only one consumer of the group receives the message

# Consumer with properties
kafka-console-consumer \
  --bootstrap-server "localhost:9092" \
  --topic "my-topic" \
  --property "print.key=true" \
  --property "key.separator=:"

# Consumer with properties from file
kafka-console-consumer \
  --bootstrap-server "localhost:9092" \
  --topic "my-topic"
  --consumer.config "/path/to/config.properties"
```
