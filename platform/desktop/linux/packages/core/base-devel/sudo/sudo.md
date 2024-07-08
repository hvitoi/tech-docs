# sudo

- SUDO - Super User DO
- Run a command as another user (defaults to root user)

```shell
# Change into super user
sudo -s # Same as su -

# print sudoers configuration
sudo -ll

# login as root
sudo su

# login as another user
sudo -u <user> -- sh -c "cd /; /bin/bash"

# logs in as another user interactively
sudo -i
```
