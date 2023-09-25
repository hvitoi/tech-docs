# rbenv

- Manages multiple ruby versions

```shell
brew install rbenv

```

## install

```shell
# list all available versions to be installed
rbenv install --list

# Install a specific version
rbenv install 3.2.2
```

## global

- Use a specific version globally

```shell
rbenv global 3.2.2
```

## init

- Add `$HOME/.rbenv/bin` to your path
- Eval rbenv at the shell startup

```shell
fish_add_path -g $HOME/.rbenv/bin
eval "$(rbenv init -)"
```
