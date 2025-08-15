import mongoose from 'mongoose';
import { Message } from 'node-nats-streaming';
import { TicketUpdatedEvent } from '@hvtickets/common';
import { TicketUpdatedListener } from '../ticket-updated-listener';
import { natsWrapper } from '../../../nats-wrapper';
import { Ticket } from '../../../models/ticket';

const setup = async () => {
  // Create a listener
  const listener = new TicketUpdatedListener(natsWrapper.client);

  // Create and save a ticket
  const ticket = Ticket.build({
    id: mongoose.Types.ObjectId().toHexString(),
    title: 'Concert',
    price: 10
  });
  await ticket.save();

  // Create a fake event data
  const data: TicketUpdatedEvent['data'] = {
    id: ticket.id,
    version: ticket.version + 1, // The 'ticket' model in the 'tickets' service emitted an event with the incremented version
    title: 'Football match',
    price: 50,
    userId: '123'
  };

  // Create a fake event message
  // @ts-ignore
  const msg: Message = {
    ack: jest.fn()
  };

  // Return all
  return { msg, data, ticket, listener };
};

test('Find, update and save a ticket', async () => {
  // Setup function
  const { msg, data, ticket, listener } = await setup();

  // 'Manually' trigger a event received. Trigger the onMEssage function
  await listener.onMessage(data, msg);

  // Find the ticket updated by the event
  const updatedTicked = await Ticket.findById(ticket.id);

  // Assertion about the ticket data
  expect(updatedTicked?.title).toEqual(data.title);
  expect(updatedTicked?.price).toEqual(data.price);
  expect(updatedTicked?.version).toEqual(data.version); // The version in the 'ticket' model in 'orders' service updates the ticket version, not the event
});

test('Ack the message', async () => {
  const { msg, data, ticket, listener } = await setup();

  await listener.onMessage(data, msg);

  expect(msg.ack).toHaveBeenCalled();
});

test('Does not ack if the event is out of order', async () => {
  const { msg, data, listener, ticket } = await setup();

  data.version = 10;
  try {
    // This has to fail!
    await listener.onMessage(data, msg); // should not be acked because it's not version 1
  } catch (err) {}

  expect(msg.ack).not.toHaveBeenCalled();
});
