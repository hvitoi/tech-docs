# chsh

- Change default shell
- The shell binary must be authorized in `/etc/shells`
- The default shell is defined per user and it's stored at `/etc/passwd`

```shell
# Change the default shell for the current user
chsh -s "shell"

# Example for zsh
chsh -s $(which zsh) # Log out to apply!

# Check the user shell
cat /etc/passwd | grep "username"
echo $SHELL
```
