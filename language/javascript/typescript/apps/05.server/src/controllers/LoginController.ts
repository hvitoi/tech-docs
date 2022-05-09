import { Request, Response } from 'express'; // types
import { get, controller, use, post } from './decorators'; // decorators
import { bodyValidator } from './middlewares';

// ---
@controller('/auth')
class LoginController {
  // @get('/')
  // add(a: number, b: number): number { // Will be an error! Because add is not a valid route handler
  //   return a + b;
  // }

  @get('/login')
  getLogin(req: Request, res: Response): void {
    res.send(`
      <form method="POST">

        <div>
          <label>Email</label>
          <input name="email" type=text" />
        </div>

        <div>
          <label>Password</label>
          <input name="password" type="password" />
        </div>

        <button>Submit</button>

      </form>
    `);
  }

  @post('/login')
  //@bodyValidator('email', 'password')\
  @use(bodyValidator('email', 'password'))
  postLogin(req: Request, res: Response): void {
    const { email, password } = req.body;
    if (email && password && email === 'hi@hi.com' && password === '123') {
      req.session = { loggedIn: true };
      res.redirect('/');
    } else {
      res.send('Invalid email or password.');
    }
  }

  @get('/logout')
  getLogout(req: Request, res: Response) {
    req.session = { loggedIn: undefined };
    res.redirect('/');
  }
}
