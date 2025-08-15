// Types & Interfaces
import { AxiosPromise, AxiosResponse } from 'axios';

interface AttributesModel<T> {
  set(value: T): void;
  getAll(): T;
  get<K extends keyof T>(key: K): T[K];
}

interface SyncModel<T> {
  fetch(id: number): AxiosPromise;
  save(data: T): AxiosPromise;
}

interface EventsModel {
  on(eventName: string, callback: () => void): void;
  trigger(eventName: string): void;
}

interface HasId {
  id?: number; // Define that the object has optionally a id
}

// ---
// T is the DataType! E.g. UserProps ...
export class Model<T extends HasId> {
  constructor(
    private attributes: AttributesModel<T>,
    private events: EventsModel,
    private sync: SyncModel<T>
  ) {}

  // Delegation of methods to the composites
  // This assignment like like can only be made if properties are initialized inline
  on = this.events.on;
  trigger = this.events.trigger;
  get = this.attributes.get;
  getAll = this.attributes.getAll;

  set(update: T): void {
    this.attributes.set(update); // Update data
    this.trigger('change'); // Trigger a 'change event'
  }

  fetch(): void {
    const id = this.get('id');
    if (typeof id !== 'number') {
      throw new Error('Cannot fetch without an id. Save first.');
    }
    // this.sync.fetch() returns a Promise
    this.sync.fetch(id).then((res: AxiosResponse): void => {
      this.set(res.data); // Set and trigger change event
    });
  }

  save(): void {
    // this.sync.save() returns a Promise
    this.sync
      .save(this.getAll())
      .then((res: AxiosResponse): void => {
        this.trigger('save');
      })
      .catch((): void => {
        this.trigger('error');
      });
  }
}
