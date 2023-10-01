# bash

- Startup scripts
  1. `~/.bash_profile`: entrypoint
  1. `~/.bash_login`: executed only if bash_profile is not found
  1. `~/.profile`: executed only if bash_login is not found
  1. `~/.bashrc`: invoked from bash_profile/bash_login/bashrc

## Interactive Shells

- **Interactive Shell** (Non-login shell)
  - Executes all the startup scripts
  - Example: a terminal emulator, a ssh
- **Non-Interactive Shell** (Login shell)
  - Does not execute any startup script
  - Example: executed from a script, child shells
