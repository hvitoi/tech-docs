import express from 'express';
import { currentUser } from '@hvtickets/common'; // middleware

// Create the router
const router = express.Router();

// Specify the router
router.get('/api/users/currentuser', currentUser, (req, res) => {
  res.send({ currentUser: req.currentUser || null });
});

export { router as currentUserRouter };
