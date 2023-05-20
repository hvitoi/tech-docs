// import { scrypt, randomBytes } from 'crypto'; // encrypt
// import { promisify } from 'util'; // promisify

// const scryptAsync = promisify(scrypt);

// export class Password {
//   static async toHash(password: string) {
//     const salt = randomBytes(8).toString('hex'); // Generate a random string.
//     const buf = (await scryptAsync(password, salt, 64)) as Buffer; // Create the buffered hash

//     return `${buf.toString('hex')}.${salt}`;
//     // The hashed pass and the buffer are sent together separated by a comma
//   }

//   static async compare(storedPassword: string, suppliedPassword: string) {
//     const [hashedPassword, salt] = storedPassword.split('.'); // Separate both parts of the stored password
//     const buf = (await scryptAsync(suppliedPassword, salt, 64)) as Buffer; // Hash the supplied password
//     return buf.toString('hex') === hashedPassword; // Compare and send
//   }
// }
import { createHash } from 'crypto';

export class PasswordManager {
  static toHash(password: string) {
    return createHash('sha512').update(password).digest('hex');
  }

  static compare(storedPassword: string, suppliedPassword: string) {
    const hashedSuppliedPassword = createHash('sha512')
      .update(suppliedPassword)
      .digest('hex');
    return storedPassword === hashedSuppliedPassword;
  }
}
