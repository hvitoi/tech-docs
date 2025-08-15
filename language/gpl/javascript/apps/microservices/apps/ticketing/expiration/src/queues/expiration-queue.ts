// 1. order:created event is received
// 2. Bull creates a job
// 3. Job is sent to Redis server
// 4. Job is received back to bull after 15 min
// 5. expiration:complete event is emitted

import Queue from 'bull';
import { ExpirationCompletePublisher } from '../events/publishers/expiration-complete-publisher';
import { natsWrapper } from '../nats-wrapper';

// Payload of the Job (message)
interface Payload {
  orderId: string;
}

// A queue is A list of jobs to be processed!
// Queue('channel-name', { options })<job-data-interface>
const expirationQueue = new Queue<Payload>('order:expiration', {
  redis: {
    host: process.env.REDIS_HOST
  }
});

// Callback to be invoked when the job is processed
expirationQueue.process(async (job) => {
  new ExpirationCompletePublisher(natsWrapper.client).publish({
    orderId: job.data.orderId
  });
});

export { expirationQueue };
