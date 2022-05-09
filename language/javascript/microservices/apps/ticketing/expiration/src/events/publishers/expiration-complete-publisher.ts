import {
  EventPublisher,
  EventSubjects,
  ExpirationCompleteEvent
} from '@hvtickets/common';

class ExpirationCompletePublisher extends EventPublisher<
  ExpirationCompleteEvent
> {
  readonly subject = EventSubjects.ExpirationComplete;
}

export { ExpirationCompletePublisher };
