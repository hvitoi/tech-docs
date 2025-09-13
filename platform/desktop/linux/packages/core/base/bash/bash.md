# bash

```shell
bash -c "sleep 1 && echo hello"
```

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
