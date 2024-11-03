# softwareupdate

```shell
# list of outdated software
softwareupdate --list

# update all outdated software
softwareupdate --install --all
softwareupdate -ia --verbose

# update the software you named
softwareupdate --install "product name"

# Rosetta 2
softwareupdate --install-rosetta --agree-to-license
```

## Servers

- MacOS servers for update services

```conf
0.0.0.0 albert.apple.com # automated updates
0.0.0.0 gdmf.apple.com # automated updates
```
