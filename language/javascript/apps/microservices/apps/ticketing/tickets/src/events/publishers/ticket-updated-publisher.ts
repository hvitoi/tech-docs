import {
  EventPublisher,
  EventSubjects,
  TicketUpdatedEvent
} from '@hvtickets/common';

class TicketUpdatedPublisher extends EventPublisher<TicketUpdatedEvent> {
  readonly subject = EventSubjects.TicketUpdated;
}

export { TicketUpdatedPublisher };
