import express from 'express';

// This is a singleton. There will be only ONE copy of the router at a time
export class AppRouter {
  // An instance of router
  private static instance: express.Router;

  // Returns the instance
  static getInstance(): express.Router {
    if (!AppRouter.instance) {
      AppRouter.instance = express.Router(); // Create a instance if there isn't
    }
    return AppRouter.instance;
  }
}

// With the singleton, it's assured that there is only one instance of router in the app
