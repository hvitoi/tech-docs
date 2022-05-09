import { Message } from 'node-nats-streaming';
import {
  EventListener,
  EventSubjects,
  ExpirationCompleteEvent,
  OrderStatus
} from '@hvtickets/common';
import { OrderCancelledPublisher } from '../publishers/order-cancelled-publisher';
import { queueGroupName } from './queue-group-name';
import { Order } from '../../models/order';

class ExpirationCompleteListener extends EventListener<
  ExpirationCompleteEvent
> {
  readonly subject = EventSubjects.ExpirationComplete;
  queueGroupName = queueGroupName;

  async onMessage(data: ExpirationCompleteEvent['data'], msg: Message) {
    // Find the Order
    const order = await Order.findById(data.orderId).populate('ticket');
    if (!order) throw new Error('Order not found');

    // Return early if the order is complete
    if (order.status === OrderStatus.Complete) return msg.ack();

    // Update the order status
    order.set({ status: OrderStatus.Cancelled });
    await order.save();

    // Publish event
    await new OrderCancelledPublisher(this.client).publish({
      id: order.id,
      version: order.version,
      ticket: {
        id: order.ticket.id
      }
    });

    // Ack the message
    msg.ack();
  }
}

export { ExpirationCompleteListener };
