import {
  EventPublisher,
  EventSubjects,
  TicketCreatedEvent
} from '@hvtickets/common';

class TicketCreatedPublisher extends EventPublisher<TicketCreatedEvent> {
  readonly subject = EventSubjects.TicketCreated;
}

export { TicketCreatedPublisher };
