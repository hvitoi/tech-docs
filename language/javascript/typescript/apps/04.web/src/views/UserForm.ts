// Views
import { View } from '../views/View';

// Models
import { User } from '../models/User';

// Types & Interfaces
import { UserProps } from '../models/User';

// ---

export class UserForm extends View<User, UserProps> {
  // Object that represents the events in the template
  eventsMap(): { [key: string]: () => void } {
    return {
      'click:.set-age': this.onSetAgeClick,
      'click:.set-name': this.onSetNameClick,
      'click:.save-model': this.onSaveClick
    };
  }
  // Events
  onSetAgeClick = (): void => {
    this.dataModel.setRandomAge();
  };
  onSetNameClick = (): void => {
    const input = this.parent.querySelector('input'); // Take the content of the text box

    if (input) {
      const new_name = input.value;
      this.dataModel.set({ name: new_name });
    }
  };
  onSaveClick = (): void => {
    this.dataModel.save();
  };

  // Template
  template(): string {
    return `
      <div>
        <input placeHolder="${this.dataModel.get('name')}"/>
        <button class="set-name">Change Name</button>
        <button class="set-age">Set Random Age</button>
        <button class="save-model">Save User</button>
      </div>
    `;
  }
}
