import {
  EventPublisher,
  TicketCreatedEvent,
  EventSubjects
} from '@hvtickets/common';

class TicketCreatedPublisher extends EventPublisher<TicketCreatedEvent> {
  readonly subject = EventSubjects.TicketCreated;
}

export { TicketCreatedPublisher };
