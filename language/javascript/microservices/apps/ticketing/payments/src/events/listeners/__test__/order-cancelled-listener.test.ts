import mongoose from 'mongoose';
import { Message } from 'node-nats-streaming';
import { natsWrapper } from '../../../nats-wrapper';
import { OrderCancelledListener } from '../order-cancelled-listener';
import { OrderCancelledEvent, OrderStatus } from '@hvtickets/common';
import { Order } from '../../../models/order';

const setup = async () => {
  const listener = new OrderCancelledListener(natsWrapper.client);

  // Create an order
  const order = Order.build({
    id: mongoose.Types.ObjectId().toHexString(),
    status: OrderStatus.Created,
    price: 10,
    userId: 'asdf',
    version: 0
  });
  await order.save();

  // Create fake event
  const data: OrderCancelledEvent['data'] = {
    id: order.id,
    version: 1,
    ticket: {
      id: 'asdf'
    }
  };
  // @ts-ignore
  const msg: Message = { ack: jest.fn() };

  return { listener, data, msg, order };
};

test('Update the status of the order', async () => {
  const { listener, data, msg, order } = await setup();

  // Trigger event
  await listener.onMessage(data, msg);

  // Fetch the updated order
  const updatedOrder = await Order.findById(order.id);

  // Assertions
  expect(updatedOrder!.status).toEqual(OrderStatus.Cancelled);
});

test('Ack the message', async () => {
  const { listener, data, msg, order } = await setup();

  // Trigger event
  await listener.onMessage(data, msg);

  // Assertions
  expect(msg.ack).toHaveBeenCalled();
});
