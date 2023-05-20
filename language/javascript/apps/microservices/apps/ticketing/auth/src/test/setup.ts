import { MongoMemoryServer } from 'mongodb-memory-server-core';
import mongoose from 'mongoose';
import request from 'supertest';
import { app } from '../app';

// Define a new global variable in TS
declare global {
  namespace NodeJS {
    interface Global {
      signup(): Promise<string[]>;
    }
  }
}

let mongo: any; // Database itself

beforeAll(async () => {
  // Increase the timeout to be able to download the binaries of mongo
  jest.setTimeout(100000);

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

// Global function to signin and return the Set-Cookie
global.signup = async () => {
  // Supertest by itself cannot store and manage cookies! The cookies are lost after received
  // This helper function make cookies be preserved

  const email = 'test@test.com';
  const password = '1234';

  const response = await request(app)
    .post('/api/users/signup')
    .send({ email, password })
    .expect(201);

  // Pull off the Set-Cookie from the authentication
  const cookie = response.get('Set-Cookie');
  return cookie;
};
