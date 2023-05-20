import mongoose from 'mongoose';
import { Message } from 'node-nats-streaming';
import { TicketCreatedEvent } from '@hvtickets/common';
import { TicketCreatedListener } from '../ticket-created-listener';
import { natsWrapper } from '../../../nats-wrapper';
import { Ticket } from '../../../models/ticket';

const setup = async () => {
  // Create an instance of the listener
  const listener = new TicketCreatedListener(natsWrapper.client);

  // Create a fake event data
  const data: TicketCreatedEvent['data'] = {
    version: 0,
    id: mongoose.Types.ObjectId().toHexString(),
    title: 'Concert',
    price: 10,
    userId: mongoose.Types.ObjectId().toHexString()
  };

  // Create a fake event message. ts-ignore to do not implement all the methods and properties of 'Message', just the necessary ones for the test
  // @ts-ignore
  const msg: Message = {
    ack: jest.fn() // Define the ack as a jest mock function so that we can count how many times it was invoked
  };

  return { listener, data, msg };
};

test('Create and save a ticket', async () => {
  // Setup function
  const { listener, data, msg } = await setup();

  // 'Manually' invoke the onMessage function. It fakes a event received
  await listener.onMessage(data, msg);

  // Search for the Ticket created by the onMessage function
  const ticket = await Ticket.findById(data.id);

  // Assertions
  expect(ticket).toBeDefined();
  expect(ticket!.title).toEqual(data.title);
  expect(ticket!.price).toEqual(data.price);
});

test('Ack the message', async () => {
  // Setup function
  const { listener, data, msg } = await setup();

  // 'Manually' invoke the onMessage function. It fakes a event received
  await listener.onMessage(data, msg);

  // Assertions about the ack being invoked
  expect(msg.ack).toHaveBeenCalled();
});
