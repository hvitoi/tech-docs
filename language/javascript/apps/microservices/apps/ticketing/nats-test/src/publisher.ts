import nats from 'node-nats-streaming';
import { TicketCreatedPublisher } from './events/ticket-created-publisher';

console.clear();

// Create a NATS client (stan - nats backwards)
const stan = nats.connect('ticketing', 'abc', {
  url: 'http://localhost:4222'
});

// Callback to 'connect' event
stan.on('connect', async () => {
  console.log('Publisher connected to NATS');

  const publisher = new TicketCreatedPublisher(stan);
  try {
    await publisher.publish({
      id: '123',
      title: 'concert',
      price: 20,
      userId: '24fa'
    });
  } catch (err) {
    console.error(err);
  }
});