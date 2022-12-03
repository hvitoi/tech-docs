# sqs

```shell
# list queues
aws sqs list-queues --region "us-east-1"

# send message
aws sqs send-message \
  --queue-url "https://queue.amazonaws.com/account-id/MyFirstQueue" \
  --region "us-east-1" \
  --message-body "hello-world"

# receive message
aws sqs receive-message \

  --max-number-of-messages "10" \
  --visibility-timeout "30" \
  --wait-time-seconds "20"

# delete message
aws sqs delete-message \
  --queue-url "https://queue.amazonaws.com/account-id/MyFirstQueue" \
  --region "us-east-1" \
  --receipt-handle "receipt-id"
```
