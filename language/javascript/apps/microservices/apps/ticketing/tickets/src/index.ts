import mongoose from 'mongoose';
import { natsWrapper } from './nats-wrapper';
import { app } from './app';
import { OrderCancelledListener } from './events/listeners/order-cancelled-listener';
import { OrderCreatedListener } from './events/listeners/order-created-listener';

// A start script is made because some versions of node do not support 'await' syntax on the top level
const start = async () => {
  // Check the existence of environment variables
  if (!process.env.JWT_KEY) throw new Error('JWT_KEY must be defined');
  if (!process.env.MONGO_URI) throw new Error('MONGO_URI must be defined');
  if (!process.env.NATS_URL) throw new Error('NATS_URL must be defined');
  if (!process.env.NATS_CLUSTER_ID)
    throw new Error('NATS_CLUSTER_ID must be defined');
  if (!process.env.NATS_CLIENT_ID)
    throw new Error('NATS_CLIENT_ID must be defined');

  try {
    // Connect to NATS
    await natsWrapper.connect(
      process.env.NATS_CLUSTER_ID,
      process.env.NATS_CLIENT_ID,
      process.env.NATS_URL
    );

    natsWrapper.client.on('close', () => {
      console.log('NATS connection closed');
      process.exit();
    });

    process.on('SIGINT', () => natsWrapper.client.close()); // Watch for interrupt signals
    process.on('SIGTERM', () => natsWrapper.client.close()); // Watch for terminate signals
    process.on('SIGUSR2', () => natsWrapper.client.close()); // Nodemon kill signal

    // Listen to events
    new OrderCancelledListener(natsWrapper.client).listen();
    new OrderCreatedListener(natsWrapper.client).listen();

    // Connect to MongoDB
    mongoose.set('useNewUrlParser', true);
    mongoose.set('useUnifiedTopology', true);
    mongoose.set('useCreateIndex', true);
    await mongoose.connect(process.env.MONGO_URI);
    console.log('Tickets Service MongoDB is running.');

    // Start express
    app.listen(3000, () => {
      console.log('Tickets Service is running.');
    });
  } catch (err) {
    console.error(err);
  }
};

// Start app
start();
