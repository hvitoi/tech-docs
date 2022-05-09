# Kafka Consumer Groups

```shell
# List all consumer groups
kafka-consumer-groups.sh \
  --bootstrap-server "localhost:9092" \
  --list

# Describe a consumer group
kafka-consumer-groups.sh \
  --bootstrap-server "localhost:9092" \
  --describe \
  --group "group-name"
# It will show if there are active members (consumers) in this group
# Current-Offset: Last message read
# Log-End-Offset: Last message of the partition
# Lag: Difference between both. How many messages it has to read to keep up to date. The sum of the lags is how many messages will be received by a member when it logs in
```

## Reset offsets

```shell
# shift-by
kafka-consumer-groups.sh \
  --bootstrap-server "localhost:9092" \
  --group 'group-name' \
  --reset-offsets \
  --topic 'topic-name' \
  --shift-by '2' \ # E.g., 2 (forward), -2 (backwards)
  --execute

# to-earliest
kafka-consumer-groups.sh \
  --bootstrap-server "localhost:9092" \
  --group "kafkatrain" \
  --reset-offsets \
  --topic "topic-name" \ # Specify the topic (alternatively set --all-topics)
  --to-earliest \ # Current Offset goes to 0 and lag to maximum
  --execute # Apply

# to-current
kafka-consumer-groups.sh \
  --bootstrap-server "localhost:9092" \
  --group "kafkatrain" \
  --reset-offsets \
  --topic "topic-name" \
  --to-current \
  --execute

# to-offset
kafka-consumer-groups.sh \
  --bootstrap-server "localhost:9092" \
  --group "kafkatrain" \
  --reset-offsets \
  --topic "topic-name" \
  --to-offset "123454" \
  --execute

# to-datetime
kafka-consumer-groups.sh \
  --bootstrap-server "localhost:9092" \
  --group "kafkatrain" \
  --reset-offsets \
  --topic "topic-name" \ # all-topics can be set
  --to-datetime "20200302" \
  --execute
```
