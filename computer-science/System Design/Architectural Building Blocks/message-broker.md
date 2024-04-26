# Message Broker

- A message/event broker allows `asynchronous` communication
- Useful for:
  - Processing a result in background and free the connection with the client
  - Implement `retry techniques` without having to start the flow from the very beginning
  - `Buffer messages` to absorb sudden traffic spikes by "enqueuing" jobs to be processed and process it when more appropriate
  - `Decouple senders from receivers`, allowing a system to operate partially whenever an incident occurs\
  - Avoid losing `messages`
- It's a `internal building block`, it's (usually) not a good practice to expose it externally

## Publish/Subscribe pattern

- Allows multiple services (or group of) to `subscribe` to `messages/events/channels/topics` independently

## Queue pattern

- Guarantees the messages are processed in order
