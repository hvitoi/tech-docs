import Stripe from 'stripe';

// Stripe (secret-key, { options })
const stripe = new Stripe(process.env.STRIPE_KEY!, {
  apiVersion: '2020-03-02'
});

export { stripe };
