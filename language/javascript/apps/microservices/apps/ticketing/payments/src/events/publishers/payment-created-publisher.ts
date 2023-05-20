import {
  EventPublisher,
  EventSubjects,
  PaymentCreatedEvent
} from '@hvtickets/common';

class PaymentCreatedPublisher extends EventPublisher<PaymentCreatedEvent> {
  readonly subject = EventSubjects.PaymentCreated;
}

export { PaymentCreatedPublisher };
