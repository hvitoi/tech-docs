# export

```shell
# Export an environment variable to the current environment
export MYVAR=value

# Print the environment variable
echo $MYVAR


# View all exported variables
export -p
```

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

## User environments

- System
  - `~/.profile`
- Bash
  - `~/.bashrc`
  - `~/.bash_profile`

## Global environments

- System
  - `/etc/environment`: parsed by pam_env module
  - `/etc/profile`: also loads /etc/profile.d
  - `/etc/profile.d/`: preferred folder for global variables
- Bash
  - `/etc/bashrc`
