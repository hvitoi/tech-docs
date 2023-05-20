import { EventSubjects } from './event-subjects';

export interface TicketCreatedEvent {
  // T['subject']
  subject: EventSubjects.TicketCreated;

  // T['data']
  data: {
    id: string;
    version: number;
    title: string;
    price: number;
    userId: string;
  };
}
