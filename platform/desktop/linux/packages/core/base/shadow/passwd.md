# passwd

```shell
# Change password an a user
passwd "username" # A prompt will ask for the old and new password

# Change password of the current user
passwd

# Lock the root account (removes the password)
sudo passwd -l root
```

```shell
# Passwords
cat /etc/passwd

# Shadows - Password information
cat /etc/shadow

# User configuration (E.g., minimum password length)
cat /etc/login.defs

# Other security config
cat /etc/pam.d/system-auth
```
