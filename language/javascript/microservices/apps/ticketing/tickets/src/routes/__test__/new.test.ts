import request from 'supertest';
import { app } from '../../app';
import { Ticket } from '../../models/ticket';
import { natsWrapper } from '../../nats-wrapper';

test('Has a route handler listening to /api/tickets for POST requests', async () => {
  const response = await request(app).post('/api/tickets').send({}); // response to empty POST
  expect(response.status).not.toEqual(404);
});

test('Receives a 401 when user is not signed in', async () => {
  const response = await request(app).post('/api/tickets').send({});
  expect(response.status).toEqual(401);
});

test('Returns a status other than 401 is the user is signed in', async () => {
  const response = await request(app)
    .post('/api/tickets')
    .set('Cookie', global.signup())
    .send({});
  expect(response.status).not.toEqual(401);
});

test('Returns an error if an invalid title is provided', async () => {
  await request(app)
    .post('/api/tickets')
    .set('Cookie', global.signup())
    .send({
      title: '',
      price: 10
    })
    .expect(400);

  await request(app)
    .post('/api/tickets')
    .set('Cookie', global.signup())
    .send({
      price: 10
    })
    .expect(400);
});

test('Returns an error if an invalid price is provided', async () => {
  await request(app)
    .post('/api/tickets')
    .set('Cookie', global.signup())
    .send({
      title: 'Concert',
      price: -10
    })
    .expect(400);

  await request(app)
    .post('/api/tickets')
    .set('Cookie', global.signup())
    .send({
      title: 'Concert'
    })
    .expect(400);
});

test('Creates a ticket with valid inputs', async () => {
  let tickets = await Ticket.find({}); // Before
  expect(tickets.length).toEqual(0);

  await request(app)
    .post('/api/tickets')
    .set('Cookie', global.signup())
    .send({
      title: 'Concert',
      price: 20
    })
    .expect(201);

  tickets = await Ticket.find({}); // After
  expect(tickets.length).toEqual(1);
});

test('Publishes an event', async () => {
  // Create the ticket
  await request(app)
    .post('/api/tickets')
    .set('Cookie', global.signup())
    .send({
      title: 'Concert',
      price: 20
    })
    .expect(201);

  // Expect the event to be published
  console.log(natsWrapper); // Console log the mocked object with the mock function
  expect(natsWrapper.client.publish).toHaveBeenCalled();
});
