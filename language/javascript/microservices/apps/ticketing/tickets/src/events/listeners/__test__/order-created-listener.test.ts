import mongoose from 'mongoose';
import { Message } from 'node-nats-streaming';
import { OrderCreatedEvent, OrderStatus } from '@hvtickets/common';
import { OrderCreatedListener } from '../order-created-listener';
import { natsWrapper } from '../../../nats-wrapper';
import { Ticket } from '../../../models/ticket';

const setup = async () => {
  // Create an instance of the listener
  const listener = new OrderCreatedListener(natsWrapper.client);

  // Create and save a ticket
  const ticket = Ticket.build({
    title: 'Concert',
    price: 99,
    userId: mongoose.Types.ObjectId().toHexString() // Who created the ticket
  });
  await ticket.save();

  // Create fake event data
  const data: OrderCreatedEvent['data'] = {
    id: mongoose.Types.ObjectId().toHexString(),
    version: 0,
    status: OrderStatus.Created,
    userId: '',
    expiresAt: '',
    ticket: {
      id: ticket.id,
      price: ticket.price
    }
  };

  // Create fake event message
  // @ts-ignore
  const msg: Message = {
    ack: jest.fn()
  };

  return { listener, ticket, data, msg };
};

test('Sets the orderId of the ticket', async () => {
  const { listener, ticket, data, msg } = await setup();

  // Manually trigger the event listener
  await listener.onMessage(data, msg);

  // Get the ticket
  const updatedTicket = await Ticket.findById(ticket.id);

  // Assertion about the existence of the orderId in the ticket
  expect(updatedTicket!.orderId).toEqual(data.id);
});

test('Acks the message', async () => {
  const { listener, ticket, data, msg } = await setup();
  await listener.onMessage(data, msg);
  expect(msg.ack).toHaveBeenCalled();
});

test('Publishes a ticket updated ticket', async () => {
  const { listener, ticket, data, msg } = await setup();
  await listener.onMessage(data, msg);
  expect(natsWrapper.client.publish).toHaveBeenCalled();

  // @ts-ignore
  console.log(natsWrapper.client.publish.mock.calls); // Optional: show the arguments provided to the mock function

  const ticketUpdateData = JSON.parse(
    (natsWrapper.client.publish as jest.Mock).mock.calls[0][1]
  ); // Tells TS that publish is a mock function
  expect(ticketUpdateData.orderId).toEqual(data.id);
});
