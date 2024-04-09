# sysadminctl

- This CLI is not available from Recovery
- Use `-` to type passwords interactively

```shell
# Create a new user
sysadminctl -addUser myself -admin -password -
```

```shell
# Enable secure token for a given user
sysadminctl -secureTokenOn myself -password - -adminUser root -adminPassword -
```
