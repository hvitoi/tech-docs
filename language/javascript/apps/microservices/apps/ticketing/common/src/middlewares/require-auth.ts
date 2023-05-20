import { Request, Response, NextFunction } from 'express';
import { NotAuthorizedError } from '../errors/not-authorized-error';

const requireAuth = (req: Request, res: Response, next: NextFunction) => {
  // If there is no Session or the jwt was invalidated...
  if (!req.currentUser) {
    throw new NotAuthorizedError();
  }
  next();
};

export { requireAuth };
