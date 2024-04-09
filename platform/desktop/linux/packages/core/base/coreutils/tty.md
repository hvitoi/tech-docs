# tty

- Print the file name of the terminal connected to standard input.

```shell
tty
```

- The output is `/dev/ttyN`, when a "root" tty
  - Where N is the number of the tty, as switched by `Ctrl + Alt + Fn`
- The output is `/dev/pts/N`, when a "virtual" tty
  - When running from a terminal emulator, for instance

## Autostart a DE when logging in

```conf
# .bash_profile (bash)
# .zlogin or .zprofile (Zsh)
[ "$(tty)" = "/dev/tty1" ] && exec sway
```
