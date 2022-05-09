# Jest Testing Framework

## Setup configuration

```bash
jest --init
```

## Test script

```json
"scripts": {
  "start": "nodemon ./src/index.ts",
  "test": "jest  --watchAll --no-cache"
}
```

- watchAll runs all the .test files in the folder
- no-cache to use TS with jest

## Jest configuration

```json
"jest": {
  "preset": "ts-jest", /* TS support */
  "testEnvironment": "node", /* Jest running on NodeJS */
  "setupFilesAfterEnv": [ /* Run setup files */
    "./src/test/setup.ts"
  ]
}
```

## Folder convention

- Create a `__test__` folder inside of each other directory in the project to store the test files
- Test file will follow the naming convention `signup.test.ts`

## Response Object in Supercell

```javascript
// get() methods inspect an header of the response object
response.get('Set-Cookie');
```

## Checking the current environment mode

```javascript
app.use(
  cookieSession({
    signed: false, // Disable encryption
    secure: process.env.NODE_ENV !== 'test' // true if on 'start', false if on 'test'
    // Cookie only will be used over https if true
  })
);
```

## Sign in and return cookie

```typescript
// Define a new global variable in TS
declare global {
  namespace NodeJS {
    interface Global {
      signin(): Promise<string[]>;
    }
  }
}

// Global function to signin and return the Set-Cookie
global.signin = async () => {
  const email = 'test@test.com';
  const password = '1234';

  const response = await request(app)
    .post('/api/users/signup')
    .send({ email, password })
    .expect(201);

  const cookie = response.get('Set-Cookie');
  return cookie;
};
```

## Mocks

- Mocks fake files
- In testing, the mocked files will be called on imports instead of the original files
- `__mocks__` folder must be placed in the same directory of the file to be mocked
- Inside of the `__mocks__` folder the fake file with the same name is placed

```javascript
// Place mocking line inside of the test
jest.mock('../../nats-wrapper');
```

## Mock function

```javascript
const myMockFunction = jest.fn().mockImplementation(
  // This here is actual publish function that will be implemented
  (subject: string, data) => {
    console.log(subject);
  }
);

// Clear the stats for the mock functions before each test
beforeEach(async () => {
  jest.clearAllMocks();
}

// Expectation on mock functions
test('Function was called', async () => {
  expect(myMockFunction).toHaveBeenCalled();
}

```
