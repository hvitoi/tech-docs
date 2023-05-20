# NATS

- NATS is a basic implementation of event sharing
- NATS Streaming Server is built on top of NATS. It's more advanced
- <docs.nats.io>: Plain NATS
- <docs.nats.io/nats-streaming-concepts/intro>: NATS streaming server
- 'nats-streaming' is the official docker image
- NATS is based on the Post/Subscribe model to emit events

## Communication with the NATS Streaming server

- Clients (other services) use a NATS client to communication with the event bus (NATS server)
- THis client is the 'node-nats-streaming' (npm)
- The client is called 'stan'

## Channels/Topics

- This is the means where an `event` will be `published`
- Services can subscribe to `channels`
- The NATS Server has many channels being managed

## Queue groups

- Created inside of a Channel (in the server)
- NATS Server sends the event to only ONE member (service) of that group
- Prevents double processing of an event
- Services don't need to be member of a group, in this case they will always receive the event
- To join a queue group, a second argument is passed to the SUBSCRIBE action

## Subscription options

- Passed as parameter before subscribing to a channel

- .subscriptionOptions(): Subscription Options: Double click to see the type definition file
- .setManualAckMode(true): Activate the 'Acknowledgement' from services receiving the event. If no Ack is received from the service, NATS will send the event to another service in the queue group
- .setDeliverAllAvailable(): Get all events delivered in the past. Send these events to a newly started up service
- .setDurableName(): Keep track of all events that have gone to the subscription (service) or the queue group

## Durable subscription

- Store information about acknowledgement of events by services
- Says which events have been processed or not

## Events - Subjects - Channels

- Event/Subject 'ticket:created'
- Those who want to follow these events, must subscribe to the channel 'ticket:created'

## Standardization of events/subjects

- Placing the data type of the events in a common repository is a good idea
- Alternatives with Cross Language Support
  - JSON Schema
  - Protobuf
  - Apache Avro
