import express, { Request, Response } from 'express';
import { body } from 'express-validator';
import { requireAuth, validateRequest } from '@hvtickets/common'; // Middlewares
import { natsWrapper } from '../nats-wrapper';
import { TicketCreatedPublisher } from '../events/publishers/ticket-created-publisher'; // Event publisher
import { Ticket } from '../models/ticket';

const router = express.Router();

router.post(
  '/api/tickets',
  requireAuth,
  [
    body('title').not().isEmpty().withMessage('Title is required'),
    body('price').isFloat({ gt: 0 }).withMessage('Price must be greater than 0')
  ],
  validateRequest,
  async (req: Request, res: Response) => {
    const { title, price } = req.body;

    // Build ticket instance
    const ticket = Ticket.build({
      title,
      price,
      userId: req.currentUser!.id // req.currentUser does exist at this point
    });

    // Save to DB
    await ticket.save(); // ticket here already receive the additional properties (e.g., _id, createdAt)

    // Publish the event
    await new TicketCreatedPublisher(natsWrapper.client).publish({
      id: ticket.id,
      version: ticket.version,
      title: ticket.title,
      price: ticket.price,
      userId: ticket.userId
    });

    // Send response
    res.status(201).send(ticket);
  }
);

export { router as createTicketRouter };
