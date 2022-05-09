import { Message } from 'node-nats-streaming';
import {
  EventListener,
  OrderCreatedEvent,
  EventSubjects
} from '@hvtickets/common';
import { queueGroupName } from './queue-group-name';
import { Ticket } from '../../models/ticket';
import { TicketUpdatedPublisher } from '../publishers/ticket-updated-publisher';

class OrderCreatedListener extends EventListener<OrderCreatedEvent> {
  readonly subject = EventSubjects.OrderCreated;
  queueGroupName = queueGroupName;

  async onMessage(data: OrderCreatedEvent['data'], msg: Message) {
    // Find the ticket from the order
    const ticket = await Ticket.findById(data.ticket.id);

    // If no ticket if found, throw an error (out of order process)
    if (!ticket) throw new Error('Ticket not found');

    // Set ticket as reserved (set the orderId)
    ticket.set({ orderId: data.id });

    // Save the ticket
    await ticket.save();

    // Emit ticket updated event
    await new TicketUpdatedPublisher(this.client).publish({
      id: ticket.id,
      price: ticket.price,
      title: ticket.title,
      userId: ticket.userId,
      orderId: ticket.orderId,
      version: ticket.version
    });

    // Ack the message
    msg.ack();
  }
}

export { OrderCreatedListener };
