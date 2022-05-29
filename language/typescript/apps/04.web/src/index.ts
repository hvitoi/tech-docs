// Views (classes)
import { UserList } from './views/UserList';

// Types & Interfaces
import { User } from './models/User';

// ---

// root HTMLElement
const root = document.getElementById('root');
if (!root) throw new Error('Root element not found');

// Instance of Collection
const users = User.buildUserCollection();

users.on('change', () => {
  console.log(users); // log change to console
});

users.fetch(); // Fetch all the users

new UserList(root, users).render();
