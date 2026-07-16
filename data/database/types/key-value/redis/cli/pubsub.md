# pubsub

- <https://redis.io/commands#pubsub>

```shell
# Open two terms and have redis-cli open in both.

# Client subscriber
SUBSCRIBE channel_test_1

# Server
PUBLISH channel_test_1 "Hello World"
```
