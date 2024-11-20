# dsenableroot

- You cannot disable a root account if no other account has a `secure token` enabled(`sysadminctl -secureTokenStatus <user>`)

```shell
# Enable root account and set a password for it
dsenableroot # for the "root" user

# Enable root for an arbitrary user
dsenableroot -u "john" # for the "john" user

# Disable root account
dsenableroot -d # disable root user
dsenableroot -d -u "john" # disable root from a user
```
