import express, { Request, Response } from 'express';
import jwt from 'jsonwebtoken';
import { body } from 'express-validator'; // validator

import { validateRequest, BadRequestError } from '@hvtickets/common'; // middleware & error

import { User } from '../models/user'; // models
import { PasswordManager } from '../services/password-manager'; // password

// Create the router
const router = express.Router();

// Specify the router
router.post(
  '/api/users/signin',
  [
    body('email').isEmail().withMessage('Email must be valid'),
    body('password').trim().notEmpty().withMessage('You must supply a password') // Trim remove spaces before and after
  ],
  validateRequest,
  async (req: Request, res: Response) => {
    const { email, password } = req.body;

    // Check if user exists
    const existingUser = await User.findOne({ email });
    if (!existingUser) throw new BadRequestError('Invalid credentials');

    // Compare passwords
    const passwordsMatch = await PasswordManager.compare(
      existingUser.password,
      password
    );
    if (!passwordsMatch) throw new BadRequestError('Invalid credentials');

    // Generate JWT and store in the SESSION (Cookie)
    const userJwt = jwt.sign(
      {
        id: existingUser.id,
        email: existingUser.email
      },
      process.env.JWT_KEY!
    );
    req.session = { jwt: userJwt };

    // Send response
    res.status(200).send(existingUser);
  }
);

export { router as signinRouter };
