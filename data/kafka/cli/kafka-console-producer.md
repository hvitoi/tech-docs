# Kafka Console Producer

```sh
# Produce messages
kafka-console-producer.sh \
  --bootstrap-server "localhost:9092" \
  --topic "topic-name" # Ctrl+C to stop

# Produce messages with key
kafka-console-producer \
  --bootstrap-server "localhost:9092" \
  --topic "topic-name" \
  --property "parse.key=true" \
  --property "key.separator=:" # TestKey:TestValue

# Properties file
kafka-console-producer \
  --bootstrap-server "localhost:9092" \
  --topic "topic-name" \
  --producer.config "/path/to/config.properties"

# Produce from txt file
kafka-console-producer \
  --bootstrap-server "localhost:9092" \
  --topic "topic-name" < ./messages.txt
```
