# zsh

## Startup scripts

Startup scripts are executed in the following order:

1. `~/.zshenv`
1. `~/.zprofile`
1. `~/.zshrc`: non-login shells
1. `~/.zlogin`

### ~/.zshenv (Environment Variables)

- It's executed for `all types of shell` (login, non-login, scripts, etc)
- It is the first file to be sourced during initialization
- Commonly used to set for environment variables that should always be available, regardless of how zsh is invoked
- This file should not include shell options

```shell
export XDG_CONFIG_HOME="$HOME/.config"
export ZDOTDIR="$HOME/.config/zsh"

export EDITOR=vim

export LC_ALL="en_US.UTF-8"
export GOPATH="$HOME/.local/share/go"

export LESS="-R"

umask 022
```

### ~/.zprofile

- It's executed only for `login shells`
- Executed before `~/.zshrc`

### ~/.zshrc

- It's executed only for `interactive shells`

### ~/.zlogin

- It's executed only for `login shells`
- Executed after `~/.zshrc`

```shell
# welcoming message
echo "Welcome, $USER!"

# Start the i3 window manager
# Not usually done anymore since nowadays DE is usually started at boot
exec i3
```

### ~/.zlogout

```shell
clear
echo "Goodbye, $(whoami)! Have a great day!"
```

## Environment variables

- `ZDOTDIR`

## Oh My Zsh

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### Plugins

- <https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins>
- <https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins>

- Enabling plugins

```shell
vi ~/.zshrc
```

```conf
plugins=(
  git
  bundler
  dotenv
  osx
  rake
  rbenv
  ruby
)
```

### Themes

```conf
ZSH_THEME="robbyrussell" # Default theme
ZSH_THEME="agnoster" # fancy
```

```conf
ZSH_THEME="random" # random on each start
ZSH_THEME_RANDOM_CANDIDATES=(
  "robbyrussell"
  "agnoster"
)
ZSH_THEME_RANDOM_IGNORED=(pygmalion tjkirch_mod)
```

### Installation folder

- `~/.oh-my-zsh`

```shell
echo $ZSH
```
