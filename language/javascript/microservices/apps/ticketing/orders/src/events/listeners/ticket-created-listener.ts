import { Message } from 'node-nats-streaming';
import {
  EventSubjects,
  EventListener,
  TicketCreatedEvent
} from '@hvtickets/common';
import { Ticket } from '../../models/ticket';
import { queueGroupName } from './queue-group-name';

export class TicketCreatedListener extends EventListener<TicketCreatedEvent> {
  readonly subject = EventSubjects.TicketCreated;
  queueGroupName = queueGroupName;

  async onMessage(data: TicketCreatedEvent['data'], msg: Message) {
    const { id, title, price } = data;
    const ticket = Ticket.build({
      id, // Saves the same ID from the 'tickets' service
      title,
      price
    });
    await ticket.save();

    msg.ack(); // Acknowledge the message
  }
}
