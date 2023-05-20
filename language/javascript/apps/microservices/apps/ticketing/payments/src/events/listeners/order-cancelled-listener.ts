import {
  EventListener,
  EventSubjects,
  OrderCancelledEvent,
  OrderStatus
} from '@hvtickets/common';
import { queueGroupName } from './queue-group-name';
import { Message } from 'node-nats-streaming';
import { Order } from '../../models/order';

class OrderCancelledListener extends EventListener<OrderCancelledEvent> {
  readonly subject = EventSubjects.OrderCancelled;
  queueGroupName = queueGroupName;

  async onMessage(data: OrderCancelledEvent['data'], msg: Message) {
    // Find the order
    const order = await Order.findOne({
      _id: data.id,
      version: data.version - 1
    });
    if (!order) throw new Error('Order not found');

    // Update the order status
    order.set({ status: OrderStatus.Cancelled });
    await order.save();

    // Ack the message
    msg.ack();
  }
}

export { OrderCancelledListener };
