# visudo

- Command used to edit the `/etc/sudoers`
- visudo adds groups to `/etc/sudoers`
- Uncomment `%wheel ALL=(ALL) ALL` to give all users in this group root permissions

```sh
# visudo with vi
visudo

# visudo with vim
EDITOR=vim visudo
```
