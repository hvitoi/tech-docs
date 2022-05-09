export class Attributes<T> {
  // Receives a generic data of type T
  constructor(private data: T) {}

  // K can be any of the 'keys' in T!
  // The function returns a value of type Object['key']
  // In arrow functions, 'this' always refer to the object instantiated
  get = <K extends keyof T>(key: K): T[K] => {
    return this.data[key];
  };

  set = (update: T): void => {
    this.data = { ...this.data, ...update };
  };

  getAll = (): T => {
    return this.data;
  };
}
