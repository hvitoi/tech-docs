# pyenv

- Python version management

```shell
# add this to your .zshrc
eval $(pyenv init --path)
```

```shell
# list python versions available for download
pyenv install --list

# install a python version
pyenv install "3.9.6"

# uninstall a python version
pyenv uninstall "3.9.6"

# list installed versions
pyenv versions

# set a version
pyenv global "3.9.6"
```
