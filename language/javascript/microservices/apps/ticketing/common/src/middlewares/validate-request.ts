import { Request, Response, NextFunction } from 'express';
import { validationResult } from 'express-validator'; // validator
import { RequestValidationError } from '../errors/request-validation-error'; // error

export const validateRequest = (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  // ValidationError object that contains the array of validation errors!
  const errors = validationResult(req);

  // If validation fails...
  if (!errors.isEmpty()) throw new RequestValidationError(errors.array());

  // Go to next middleware
  next();
};
