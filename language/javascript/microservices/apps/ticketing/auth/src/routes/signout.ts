import express from 'express';

// Create the router
const router = express.Router();

// Specify the router
router.post('/api/users/signout', (req, res) => {
  // Destroy all the cookies
  req.session = null;
  // Send empty object
  res.send({});
});

export { router as signoutRouter };
