# aws logs

## describe-log-groups

```shell
aws logs describe-log-groups
```

## describe-log-streams

- List Log Streams for a specific Log Group
- E.g., `/aws/fis/EXP24BKXHpK7HbGBuXg`, where the id is the experiment-id

```shell
aws logs describe-log-streams \
  --log-group-name <log-group-name>
```

## get-log-events

- Paginated logs receive a `nextForwardToken` and `nextBackwardToken`

```shell
aws logs get-log-events \
  --log-group-name <log-group-name> \
  --log-stream-name <log-stream-name> \ # "/aws/fis/EXPGEqpGoPBNU6JdSr"
  --start-time $(date -d '1 hour ago' +%s) \
  --limit 100 \
  --no-paginate \
  --query 'events[*].message'

aws logs get-log-events \
  --log-group-name "chaos-log-group" \
  --log-stream-name "/aws/fis/EXPGEqpGoPBNU6JdSr" \
  --no-paginate \
  --query 'events[*].message'
```

```json
{
    "events": [
        {
            "timestamp": 1736353453663,
            "message": "{\"id\":\"EXPGEqpGoPBNU6JdSr\",\"log_type\":\"experiment-end\",\"event_timestamp\":\"2025-01-08T16:24:13.663Z\",\"version\":\"2\",\"details\":{\"experiment_end_time\":\"2025-01-08T16:24:13.645Z\",\"experiment_state\":{\"status\":\"completed\",\"reason\":\"Experiment completed.\"}}}",
            "ingestionTime": 1736353457922
        }
    ],
    "nextForwardToken": "f/38721975944727212086772177815645661031833992941095157760/s",
    "nextBackwardToken": "b/38721974264477565103482377124715101774095691139494445056/s"
}
```
