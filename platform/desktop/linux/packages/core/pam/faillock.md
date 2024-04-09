# faillock

- Show failed password attempts per user
- Failed attempts info is stored at `/var/run/faillock/` (tally directory)

```shell
faillock

# reset counter
# or remove /var/run/faillock/theuser
faillock --user "theuser" --reset
```
