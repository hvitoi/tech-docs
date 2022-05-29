// Views
import { View } from './View';
import { UserShow } from './UserShow';
import { UserForm } from './UserForm';

// Models
import { User } from '../models/User';

// Types & Interfaces
import { UserProps } from '../models/User';

// ---

export class UserEdit extends View<User, UserProps> {
  // regions contained inside of this view
  // the regions will be mapped to the HTMLElement with the mapRegions() function
  getCurrentRegions(): { [key: string]: string } {
    return {
      userShow: '.user-show',
      userForm: '.user-form'
    };
  }

  onRender(): void {
    // Do the nesting!
    const userShow = new UserShow(this.regions['userShow'], this.dataModel); // new UserShow(parent, dataModel)
    userShow.render();

    const userForm = new UserForm(this.regions['userForm'], this.dataModel);
    userForm.render();
  }

  template(): string {
    return `
    <div>
      <h1>Henrique's framework!</h1>
      <div class="user-show"></div>
      <div class="user-form"></div>
    </div>
    `;
  }
}
