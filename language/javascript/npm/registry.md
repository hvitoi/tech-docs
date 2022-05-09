# Create a NPM Registry (Package)

- NPM public registry (Free!)
- NPM private registry (Paid!)
- NPM public organization (Free!)
- NPM private organization (Paid!)

## Create an organization

- <https://www.npmjs.com/org/create>

- First push

```bash
git add .
git commit -m "Initial commit"
npm login
npm publish --access public
```

```json
{
  "name": "@hvtickets/common" /* The name of the package must have the format @`organization`/`package-name` */,
  "version": "1.0.0",
  "description": "",
  "main": "./build/index.js" /* Tells what file to reach to when using the import statement import ... from '@hvtickets/common */,
  "types": "./build/index.d.ts" /* Main type definition file */,
  "files": ["build/**/*"], // Specify the files that will be shipped as a package
  "scripts": {
    "clean": "del ./build/*",
    "build": "npm run clean && tsc",
    "pub": "git add . && git commit -m \"Updates\" && npm version patch && npm run build && npm publish"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "del-cli": "^3.0.1",
    "typescript": "^3.9.7"
  }
}
```

```bash
# Start up a repository
git init && git add . && git commit -m "initial commit"

# Login to npm
npm login

# Publish a package
npm publish --access public # if --access if not defined it will try to publish as private package

# ---

# Increment the version number
npm version patch # Update the last version number (E.g., 1.0.1)

# Build the new version
npm run build

# Publish the new version
npm publish

```

- The common library must be published as Javascript (even if it was written as Typescript)
- For TS projects `"declaration": true` must be true to generate a type definition file on build
- It's a good practice to export everything from a single index.js file!
