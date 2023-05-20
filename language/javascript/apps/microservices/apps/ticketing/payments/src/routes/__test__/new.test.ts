import mongoose from 'mongoose';
import request from 'supertest';
import { OrderStatus } from '@hvtickets/common';
import { app } from '../../app';
import { Order } from '../../models/order';
import { Payment } from '../../models/payment';
import { stripe } from '../../stripe'; // (only for UNIT TEST)

test('Returns 404 when purchasing inexistent order', async () => {
  await request(app)
    .post('/api/payments')
    .set('Cookie', global.signin())
    .send({
      token: 'ndsakdio',
      orderId: mongoose.Types.ObjectId().toHexString()
    })
    .expect(404);
});

test('Return 401 when purchasing an order that doesnt belong to the user', async () => {
  // Create an order
  const order = Order.build({
    id: mongoose.Types.ObjectId().toHexString(),
    userId: mongoose.Types.ObjectId().toHexString(),
    version: 0,
    price: 20,
    status: OrderStatus.Created
  });
  await order.save();

  // Pay
  await request(app)
    .post('/api/payments')
    .set('Cookie', global.signin()) // Different user
    .send({
      token: 'ndsakdio',
      orderId: order.id
    })
    .expect(401);
});

test('Returns 400 when purchasing a cancelled order', async () => {
  const userId = mongoose.Types.ObjectId().toHexString();

  // Create an order
  const order = Order.build({
    id: mongoose.Types.ObjectId().toHexString(),
    userId: userId,
    version: 0,
    price: 20,
    status: OrderStatus.Cancelled
  });
  await order.save();

  // Pay
  await request(app)
    .post('/api/payments')
    .set('Cookie', global.signin(userId)) // Same user
    .send({
      token: 'ndsakdfdsio',
      orderId: order.id
    })
    .expect(400);
});

test('Returns a 201 with valid inputs', async () => {
  const userId = mongoose.Types.ObjectId().toHexString();
  const price = Math.floor(Math.random() * 100000);

  // Create an order
  const order = Order.build({
    id: mongoose.Types.ObjectId().toHexString(),
    userId,
    version: 0,
    price,
    status: OrderStatus.Created
  });
  await order.save();

  // Pay valid order
  await request(app)
    .post('/api/payments')
    .set('Cookie', global.signin(userId))
    .send({
      token: 'tok_visa',
      orderId: order.id
    })
    .expect(201);

  // Get the options sent to stripe API (only for UNIT TEST)
  const chargeOptions = (stripe.charges.create as jest.Mock).mock.calls[0][0];
  expect(chargeOptions.source).toEqual('tok_visa');
  expect(chargeOptions.amount).toEqual(price * 100);
  expect(chargeOptions.currency).toEqual('usd');

  // Get the result of the stripe mock function
  const chargeResult = await (stripe.charges.create as jest.Mock).mock
    .results[0].value;

  // Fetch from Stripe API the 50 recent charges (only for INTEGRATION TEST)
  // const stripeCharges = await stripe.charges.list({ limit: 50 });
  // const stripeCharge = stripeCharges.data.find((charge) => {
  //   return charge.amount === price * 100;
  // });
  // expect(stripeCharge).toBeDefined();

  // Check if the PaymentDoc was created
  const payment = await Payment.findOne({
    orderId: order.id,
    stripeId: chargeResult.id
  });

  expect(payment).not.toBeNull(); // toBeDefined doesn't work because when not found it returns null, which is a definition
  expect(payment!.orderId).toEqual(order.id);
  expect(payment!.stripeId).toEqual(chargeResult.id);
});
