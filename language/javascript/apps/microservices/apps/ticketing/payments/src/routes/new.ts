import express, { Request, Response } from 'express';
import { body } from 'express-validator';
import {
  requireAuth,
  validateRequest,
  BadRequestError,
  NotFoundError,
  NotAuthorizedError,
  OrderStatus
} from '@hvtickets/common';
import { stripe } from '../stripe';
import { Order } from '../models/order';
import { Payment } from '../models/payment';
import { PaymentCreatedPublisher } from '../events/publishers/payment-created-publisher';
import { natsWrapper } from '../nats-wrapper';

const router = express.Router();

router.post(
  '/api/payments',
  requireAuth,
  [
    body('token').not().isEmpty(), // Token for the credit card payment
    body('orderId').not().isEmpty()
  ],
  validateRequest,
  async (req: Request, res: Response) => {
    const { token, orderId } = req.body;

    // Find the order
    const order = await Order.findById(orderId);
    if (!order) throw new NotFoundError();

    // Unauthorized order
    if (order.userId !== req.currentUser!.id) throw new NotAuthorizedError();

    // Cancelled order
    if (order.status === OrderStatus.Cancelled)
      throw new BadRequestError('Cannot pay cancelled order');

    // Make a charge
    const charge = await stripe.charges.create({
      currency: 'usd',
      amount: order.price * 100,
      source: token
    });

    // Create a PaymentDoc
    const payment = Payment.build({
      orderId: order.id,
      stripeId: charge.id // retrieved from the stripe.charges.create function
    });
    await payment.save();

    // Publish payment:created
    await new PaymentCreatedPublisher(natsWrapper.client).publish({
      id: payment.id,
      orderId: payment.orderId,
      stripeId: payment.stripeId
    });

    // Response
    res.status(201).send({ id: payment.id });
  }
);

export { router as createChargeRouter };
