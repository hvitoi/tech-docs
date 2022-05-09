// This middleware takes the user from the cookie, validate it and set as a property in Request object
// This middleware does NOT throw error for unauthenticated users

import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';

// ---
// Interface to describe the user payload
interface UserPayload {
  id: string;
  email: string;
}

// Add a new property for the Request interface in Express
declare global {
  namespace Express {
    interface Request {
      currentUser?: UserPayload;
    }
  }
}

// ---

const currentUser = (req: Request, res: Response, next: NextFunction) => {
  // If there is no session (no authentication)
  // req.session is either null or a CookieSessionObject
  // req.session will only be null if the cookieSession is not setup in the index.ts
  if (!req.session?.jwt) return next();

  // Validate the jwt
  // verify throws an error if the token is not valid
  try {
    const payload = jwt.verify(
      req.session.jwt,
      process.env.JWT_KEY!
    ) as UserPayload;

    // Add the payload to the recently created property (currentUser) in the req object
    req.currentUser = payload;
  } catch (err) {}

  next();
};

export { currentUser };
