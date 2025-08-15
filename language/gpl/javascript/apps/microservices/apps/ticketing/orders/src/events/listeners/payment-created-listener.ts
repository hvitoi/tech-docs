import { Message } from 'node-nats-streaming';
import {
  EventListener,
  EventSubjects,
  PaymentCreatedEvent,
  OrderStatus
} from '@hvtickets/common';
import { queueGroupName } from './queue-group-name';
import { Order } from '../../models/order';

class PaymentCreatedListener extends EventListener<PaymentCreatedEvent> {
  readonly subject = EventSubjects.PaymentCreated;
  queueGroupName = queueGroupName;

  async onMessage(data: PaymentCreatedEvent['data'], msg: Message) {
    // Find the order
    const order = await Order.findById(data.orderId);
    if (!order) throw new Error('Order not found');

    // Update the status of the order
    order.set({ status: OrderStatus.Complete });
    await order.save();

    // Ack the message
    msg.ack();
  }
}
export { PaymentCreatedListener };
