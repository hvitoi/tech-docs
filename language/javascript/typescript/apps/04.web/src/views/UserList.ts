// Views
import { CollectionView } from './CollectionView';
import { UserShow } from './UserShow';

// Classes
import { User } from '../models/User';

// Types * Interfaces
import { UserProps } from '../models/User';

// ---

export class UserList extends CollectionView<User, UserProps> {
  renderItem(model: User, wrapperElement: Element): void {
    new UserShow(wrapperElement, model).render();
  }
}
