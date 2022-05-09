# chage

- Change user-specific policies
- User-specific policies can be also seen at `/etc/shadow`

```shell
# Show password policy for a user
chage "username" -l

# Minimium number of days between password changes
chage -m "5" "username"

# Minimium number of days the same password can be used
chage -M "90" "username"

# Warn N days before it expires
chage -W "10" "username"

# Disable the account N days after the password expired
chage -I "3" "username"

# Date in which the account will expire (days from 1970)
chage -E "1627445999" "username"
```

## Default policy

- `/etc/login.defs` stores the default policy configuration

```conf
PASS_MAX_DAYS 99999
PASS_MIN_DAYS 0
PASS_MIN_LEN 5
PASS_WARN_AGE 7
```
