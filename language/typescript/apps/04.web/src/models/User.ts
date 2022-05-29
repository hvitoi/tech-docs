// Classes
import { Model } from './Model';
import { Attributes } from './Attributes';
import { ApiSync } from './ApiSync';
import { Eventing } from './Eventing';
import { Collection } from './Collection';

// ---

// Types & Interfaces
export interface UserProps {
  id?: number; // '?' indicates optional props
  name?: string;
  age?: number;
}

// ---

const rootUrl = 'http://localhost:3000/users';

export class User extends Model<UserProps> {
  // Static method to pre-initialize a user
  // User will no longer be instantiated with new User({}), but User.buildUser({})
  static buildUser(data: UserProps): User {
    // buildUser() invokes the construtor method
    return new User(
      new Attributes<UserProps>(data),
      new Eventing(),
      new ApiSync(rootUrl)
    );
  }

  // Static method to build a Collection of users
  // Instantiation of a Collection receives the url and a function to build the user
  static buildUserCollection(): Collection<User, UserProps> {
    return new Collection<User, UserProps>(rootUrl, this.buildUser);
  }

  // Method to set random age
  setRandomAge = (): void => {
    const age = Math.ceil(Math.random() * 100);
    this.set({ age });
  };
}
