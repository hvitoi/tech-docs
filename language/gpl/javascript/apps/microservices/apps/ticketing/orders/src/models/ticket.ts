// This implementation of the 'ticket' CANNOT be copied from the tickets services
// The requirements are different! A new model must be created
import mongoose from 'mongoose';
import { updateIfCurrentPlugin } from 'mongoose-update-if-current';
import { Order, OrderStatus } from './order';

interface TicketAttrs {
  id: string; // Ticket ID from 'tickets' service
  title: string;
  price: number;
}

interface TicketDoc extends mongoose.Document {
  title: string;
  price: number;
  version: number;
  isReserved(): Promise<boolean>;
}

interface TicketModel extends mongoose.Model<TicketDoc> {
  build(attrs: TicketAttrs): TicketDoc;
  findByEvent(event: {
    id: string;
    version: number;
  }): Promise<TicketDoc | null>;
}

const ticketSchema = new mongoose.Schema(
  {
    title: {
      type: String,
      required: true,
      min: 0
    },
    price: {
      type: Number,
      required: true,
      min: 0
    }
  },

  {
    toJSON: {
      transform(doc, ret) {
        ret.id = ret._id;
        delete ret._id;
      }
    }
  }
);

// Change the default property of __v
ticketSchema.set('versionKey', 'version');
ticketSchema.plugin(updateIfCurrentPlugin); // This plugins blocks saving tickets are out of sync (different versions)

// Model functions
ticketSchema.statics.build = (attrs: TicketAttrs) => {
  return new Ticket({
    _id: attrs.id, // The id must be created as _id otherwise it would not be considered a id in mongodb
    title: attrs.title,
    price: attrs.price
  });
};
ticketSchema.statics.findByEvent = (event: { id: string; version: number }) => {
  // Find by ID and the previous version
  return Ticket.findOne({
    _id: event.id,
    version: event.version - 1
  });
};

// Document functions
ticketSchema.methods.isReserved = async function () {
  const existingOrder = await Order.findOne({
    ticket: this, // THIS is the ticket document
    status: {
      $in: [
        OrderStatus.Created,
        OrderStatus.AwaitingPayment,
        OrderStatus.Complete
        // OrderStatus.Cancelled is allowed!
      ] // $in is a mongoose operator, list out possible values. Same as IN in SQL
    }
  });

  return !!existingOrder; // <value> -> true / <undefined> -> false
};

const Ticket = mongoose.model<TicketDoc, TicketModel>('Ticket', ticketSchema);

export { Ticket, TicketDoc };
