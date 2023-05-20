import request from 'supertest';
import mongoose from 'mongoose';
import { app } from '../../app';
import { Order, OrderStatus } from '../../models/order';
import { Ticket } from '../../models/ticket';
import { natsWrapper } from '../../nats-wrapper';

test('Returns error if ticket does not exist', async () => {
  // Generate a UUID
  const ticketId = mongoose.Types.ObjectId();

  // Send request with invalid UUID
  await request(app)
    .post('/api/orders')
    .set('Cookie', global.signup())
    .send({ ticketId })
    .expect(404);
});

test('Returns error if ticket is already reserved', async () => {
  // Create ticket
  const ticket = Ticket.build({
    id: mongoose.Types.ObjectId().toHexString(),
    title: 'concert',
    price: 20
  });
  await ticket.save();

  // Create order
  const order = Order.build({
    ticket,
    userId: 'asdfgh',
    status: OrderStatus.Created,
    expiresAt: new Date()
  });
  await order.save();

  // Attempt the create order with reserved ticket
  await request(app)
    .post('/api/orders')
    .set('Cookie', global.signup())
    .send({ ticketId: ticket.id })
    .expect(400);
});

test('Reserves a ticket', async () => {
  // Create ticket
  const ticket = Ticket.build({
    id: mongoose.Types.ObjectId().toHexString(),
    title: 'concert',
    price: 20
  });
  await ticket.save();

  // Attempt to create order
  await request(app)
    .post('/api/orders')
    .set('Cookie', global.signup())
    .send({ ticketId: ticket.id })
    .expect(201);
});

test('Emits order:created event', async () => {
  // Create ticket
  const ticket = Ticket.build({
    id: mongoose.Types.ObjectId().toHexString(),
    title: 'concert',
    price: 20
  });
  await ticket.save();

  // Attempt to create order
  await request(app)
    .post('/api/orders')
    .set('Cookie', global.signup())
    .send({ ticketId: ticket.id })
    .expect(201);

  // Expect publish to be invoked
  expect(natsWrapper.client.publish).toHaveBeenCalled();
});
