import 'reflect-metadata';
import { AppRouter } from '../../AppRouter'; // router singleton
import { Methods } from './Methods'; // enum
import { MetadataKeys } from './MetadataKeys'; // enum

// The controller check all the metadata of the class
// The metadata is used to create a route in the Router()

export function controller(routePrefix: string) {
  return function (target: Function) {
    // Get the router
    const router = AppRouter.getInstance();

    // Loop through all the methods in the prototype
    for (let key in target.prototype) {
      // Get handler
      const routeHandler = target.prototype[key];
      // metadata: path
      const path = Reflect.getMetadata(
        MetadataKeys.path,
        target.prototype,
        key
      );
      // metadata: method
      const method: Methods = Reflect.getMetadata(
        MetadataKeys.method,
        target.prototype,
        key
      );
      // metadata: middleware
      const middlewares =
        Reflect.getMetadata(MetadataKeys.middleware, target.prototype, key) ||
        [];

      if (path) {
        // Associate the (routeHandler + path + method + middlewares) and add to the Router
        router[method](routePrefix + path, ...middlewares, routeHandler);
      }
    }
  };
}
