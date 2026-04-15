# Shell

Shell é o programa que interpreta os comandos que você digita no terminal. Ele processa os comandos e chama programas.

Common shells:

- `bash`
- `sh`
- `zsh`
- `fish`

## Types

Two independent axes that combine in any way.

### Login vs Non-login

Whether this shell is the entry point for a new user session.

- **Login shell** - SSH, console login, `su -`
- **Non-login shell** - Opening a terminal tab inside an existing session

### Interactive vs Non-interactive

Whether a human is typing commands.

- **Interactive** - You open a terminal and type
- **Non-interactive** - Running a script (`bash script.sh`)

### Common combinations

| Scenario            | Type                        |
| ------------------- | --------------------------- |
| SSH into a server   | Interactive + Login         |
| Open a terminal tab | Interactive + Non-login     |
| Run a script        | Non-interactive + Non-login |

## Bash startup files

### Load order

**Login shells** — first match wins, rest are skipped:

1. `/etc/profile`
2. `~/.bash_profile` → `~/.bash_login` → `~/.profile` (first found only)

**Interactive non-login shells:**

1. `~/.bashrc`

### User files

- **Generic** (read by any POSIX login shell — sh, dash, bash)
  - `~/.profile`: read if neither `~/.bash_profile` nor `~/.bash_login` exists

- **Bash**
  - `~/.bash_profile`: first choice for login shells; commonly sources `~/.bashrc` so login shells also pick it up
  - `~/.bash_login`: read only if `~/.bash_profile` is not found
  - `~/.bashrc`: read by interactive non-login shells

### System files

- **Generic**
  - `/etc/environment`: parsed by pam_env module (key=value pairs, not a shell script)
  - `/etc/profile`: sourced by all login shells; loads `/etc/profile.d/`
  - `/etc/profile.d/`: preferred location for system-wide environment variables

- **Bash**
  - `/etc/bashrc`: sourced by interactive shells (`/etc/bash.bashrc` on Debian/Ubuntu)
