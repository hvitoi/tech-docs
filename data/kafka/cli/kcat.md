# kafkacat

## Metadata List

```sh
# Cluster information and topics
kcat \
  -b "localhost:9092"
  -L
```

## Consume

```sh
kcat -C \
  -b "localhost:9092" \
  -t "my-topic"
```
