import express from 'express';
import 'express-async-errors'; // Allow throwing new Error() inside of async functions. Async functions do not return anything, instead they return a promise that resolve some value in the future. Async routes rely on the next() function. This package prevents this default behavior next(new Error())
import cookieSession from 'cookie-session';
import { errorHandler, currentUser, NotFoundError } from '@hvtickets/common'; // Middlewares & Errors

// Router
import { indexOrderRouter } from './routes/index';
import { showOrderRouter } from './routes/show';
import { newOrderRouter } from './routes/new';
import { deleteOrderRouter } from './routes/delete';

// ---

// API configuration
const app = express();
app.set('trust proxy', true); // Trust traffic coming from a proxy (nginx)
app.use(express.json()); // bodyParser middleware
app.use(
  cookieSession({
    signed: false, // Disable encryption
    //secure: process.env.NODE_ENV !== 'test' // true if on 'start', false if on 'test'
    // Cookie only will be used over https if true
    secure: false
  })
);

// Middleware to extract the user from the cookie
app.use(currentUser);

// Routes
app.use(indexOrderRouter);
app.use(showOrderRouter);
app.use(newOrderRouter);
app.use(deleteOrderRouter);
app.all('*', () => {
  throw new NotFoundError();
});

// Middlewares for error handling
app.use(errorHandler);

// Export app
export { app };
