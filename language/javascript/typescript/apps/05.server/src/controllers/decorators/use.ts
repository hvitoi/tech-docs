import 'reflect-metadata';
import { MetadataKeys } from './MetadataKeys'; // enum
import { RequestHandler } from 'express'; // type

export function use(middleware: RequestHandler) {
  return function (target: any, key: string, desc: PropertyDescriptor) {
    // Middlewares are stored as an array of middlewares in the metadata!
    const middlewares =
      Reflect.getMetadata(MetadataKeys.middleware, target, key) || [];

    // Assign back the array with the new middleware to the metadata
    Reflect.defineMetadata(
      MetadataKeys.middleware,
      [...middlewares, middleware],
      target,
      key
    );
  };
}
