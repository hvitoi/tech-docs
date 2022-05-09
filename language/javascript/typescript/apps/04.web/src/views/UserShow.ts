// Views
import { View } from './View';

// Models
import { User } from '../models/User';

// Types & Interfaces
import { UserProps } from '../models/User';

// ---

export class UserShow extends View<User, UserProps> {
  template(): string {
    return `
      <div>
        <h2>User Detail</h2>
        <div>User Name: ${this.dataModel.get('name')}</div>
        <div>User Age: ${this.dataModel.get('age')}</div>
      </div>
    `;
  }
}
