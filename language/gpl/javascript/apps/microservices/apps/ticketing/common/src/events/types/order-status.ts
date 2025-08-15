export enum OrderStatus {
  // Order created but ticket not reserved yet
  Created = 'created',

  // User cancelled the order
  /// The ticket is already reserved
  // The order expired
  Cancelled = 'cancelled',

  // Order reserved the ticket
  AwaitingPayment = 'awaiting:payment',

  // Order reserved the ticket and user has paid
  Complete = 'complete'
}
