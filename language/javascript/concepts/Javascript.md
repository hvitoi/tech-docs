# Javascript

- Specified in `ECMA 262`
- Level of abstraction: $$JS/Python > C/C++ > Assembly > Machine Code$$

## Styles

### CJS (Common JavaScript)

- Load modules synchronously

```javascript
// exporting
modules.exports = {
  myFunction
}

// importing
const { myFunction } = require('./file.js')
```

### ESM (ECMAScript Module)

- Available since `ES2015` (ES6?)
- Supports loading modules asynchronously
- Run implicitly in strict mode
- Requires `{"type":"module"}` in `package.json`
- The complete filename must be specified. E.g., 'file.js' (instead of 'file')

```javascript
// exporting
export {
  myFunction
}

// importing
import { myFunction } from './file.js'
```

## Code Translation

- `Interpreter`: read the source code and execute it
- `Compiler`: statically analyze all the code in advance and compile it to a binary that runs by itself on the machine

## Implementations

- Mozilla Firefox: `Spider Monkey`
- Google Chrome: `V8`

## Characteristic

- **Interpreted**
- **Dynamic weakly typed**: data type become known at runtime
- **Multi-paradigm**: declarative functional or imperative object-oriented
- **Prototype inheritance**: everything in js in an object with prototype methods inherited
- **Single-threaded**: one computation at a time
- **Garbage-collected**: clear free memory in heap when it's no longer necessary
- **Non-blocking**
- **Event Loop (JIT)**
  - For each round of the event loop
    1. Run sync code
    1. Run microtask callbacks (from `callback queue`): e.g., Promises
    1. Run macrotask callbacks (from `callback queue`): async task callbacks

```javascript
// 1st
console.log("sync1");

// 4th
setTimeout((_) => console.log("timeout"), 0);

// 3rd
Promise.resolve().then((_) => console.log("promise"));

// 2nd
console.log("sync2");
```
