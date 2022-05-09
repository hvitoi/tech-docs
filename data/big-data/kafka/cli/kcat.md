# kafkacat

## Metadata List

```shell
# Cluster information and topics
kcat \
  -b "localhost:9092"
  -L
```

## Consume

```shell
kcat -C \
  -b "localhost:9092" \
  -t "my-topic"
```
