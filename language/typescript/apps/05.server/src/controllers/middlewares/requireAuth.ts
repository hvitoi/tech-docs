import express, { Request, Response, NextFunction } from 'express';

// Authentication middleware
export function requireAuth(
  req: Request,
  res: Response,
  next: NextFunction
): void {
  if (req.session && req.session.loggedIn) {
    next(); // Pass to the next function
    return; // Returns nothing
  }

  res.status(403);
  res.send('Not permitted'); // Fail
}
