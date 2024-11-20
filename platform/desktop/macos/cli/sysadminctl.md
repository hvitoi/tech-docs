# sysadminctl

- This CLI is not available from Recovery
- Use `-` to type passwords interactively

## addUser

- Create a new user

```shell
sysadminctl -addUser myself \
  -admin \ # make the user an admin
  -password - \ # interactively type the user password
  -adminUser root -adminPassword - # name and pass of the admin in charge of creating the user
```

## deleteUser

- Create a new user

```shell
sysadminctl -deleteUser myself \
  -adminUser root -adminPassword -
```

## secureTokenStatus

- Secure token is required to be `enabled` for activating `FileVault` encryption

```shell
sysadminctl -secureTokenStatus myself
```

## secureTokenOn

- Enable secure token for a given user

```shell
sysadminctl -secureTokenOn myself \
  -password - \
  -adminUser root -adminPassword -
```

## secureTokenOff

- At least one user must have the secure token at a time (it may be the root user)

```shell
sysadminctl -secureTokenOff myself \
  -password - \
  -adminUser root -adminPassword -
```
