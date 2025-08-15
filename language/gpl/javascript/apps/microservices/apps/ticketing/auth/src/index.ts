import mongoose from 'mongoose';
import { app } from './app';

// A start script is made because some versions of node do not support 'await' syntax on top level
const start = async () => {
  // Check the existence of environment variables
  if (!process.env.JWT_KEY) throw new Error('JWT_KEY must be defined');
  if (!process.env.MONGO_URI) throw new Error('MONGO_URI must be defined');

  try {
    // Connect to MongoDB
    mongoose.set('useNewUrlParser', true);
    mongoose.set('useUnifiedTopology', true);
    mongoose.set('useCreateIndex', true);
    await mongoose.connect(process.env.MONGO_URI);
    console.log('Authentication Service MongoDB is running.');

    // Start express
    app.listen(3000, () => {
      console.log('Authentication Service is running.');
    });
  } catch (err) {
    console.error(err);
  }
};

// Start app
start();
