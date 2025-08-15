import request from 'supertest';
import { app } from '../../app';
import mongoose from 'mongoose';

test('Returns a 404 if the ticket is not found', async () => {
  const id = new mongoose.Types.ObjectId().toHexString();
  await request(app).get(`/api/tickets/${id}`).send().expect(404); // if this is not satisfied the test function throws immediately
});

test('Returns the ticket if it is found', async () => {
  const title = 'Concert';
  const price = 20;

  // Create a ticket
  const response = await request(app)
    .post('/api/tickets')
    .set('Cookie', global.signup())
    .send({
      title,
      price
    })
    .expect(201);

  // Get the send ticket
  const ticketResponse = await request(app)
    .get(`/api/tickets/${response.body.id}`)
    .send()
    .expect(200);

  expect(ticketResponse.body.title).toEqual(title);
  expect(ticketResponse.body.price).toEqual(price);
});
