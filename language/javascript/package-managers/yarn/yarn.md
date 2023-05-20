# Yarn Package Manager

## Install package

```bash
# Install
yarn add `package`

# Install in development mode
yarn add `package` -D
```

## Upgrade packages

```bash
# On dependency "react": "~16.5.1": installs the latest version on tilde range with ~16.5.1 which is 16.5.2
yarn upgrade

# On dependency "react": "^16.5.1": installs the latest version on caret range with ~16.5.1 which is 16.8.6 as of today
yarn upgrade

# On exact dependency "react": "16.5.1" does not install anything new at all
yarn upgrade

# On dependency "react": "~16.5.1": installs the latest version 16.8.6 as of today, and updates package.json to "react": ~16.8.6"
yarn upgrade --latest

# On dependency "react": "^16.5.1": installs the latest version 16.8.6 as of today, and updates package.json to "react": ^16.8.6"
yarn upgrade --latest

# On exact dependency "react": "16.5.1" installs the latest version 16.8.6 as of today, and updates package.json to "react": 16.8.6"
yarn upgrade --latest
```
