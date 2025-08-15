import mongoose from 'mongoose';
import { Message } from 'node-nats-streaming';
import { OrderStatus, ExpirationCompleteEvent } from '@hvtickets/common';
import { ExpirationCompleteListener } from '../expiration-complete-listener';
import { natsWrapper } from '../../../nats-wrapper';
import { Order } from '../../../models/order';
import { Ticket } from '../../../models/ticket';

const setup = async () => {
  // Create listener
  const listener = new ExpirationCompleteListener(natsWrapper.client);

  // Create Ticket
  const ticket = Ticket.build({
    id: mongoose.Types.ObjectId().toHexString(),
    title: 'Concert',
    price: 20
  });
  await ticket.save();

  // Create Order
  const order = Order.build({
    status: OrderStatus.Created,
    userId: mongoose.Types.ObjectId().toHexString(),
    expiresAt: new Date(),
    ticket
  });
  await order.save();

  // Fake event
  const data: ExpirationCompleteEvent['data'] = {
    orderId: order.id
  };
  // @ts-ignore
  const msg: Message = { ack: jest.fn() };

  return { listener, ticket, order, data, msg };
};

test('Update the order status to cancelled', async () => {
  const { listener, ticket, order, data, msg } = await setup();

  // Trigger event
  await listener.onMessage(data, msg);

  // Find order
  const updatedOrder = await Order.findById(order.id);

  // Assertions
  expect(updatedOrder!.status).toEqual(OrderStatus.Cancelled);
});

test('Emit order:cancelled event', async () => {
  const { listener, order, ticket, data, msg } = await setup();

  // Trigger event
  await listener.onMessage(data, msg);

  // Take the event data published
  const eventData = JSON.parse(
    (natsWrapper.client.publish as jest.Mock).mock.calls[0][1]
  );

  // Assertions
  expect(natsWrapper.client.publish).toHaveBeenCalled();
  expect(eventData.id).toEqual(order.id);
});

test('Ack the message', async () => {
  const { listener, order, ticket, data, msg } = await setup();

  // Trigger event
  await listener.onMessage(data, msg);

  // Assertions
  expect(msg.ack).toHaveBeenCalled();
});
