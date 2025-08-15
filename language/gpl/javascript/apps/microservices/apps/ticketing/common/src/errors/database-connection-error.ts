import { CustomError } from './custom-error'; // error class

export class DatabaseConnectionError extends CustomError {
  statusCode = 400; // 500 Internal Server Error
  message = 'Error connecting to database';

  constructor() {
    super('Error connecting to database');
    Object.setPrototypeOf(this, DatabaseConnectionError.prototype);
  }

  serializeErrors() {
    return [{ message: this.message }];
  }
}
