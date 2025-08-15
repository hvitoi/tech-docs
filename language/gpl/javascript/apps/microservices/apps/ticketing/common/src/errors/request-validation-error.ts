import { CustomError } from './custom-error'; // error class
import { ValidationError } from 'express-validator'; // type

export class RequestValidationError extends CustomError {
  statusCode = 400; // 400 Bad Request

  constructor(public errors: ValidationError[]) {
    // ValidationError is an array of errors
    super('Invalid request parameters');
    Object.setPrototypeOf(this, RequestValidationError.prototype);
  }

  serializeErrors() {
    return this.errors.map((err) => {
      return { message: err.msg, field: err.param };
    });
  }
}
