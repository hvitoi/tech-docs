# bash

## Startup scripts

### User

- **Generic**
  - `~/.profile`: executed only if bash_login is not found

- **Bash**
  - `~/.bash_profile`: entrypoint
  - `~/.bashrc`: invoked from bash_profile/bash_login/bashrc
  - `~/.bash_login`: executed only if bash_profile is not found

### System

- **Generic**
  - `/etc/environment`: parsed by pam_env module
  - `/etc/profile`: also loads /etc/profile.d
  - `/etc/profile.d/`: preferred folder for global variables

- **Bash**
  - `/etc/bashrc`

## Interactive Shells

- **Interactive Shell** (_Non-login shell_)

- **Non-Interactive Shell** (_Login shell_)
  - When you log into the system, either via a terminal or SSH

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
