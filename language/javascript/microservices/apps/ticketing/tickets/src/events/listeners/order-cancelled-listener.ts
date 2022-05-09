import { Message } from 'node-nats-streaming';
import {
  EventListener,
  OrderCancelledEvent,
  EventSubjects
} from '@hvtickets/common';
import { queueGroupName } from './queue-group-name';
import { Ticket } from '../../models/ticket';
import { TicketUpdatedPublisher } from '../publishers/ticket-updated-publisher';

class OrderCancelledListener extends EventListener<OrderCancelledEvent> {
  readonly subject = EventSubjects.OrderCancelled;
  queueGroupName = queueGroupName;

  async onMessage(data: OrderCancelledEvent['data'], msg: Message) {
    // Find the ticket from the cancelled order
    const ticket = await Ticket.findById(data.ticket.id);

    // Throw error if no ticket is found
    if (!ticket) throw new Error('Ticket not found');

    // Free the ticket to purchase
    ticket.set({ orderId: undefined });

    // Save ticket to database
    await ticket.save();

    // Emit event ticket:updated
    await new TicketUpdatedPublisher(this.client).publish({
      id: ticket.id,
      orderId: ticket.orderId,
      userId: ticket.userId,
      price: ticket.price,
      title: ticket.title,
      version: ticket.version
    });

    // Ack message
    msg.ack();
  }
}

export { OrderCancelledListener };
