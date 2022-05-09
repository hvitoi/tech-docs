import { Request, Response, NextFunction } from 'express';
import { CustomError } from '../errors/custom-error'; // error class

// This function is called whenever a new Error() is invoked!
// Any RequestHandler with 4 parameters is an error handler

const errorHandler = (
  err: Error,
  req: Request,
  res: Response,
  next: NextFunction
) => {
  // Custom error
  if (err instanceof CustomError) {
    return res.status(err.statusCode).send({ errors: err.serializeErrors() });
  }

  // Generic error
  console.log(err);
  return res
    .status(400)
    .send({ errors: [{ message: 'Something went wrong' }] });
};

export { errorHandler };
