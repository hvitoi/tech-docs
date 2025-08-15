// Packages
import express from 'express';
import bodyParser from 'body-parser';
import cookieSession from 'cookie-session';

// Routes
import './controllers/LoginController';
import './controllers/RootController';
import { AppRouter } from './AppRouter';

// ---

// API configuration
const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cookieSession({ keys: ['anyKey!!'] }));

// Routes
app.use(AppRouter.getInstance());

// Listen
app.listen(3000, () => {
  console.log('Listening on port 3000.');
});
