# Node.js

- NPM projects

```sh
# Create npm project
npm init

# Says yes to all defaults
npm init -y
```

- `node_modules`: directory that contains the dependencies
- `package.json`: contains information about the project
- `package-lock.json`: contains information about the dependencies
- <www.npmjs.com>: to search packages

## Install packages

```sh
# Install globally
sudo npm install -g "package"

# Install locally
npm install "package"
npm install "package"@"version"

# Recreate project dependencies
npm install
npm install --only=prod # do not install dev dependencies

# Development mode
npm install "package" --save-dev
```

## List packages

```sh
# All global packages
npm list -g --depth 0
```

## Update packages

```sh
# Show outdated packages
npm outdated

# Update all packages
npm update
```

## Uninstall packages

```sh
# global
npm uninstall -g `package`

# local
npm uninstall `package`
```

## Link

```sh
# Create a symlink in your global node_modules directory that points to the actual location of the project on your machine.
npm link

# Use a package in a specific project
npm link "dependency-name"
```
