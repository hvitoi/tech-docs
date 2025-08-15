import mongoose from 'mongoose';
import { PasswordManager } from '../services/password-manager';

// Props of the User
interface UserAttrs {
  email: string;
  password: string;
}

// Props of the Document (One single record).
// It is necessary because mongoose add different other properties to the document
interface UserDoc extends mongoose.Document {
  email: string;
  password: string;
}

// Props of the Model (Entire collection of data)
interface UserModel extends mongoose.Model<UserDoc> {
  build(attrs: UserAttrs): UserDoc;
}

// ---

// Create Schema
const userSchema = new mongoose.Schema(
  {
    email: {
      type: String, // This is not typescript syntax!!
      required: true
    },
    password: {
      type: String,
      required: true
    }
  },
  {
    toJSON: {
      // Transform the mongoose document (doc) into a customized object (ret - return)
      transform(doc, ret) {
        ret.id = ret._id;
        delete ret._id;
        delete ret.password; // Remove the pass from the document (not from the database)
        delete ret.__v;
      }
    }
  }
);

// Pre-Save Hook (method)
userSchema.pre('save', async function (done) {
  // function keyword must be used! Cannot use arrow functions
  if (this.isModified('password')) {
    // This if statement assures that the password doesn't get rehashed if it was not changed
    const hashedPassword = await PasswordManager.toHash(this.get('password'));
    this.set('password', hashedPassword);
  }
  done();
});

// Static methods
userSchema.statics.build = (attrs: UserAttrs) => {
  // A function to be used to build a new user to be created
  // Now TS is aware of the properties being passed to create a user
  return new User(attrs);
};

// Create model from a schema
const User = mongoose.model<UserDoc, UserModel>('User', userSchema);

// Export
export { User };
