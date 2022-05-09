import express from 'express';
import jwt from 'jsonwebtoken';
import { Request, Response } from 'express'; // types
import { body } from 'express-validator'; // middleware

import { validateRequest, BadRequestError } from '@hvtickets/common'; // middleware & error

import { User } from '../models/user'; // model

// ---

// Create the router
const router = express.Router();

// Specify the router
router.post(
  '/api/users/signup',
  [
    // Modifies the body of the incoming request
    body('email').isEmail().withMessage('Email must be valid'),
    body('password')
      .trim()
      .isLength({ min: 4, max: 20 })
      .withMessage('Password must be between 4 and 20 characters')
  ],
  validateRequest,
  async (req: Request, res: Response) => {
    // Extract data from the request
    const { email, password } = req.body;

    // Check if user already exists
    const existingUser = await User.findOne({ email }); // UserDoc | null
    if (existingUser) throw new BadRequestError('Email in use');

    // Create user
    const user = User.build({ email, password });
    await user.save();

    // Generate JWT
    const userJwt = jwt.sign(
      {
        id: user.id,
        email: user.email
      },
      process.env.JWT_KEY!
    ); // jwt { id, email, iat }; // IAT: Issued At Time

    // Store the JWT in the SESSION (Cookie)
    req.session = { jwt: userJwt }; // It is encoded to base 64 STRING. NOT UTF-8
    // This is a Cookie-set request. It saves the cookie in the browser for the current domain (ticketing.dev)

    // Send response
    res.status(201).send(user);
  }
);

export { router as signupRouter };
