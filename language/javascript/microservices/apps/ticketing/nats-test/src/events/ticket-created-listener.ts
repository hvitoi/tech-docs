import { Message } from 'node-nats-streaming';
import {
  EventListener,
  EventSubjects,
  TicketCreatedEvent
} from '@hvtickets/common';

class TicketCreatedListener extends EventListener<TicketCreatedEvent> {
  readonly subject = EventSubjects.TicketCreated; // readonly assures that the subject will not be modified
  queueGroupName = 'payments-service';

  onMessage(data: TicketCreatedEvent['data'], msg: Message) {
    console.log('Event data!', data);

    console.log(data.id);
    console.log(data.title);
    console.log(data.price);

    msg.ack(); // Ack if everything goes successfully
  }
}

export { TicketCreatedListener };
