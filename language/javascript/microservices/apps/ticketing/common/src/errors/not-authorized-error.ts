import { CustomError } from './custom-error';

export class NotAuthorizedError extends CustomError {
  statusCode = 401; // Forbidden from access
  message = 'Not authorized';

  constructor() {
    super('Not authorized');
    Object.setPrototypeOf(this, NotAuthorizedError.prototype);
  }

  serializeErrors() {
    return [{ message: this.message }];
  }
}
