import { EventSubjects } from './event-subjects';

interface ExpirationCompleteEvent {
  subject: EventSubjects.ExpirationComplete;
  data: {
    orderId: string;
  };
}

export { ExpirationCompleteEvent };
