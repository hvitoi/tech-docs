import nats from 'node-nats-streaming';
import { randomBytes } from 'crypto';
import { TicketCreatedListener } from './events/ticket-created-listener';

console.clear();

// CONNECT (server, clientID, options)
const stan = nats.connect('ticketing', randomBytes(4).toString('hex'), {
  url: 'http://localhost:4222'
});

// CONNECT CALLBACK
stan.on('connect', () => {
  console.log('Listener connected to NATS');

  new TicketCreatedListener(stan).listen();
});

process.on('SIGINT', () => stan.close()); // Watch for interrupt signals
process.on('SIGTERM', () => stan.close()); // Watch for terminate signals
process.on('SIGUSR2', () => stan.close()); // Nodemon kill signal
