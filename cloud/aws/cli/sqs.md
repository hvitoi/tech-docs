# sqs

## list-queues

```shell
aws sqs list-queues
```

## send-message

```shell
aws sqs send-message \
  --queue-url "https://queue.amazonaws.com/account-id/MyFirstQueue" \
  --message-body "hello-world"
```

## receive-message

```shell
aws sqs receive-message \
  --max-number-of-messages "10" \
  --visibility-timeout "30" \
  --wait-time-seconds "20"
```

## delete-message

```shell
aws sqs delete-message \
  --queue-url "https://queue.amazonaws.com/account-id/MyFirstQueue" \
  --receipt-handle "receipt-id"
```
