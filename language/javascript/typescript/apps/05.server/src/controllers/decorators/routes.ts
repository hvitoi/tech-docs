import 'reflect-metadata';
import { Methods } from './Methods';
import { MetadataKeys } from './MetadataKeys';
import { RequestHandler } from 'express';

// ---

interface RouteHandlerDescriptor extends PropertyDescriptor {
  value?: RequestHandler; // The value in the PropertyDescriptor must be a valid route handler
}

// E.g., @routeBinder('get')('/login')
function routeBinder(method: string) {
  return function (path: string) {
    return function (target: any, key: string, desc: RouteHandlerDescriptor) {
      /// Defines metadata to a method in the class!
      Reflect.defineMetadata(MetadataKeys.path, path, target, key);
      Reflect.defineMetadata(MetadataKeys.method, method, target, key);
    };
  };
}

export const get = routeBinder(Methods.get); // @get('/login')
export const post = routeBinder(Methods.post); // @post('/login')
export const patch = routeBinder(Methods.patch); // ...
export const put = routeBinder(Methods.put);
export const del = routeBinder(Methods.del);
