import { Subjects } from './subjects';

export interface TicketCreatedEvent {
  // T['subject']
  subject: Subjects.TicketCreated;

  // T['data']
  data: {
    id: string;
    title: string;
    price: number;
  };
}
