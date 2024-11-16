# config

- Git configuration

```shell
# List all the config parameters
git config --list
git config -l

# Set configuration globally
git config --global user.name "Henrique Vitoi"
git config --global user.email "user@example.com"
git config --global credential.helper "cache" # caches the password/token
git config --global pull.ff only       # fast-forward only
```
