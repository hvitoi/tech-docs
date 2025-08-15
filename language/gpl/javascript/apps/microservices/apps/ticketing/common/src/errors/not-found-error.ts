import { CustomError } from './custom-error'; // error class

export class NotFoundError extends CustomError {
  statusCode = 404;
  message = 'Route not found';

  constructor() {
    super('Route not found');
    Object.setPrototypeOf(this, NotFoundError.prototype);
  }

  serializeErrors() {
    return [{ message: this.message }];
  }
}
