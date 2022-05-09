import { Message, Stan } from 'node-nats-streaming';
import { Subjects } from './subjects';

interface Event {
  subject: Subjects;
  data: any;
}

// The type of the Event (T) must have the items listed in 'Event'
abstract class Listener<T extends Event> {
  abstract subject: T['subject']; // Name of the channel to subscribe
  abstract queueGroupName: string; // Queue group this listener will join
  abstract onMessage(data: T['data'], msg: Message): void; // Function to run when a message is received
  private client: Stan; // Pre-initialized NATS client (the STAN)
  protected ackWait = 5 * 1000; // Number of seconds this listener has to ack a message

  constructor(client: Stan) {
    this.client = client;
  }

  subscriptionOptions() {
    return this.client
      .subscriptionOptions() // Subscription Options: Double click to see the type definition file
      .setManualAckMode(true) // Activate the 'Acknowledgement' from services receiving the event. If no Ack is received from the service, NATS will send the event to another service in the queue group
      .setDeliverAllAvailable() // Send all events to newly started up service
      .setAckWait(this.ackWait)
      .setDurableName(this.queueGroupName); // Use the same queue group name // The durable subscription stores the events that have been successfully processed or missed. setDeliverAllAvailable() is also necessary, because it deliver old events have not been recorded to the durable subscription
  }

  listen() {
    const subscription = this.client.subscribe(
      this.subject, // channel
      this.queueGroupName, // The queue group assures that the durable subscription doesn't get deleted after the client has gone
      this.subscriptionOptions()
    );

    subscription.on('message', (msg: Message) => {
      console.log(`Message received: ${this.subject} / ${this.queueGroupName}`);
      const parsedData = this.parseMessage(msg);
      this.onMessage(parsedData, msg);
    });
  }

  parseMessage(msg: Message) {
    const data = msg.getData();
    return typeof data === 'string'
      ? JSON.parse(data) // string
      : JSON.parse(data.toString('utf8')); // buffer
  }
}

export { Listener };
