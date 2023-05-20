import { Stan } from 'node-nats-streaming';
import { EventSubjects } from './event-subjects';

interface Event {
  subject: EventSubjects;
  data: any;
}

abstract class EventPublisher<T extends Event> {
  abstract subject: T['subject'];
  protected client: Stan;

  constructor(client: Stan) {
    this.client = client;
  }

  publish(data: T['data']): Promise<void> {
    return new Promise((resolve, reject) => {
      // Nats can only share strings. Therefore the object must be converted into json
      this.client.publish(this.subject, JSON.stringify(data), (err) => {
        if (err) return reject(err);
        console.log('Event published to subject', this.subject);
        return resolve();
      });
    });
  }
}

export { EventPublisher };
