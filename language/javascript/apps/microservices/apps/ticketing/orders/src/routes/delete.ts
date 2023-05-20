import express, { Request, Response } from 'express';
import { Order, OrderStatus } from '../models/order';
import {
  requireAuth,
  NotFoundError,
  NotAuthorizedError
} from '@hvtickets/common';
import { OrderCancelledPublisher } from '../events/publishers/order-cancelled-publisher';
import { natsWrapper } from '../nats-wrapper';

const router = express.Router();

router.delete(
  '/api/orders/:orderId',
  requireAuth,
  async (req: Request, res: Response) => {
    const { orderId } = req.params;

    // Search the order
    const order = await Order.findById(orderId).populate('ticket');
    if (!order) throw new NotFoundError();

    // If the order doesn't belong to the current user
    if (order.userId !== req.currentUser!.id) throw new NotAuthorizedError();

    // Update the order
    order.status = OrderStatus.Cancelled;
    await order.save();

    // Publish event order:cancelled
    new OrderCancelledPublisher(natsWrapper.client).publish({
      id: order.id,
      version: order.version,
      ticket: {
        id: order.ticket.id
      }
    });

    // Send the cancelled ticket
    res.status(204).send(order);
  }
);

export { router as deleteOrderRouter };
