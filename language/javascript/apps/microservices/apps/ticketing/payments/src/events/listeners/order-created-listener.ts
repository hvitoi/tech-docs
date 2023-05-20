import { Message } from 'node-nats-streaming';
import {
  EventListener,
  EventSubjects,
  OrderCreatedEvent
} from '@hvtickets/common';
import { queueGroupName } from './queue-group-name';
import { Order } from '../../models/order';

class OrderCreatedListener extends EventListener<OrderCreatedEvent> {
  readonly subject = EventSubjects.OrderCreated;
  queueGroupName = queueGroupName;

  async onMessage(data: OrderCreatedEvent['data'], msg: Message) {
    // Create an Order
    const order = Order.build({
      id: data.id,
      price: data.ticket.price,
      status: data.status,
      userId: data.userId,
      version: data.version
    });
    await order.save();

    // Ack message
    msg.ack();
  }
}

export { OrderCreatedListener };
