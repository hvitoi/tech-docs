# Kafka Consumer Groups

## List

- List all consumer groups

```shell
kafka-consumer-groups.sh --list \
  --bootstrap-server "localhost:9092"
```

## Describe

- Describes a `consumer group`
- It will show if there are active members (consumers) in this group
- Status
  - `Current-Offset`: Last message read and committed
  - `Log-End-Offset`: Last message of the partition
  - `Lag`: Difference between both. How many messages it has to read to keep up to date. The sum of the lags is how many messages will be received by a member when it logs in

```shell
# describe all groups
kafka-consumer-groups.sh --describe \
  --bootstrap-server "localhost:9092" \
  --all-groups

# describe a specific group
kafka-consumer-groups.sh --describe \
  --bootstrap-server "localhost:9092" \
  --group "my-group"
```

## Execute

- Reset offsets for a consumer group

```shell
# shift-by
kafka-consumer-groups.sh --execute \
  --bootstrap-server "localhost:9092" \
  --group "my-group" \
  --reset-offsets \
  --topic "my-topic" \
  --shift-by "2"  # E.g., 2 (forward), -2 (backwards)


# to-earliest
kafka-consumer-groups.sh --execute \
  --bootstrap-server "localhost:9092" \
  --group "my-group" \
  --reset-offsets \
  --topic "my-topic" \ # Specify the topic (alternatively set --all-topics)
  --to-earliest \ # Current Offset goes to 0 and lag to maximum

# to-current
kafka-consumer-groups.sh --execute \
  --bootstrap-server "localhost:9092" \
  --group "my-group" \
  --reset-offsets \
  --topic "my-topic" \
  --to-current

# to-offset
kafka-consumer-groups.sh --execute \
  --bootstrap-server "localhost:9092" \
  --group "my-group" \
  --reset-offsets \
  --topic "my-topic" \
  --to-offset "123"

# to-datetime
kafka-consumer-groups.sh --execute \
  --bootstrap-server "localhost:9092" \
  --group "my-group" \
  --reset-offsets \
  --topic "my-topic" \ # all-topics can be set
  --to-datetime "20200302"
```
