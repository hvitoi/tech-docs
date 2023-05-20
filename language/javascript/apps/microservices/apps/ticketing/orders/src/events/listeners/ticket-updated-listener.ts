import { Message } from 'node-nats-streaming';
import {
  EventSubjects,
  EventListener,
  TicketUpdatedEvent
} from '@hvtickets/common';
import { Ticket } from '../../models/ticket';
import { queueGroupName } from './queue-group-name';

export class TicketUpdatedListener extends EventListener<TicketUpdatedEvent> {
  readonly subject = EventSubjects.TicketUpdated;
  queueGroupName = queueGroupName;

  async onMessage(data: TicketUpdatedEvent['data'], msg: Message) {
    const { title, price } = data;

    // Find the ticket in the local DB
    const ticket = await Ticket.findByEvent(data); // Find only the ticket with the previous version number. If not found it will not acknowledge
    if (!ticket) throw new Error('Ticket not found');

    // Update the ticket
    ticket.set({ title, price });
    await ticket.save();

    // Acknowledge the message
    msg.ack();
  }
}
