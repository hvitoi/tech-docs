# Terminal

## tty (teletype)

- It connects the shell to the operating system
- It's part of the Linux Kernel
- The tty itself doesn’t display anything. It’s just the interface the kernel exposes for text I/O.

- `/dev/tty1`: virtual console in Linux (Ctrl+Alt+F1-F6)
- `/dev/ttyS0`: serial port
- `/dev/pts/0`: pseudo-terminal used by a terminal emulator

```shell
# Access tty from another terminal
echo "Hello TTY1" > /dev/tty1
cat < /dev/tty1
```

## Terminal emulator

- A program you run in user-space that provides a window (GUI) to interact with a shell.
- It creates a pseudo-terminal (pty) to talk to the kernel's tty interface.

- `Alacritty`
- `WezTerm`
- `Ghostty`
- `Kitty`
- `xterm`

## Workflow

 -> [Keyboard]
 -> [Terminal Emulator GUI]
 -> [Pseudo-terminal (pty)]
 -> [Kernel tty subsystem]
 <> [Shell]
 <- [Kernel tty subsystem]
 <- [Pseudo-terminal]
 <- [Terminal Emulator GUI]
 <- [Screen]
