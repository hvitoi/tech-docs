# aws sqs

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
  --queue-url https://sqs.sa-east-1.amazonaws.com/123456789012/my-queue \
  --max-number-of-messages "10" \
  --visibility-timeout "30" \
  --wait-time-seconds "20" \
  --attribute-names All \
  --message-attribute-names All
```

## delete-message

```shell
aws sqs delete-message \
  --queue-url "https://queue.amazonaws.com/account-id/MyFirstQueue" \
  --receipt-handle "receipt-id"
```

## get-queue-attributes

```shell
# The size of the queue: visible messages (backlog waiting to be consumed) + not visible messages (in-flight - being processed) - you could also add here scheduled for later delivery
aws sqs get-queue-attributes \
  --queue-url https://sqs.sa-east-1.amazonaws.com/0123456789012/mysqs \
  --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible ApproximateNumberOfMessagesDelayed
```
