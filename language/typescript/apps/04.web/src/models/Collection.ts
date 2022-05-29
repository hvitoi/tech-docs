// Classes
// Packages
import axios, { AxiosResponse } from 'axios';

// Classes

import { Eventing } from './Eventing';

// Types & interfaces

// ---
// T is the class of data in the array
// K is the interface for the data structure
export class Collection<T, K> {
  models: T[] = []; // the source of data
  events: Eventing = new Eventing();
  constructor(public rootUrl: string, public createInstance: (data: K) => T) {}

  get on() {
    return this.events.on;
  }

  get trigger() {
    return this.events.trigger;
  }

  fetch(): void {
    axios.get(this.rootUrl).then((res: AxiosResponse): void => {
      res.data.forEach((data: K) => {
        // Create a new user for each row
        const user = this.createInstance(data);

        // Push this user into the array
        this.models.push(user);
      });
      this.trigger('change');
    });
  }
}
