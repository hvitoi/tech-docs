import request from 'supertest';
import { app } from '../../app';
import mongoose from 'mongoose';
import { Ticket } from '../../models/ticket';
import { natsWrapper } from '../../nats-wrapper';

test('Returns a 404 if the ticketid does not exist', async () => {
  const id = new mongoose.Types.ObjectId().toHexString();
  await request(app)
    .put(`/api/tickets/${id}`)
    .set('Cookie', global.signup())
    .send({
      title: 'Concert',
      price: 20
    })
    .expect(404);
});

test('Returns a 401 if user not authenticated', async () => {
  const id = new mongoose.Types.ObjectId().toHexString();
  await request(app)
    .put(`/api/tickets/${id}`)
    .send({
      title: 'Concert',
      price: 20
    })
    .expect(401);
});

test('Returns a 401 if user does not own the ticket', async () => {
  // Create a ticket
  const response = await request(app)
    .post('/api/tickets')
    .set('Cookie', global.signup())
    .send({
      title: 'Concert',
      price: 10
    });

  // Try to edit it
  await request(app)
    .put(`/api/tickets/${response.body.id}`)
    .set('Cookie', global.signup()) // Totally different user
    .send({
      title: 'Concert',
      price: 20
    })
    .expect(401);
});

test('Returns a 400 if user provides an invalid title or price', async () => {
  const cookie = global.signup();

  // Create a ticket
  const response = await request(app)
    .post('/api/tickets')
    .set('Cookie', cookie)
    .send({
      title: 'Concert',
      price: 10
    });

  // Edit it
  await request(app)
    .put(`/api/tickets/${response.body.id}`)
    .set('Cookie', cookie)
    .send({
      title: '',
      price: 50
    })
    .expect(400);

  // Edit it
  await request(app)
    .put(`/api/tickets/${response.body.id}`)
    .set('Cookie', cookie)
    .send({
      title: 'foo',
      price: -10
    })
    .expect(400);
});

test('Updates the ticket provided valid inputs', async () => {
  const cookie = global.signup();

  // Create a ticket
  const response = await request(app)
    .post('/api/tickets')
    .set('Cookie', cookie)
    .send({
      title: 'Concert',
      price: 10
    });

  // Edit it
  await request(app)
    .put(`/api/tickets/${response.body.id}`)
    .set('Cookie', cookie)
    .send({
      title: 'foo',
      price: 100
    })
    .expect(200);

  // Consult it
  const ticketResponse = await request(app)
    .get(`/api/tickets/${response.body.id}`)
    .send();

  // Expect
  expect(ticketResponse.body.title).toEqual('foo');
  expect(ticketResponse.body.price).toEqual(100);
});

test('Publishes an event', async () => {
  const cookie = global.signup();

  // Create a ticket
  const response = await request(app)
    .post('/api/tickets')
    .set('Cookie', cookie)
    .send({
      title: 'Concert',
      price: 10
    });

  // Edit it
  await request(app)
    .put(`/api/tickets/${response.body.id}`)
    .set('Cookie', cookie)
    .send({
      title: 'foo',
      price: 100
    })
    .expect(200);

  // Expect the event to be published
  expect(natsWrapper.client.publish).toHaveBeenCalled();
});

test('Reject update if ticket is reserved', async () => {
  const cookie = global.signup();

  // Create a ticket
  const response = await request(app)
    .post('/api/tickets')
    .set('Cookie', cookie)
    .send({
      title: 'Concert',
      price: 10
    });

  // Set the ticket as reserved
  const ticket = await Ticket.findById(response.body.id);
  ticket!.set({ orderId: mongoose.Types.ObjectId().toHexString() });
  await ticket!.save();

  // Edit it
  await request(app)
    .put(`/api/tickets/${response.body.id}`)
    .set('Cookie', cookie)
    .send({
      title: 'foo',
      price: 100
    })
    .expect(400);
});
