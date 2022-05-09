import mongoose from 'mongoose';
import { Message } from 'node-nats-streaming';
import { OrderCancelledEvent } from '@hvtickets/common';
import { OrderCancelledListener } from '../order-cancelled-listener';
import { natsWrapper } from '../../../nats-wrapper';
import { Ticket } from '../../../models/ticket';

const setup = async () => {
  const listener = new OrderCancelledListener(natsWrapper.client);

  // Create a ticket
  const ticket = Ticket.build({
    title: 'Concert',
    price: 20,
    userId: mongoose.Types.ObjectId().toHexString()
  });

  // Set a orderId for the ticket
  ticket.set({ orderId: mongoose.Types.ObjectId().toHexString() });
  await ticket.save();

  // fake event data
  const data: OrderCancelledEvent['data'] = {
    id: ticket.orderId!,
    version: 0,
    ticket: {
      id: ticket.id
    }
  };

  // fake event message
  // @ts-ignore
  const msg: Message = {
    ack: jest.fn()
  };

  return { listener, ticket, msg, data };
};

test('Updates the ticket, publishes an event, acks the message', async () => {
  const { listener, ticket, msg, data } = await setup();

  // Manually trigger an event
  await listener.onMessage(data, msg);

  // Find the ticket
  const updatedTicket = await Ticket.findById(ticket.id);

  // Assertions
  expect(updatedTicket?.orderId).not.toBeDefined();
  expect(msg.ack).toHaveBeenCalled();
  expect(natsWrapper.client.publish).toHaveBeenCalled();
});
