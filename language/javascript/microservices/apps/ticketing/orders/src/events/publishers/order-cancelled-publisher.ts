import {
  EventSubjects,
  EventPublisher,
  OrderCancelledEvent
} from '@hvtickets/common';

export class OrderCancelledPublisher extends EventPublisher<
  OrderCancelledEvent
> {
  readonly subject = EventSubjects.OrderCancelled;
}
