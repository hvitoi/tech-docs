import {
  EventPublisher,
  OrderCreatedEvent,
  EventSubjects
} from '@hvtickets/common';

export class OrderCreatedPublisher extends EventPublisher<OrderCreatedEvent> {
  readonly subject = EventSubjects.OrderCreated;
}
