# tty

- Print the file name of the terminal connected to standard input.

```shell
tty
```

- The output is `/dev/ttyX`, when a "root" tty
  - Where X is the number of the tty, as switched by `Ctrl + Alt + FX`
- The output is `/dev/pts/X`, when a "virtual" tty
  - When running from a terminal emulator, for instance
