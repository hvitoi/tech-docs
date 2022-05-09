import {
  EventListener,
  OrderCreatedEvent,
  EventSubjects
} from '@hvtickets/common';
import { queueGroupName } from './queue-group-name';
import { Message } from 'node-nats-streaming';
import { expirationQueue } from '../../queues/expiration-queue';

class OrderCreatedListener extends EventListener<OrderCreatedEvent> {
  readonly subject = EventSubjects.OrderCreated;
  queueGroupName = queueGroupName;

  async onMessage(data: OrderCreatedEvent['data'], msg: Message) {
    const delay = new Date(data.expiresAt).getTime() - new Date().getTime(); // Difference in time from the expiration and the current time

    // Add a job to the queue add(data, {options})
    await expirationQueue.add(
      { orderId: data.id }, // Job data
      { delay: 60000 } // Process the job after ~15min (60s for testing)
    );

    // Ack the message
    msg.ack();
  }
}
export { OrderCreatedListener };
