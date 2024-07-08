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

## Useful environment variables

- `$HOSTNAME`: hostname
- `$TERM`: terminal used
- `$SHELL`: user shell
- `$0`: current shell
- `$HISTSIZE`: command history length
- `$USER`: current user
- `$PATH`: list of directories (separated by `:`) to search for commands when typed in the terminal.
- `$PWD`: current directory
- `$LANG`: system language configuration
- `$HOME`: home directory

## Environments

### User

- System
  - `~/.profile`
- Bash
  - `~/.bashrc`
  - `~/.bash_profile`

### Global

- System
  - `/etc/environment`: parsed by pam_env module
  - `/etc/profile`: also loads /etc/profile.d
  - `/etc/profile.d/`: preferred folder for global variables
- Bash
  - `/etc/bashrc`
