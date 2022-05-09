// Packages
import axios from 'axios';

// ---

// Types & Interfaces
import { AxiosPromise } from 'axios';

interface HasId {
  id?: number; // It's optional because if no id is passed, the element will be created
}

// ---
// T is the type of data being handled. UserProps, PostProps, etc
export class ApiSync<T extends HasId> {
  constructor(public rootUrl: string) {}

  fetch(id: number): AxiosPromise {
    return axios.get(`${this.rootUrl}/${id}`); // Returns a promise back to the user
  }

  save(data: T): AxiosPromise {
    const { id } = data;
    if (id) return axios.put(`${this.rootUrl}/${id}`, data);
    else return axios.post(this.rootUrl, data);
  }
}
