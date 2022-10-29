# kafka-reassign-partitions

```sh
# Generate
kafka-reassign-partitions.sh \
  --broker-list "0,1,2" \
  --generate
  --topics-to-move-json-file "topics.json"

# Execute
kafka-reassign-partitions.sh \
  --broker-list "0,1,2" \
  --execute
  --reassignment-json-file "reassign.json"

# Verify
kafka-reassign-partitions.sh \
  --broker-list "0,1,2" \
  --verify
  --reassignment-json-file "reassign.json"
```

```json
{
  "version": 1,
  "topics": [
    {
      "topic": "topic-name"
    }
  ]
}
```
