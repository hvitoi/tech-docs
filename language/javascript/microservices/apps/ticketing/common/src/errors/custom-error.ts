export abstract class CustomError extends Error {
  abstract statusCode: number;

  constructor(message: string) {
    super(message); // Invoke the constructor of the Error class
    Object.setPrototypeOf(this, CustomError.prototype); // setPrototypeOf must be called when extending a built in class
  }

  // Shape of the errors array
  abstract serializeErrors(): { message: string; field?: string }[];
}
