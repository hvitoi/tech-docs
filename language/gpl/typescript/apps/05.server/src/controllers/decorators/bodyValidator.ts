import { MetadataKeys } from './MetadataKeys'; // enum

export function bodyValidator(...keys: string[]) {
  return function (target: any, key: string, desc: PropertyDescriptor) {
    // keys will be an array of strings passed by the user-developer
    Reflect.defineMetadata(MetadataKeys.validator, keys, target, key);
  };
}
