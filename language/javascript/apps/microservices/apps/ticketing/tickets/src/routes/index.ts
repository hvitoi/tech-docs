import express, { Request, Response } from 'express';
import { Ticket } from '../models/ticket';

const router = express.Router();

router.get('/api/tickets', async (req: Request, res: Response) => {
  const tickets = await Ticket.find({ orderId: undefined }); // Find all the tickets that haven't yet been reserved
  res.send(tickets);
});

export { router as indexTicketRouter };
