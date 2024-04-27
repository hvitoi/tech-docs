# Message Broker

- A message/event broker allows `asynchronous` communication
- Useful for:
  - Processing a result in background and free the connection with the client
  - Implement `retry techniques` without having to start the flow from the very beginning
  - `Buffer messages` to absorb sudden traffic spikes by "enqueuing" jobs to be processed and process it when more appropriate
  - `Decouple senders from receivers`, allowing a system to operate partially whenever an incident occurs\
  - Avoid losing `messages`
- It's a `internal building block`, it's (usually) not a good practice to expose it externally
- It's also known as `event bus`

## Publish/Subscribe pattern

- Allows multiple services (or group of) to `subscribe` to `messages/events/channels/topics` independently

## Queue pattern

- Guarantees the messages are processed in order

## Delivery semantics

- Delivery semantics means how many times a message can be delivered to the same consumer in a consumer group

- `Exactly Once`
  - The best option, but the most difficult (in terms of performance)
- `At Least Once`
  - It can be implemented by forcing the consumer to "commit" the message once it's processed (if not committed, the messaged will be consumed again)
  - It's case of duplicate messages being consumed can be overcome by implementing an idempotent consumer
- `At Most Once`
  - The easiest but the one with more drawbacks
  - Consumers do not need to commit the message once processed
  - Applicable but metrics that could potentially be lost

## Implementations

- Open Source
  - **Apache Kafka**
  - **RabbitMQ**
  - **NATS**
- Cloud Based
  - **AWS SQS**: queue
  - **AWS SNS**: pub/sub

  - **GCP Cloud Tasks**: queue
  - **GCP Pub/Sub**: pub/sub

  - **Azure Service Bus**: queue & pub/sub
  - **Azure Event Hub**: for data ingestion
