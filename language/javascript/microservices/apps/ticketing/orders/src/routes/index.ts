import express, { Request, Response } from 'express';
import { requireAuth } from '@hvtickets/common';
import { Order } from '../models/order';

const router = express.Router();

router.get('/api/orders', requireAuth, async (req: Request, res: Response) => {
  const orders = await Order.find({
    userId: req.currentUser!.id
  }).populate('ticket'); // populate the ticket in the 'orders' found
  res.send(orders);
});

export { router as indexOrderRouter };
