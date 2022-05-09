import { MongoMemoryServer } from 'mongodb-memory-server-core';
import mongoose from 'mongoose';
import jwt from 'jsonwebtoken';

// Define a new global variable in TS
declare global {
  namespace NodeJS {
    interface Global {
      signin(id?: string): string[];
    }
  }
}

// Mock files
jest.mock('../nats-wrapper');
jest.mock('../stripe.ts'); //(only for UNIT TEST)
//process.env.STRIPE_KEY = 'sk_test...'; //(only for INTEGRATION TEST)

// Database itself
let mongo: any;

beforeAll(async () => {
  // Increase the timeout to be able to download the binaries of mongo
  jest.setTimeout(50000);

  // Setup the environment variables
  process.env.JWT_KEY = 'asdf';
  process.env.MONGOMS_DOWNLOAD_URL =
    'https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1804-4.2.8.tgz';
  process.env.MONGOMS_VERSION = '4.2.8';

  // Create the database
  mongo = new MongoMemoryServer();
  const mongoUri = await mongo.getUri();

  // Connect to the database
  await mongoose.connect(mongoUri, {
    useNewUrlParser: true,
    useUnifiedTopology: true
  });
});

beforeEach(async () => {
  jest.clearAllMocks();
  const collections = await mongoose.connection.db.collections();
  // Wipe out the database
  for (let collection of collections) {
    await collection.deleteMany({});
  }
});

afterAll(async () => {
  // Disconnect from the database
  await mongoose.connection.close();

  // Stop the database
  await mongo.stop();
});

// Global function to fake a signup/signin and receive a cookie
global.signin = (id?: string) => {
  // Build a JWT payload. { id, email}
  const payload = {
    id: id || new mongoose.Types.ObjectId().toHexString(),
    email: 'test@test.com'
  };

  // Create the JWT (sign)
  const token = jwt.sign(payload, process.env.JWT_KEY!);

  // Build the session object { jwt: MY_JWT }
  const session = { jwt: token };

  // Turn the session object into JSON
  const sessionJSON = JSON.stringify(session);

  // Encode it as base64
  const base64 = Buffer.from(sessionJSON).toString('base64');

  // Return the session encoded object as a cookie (express:sess=)
  return [`express:sess=${base64}`];
};
