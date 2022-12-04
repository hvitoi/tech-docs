# Shell

- `Hardware` -> `Kernel` -> `Shell` -> `Application` -> `User`
- `CPU` -> `Program` -> `Bash` -> `Browser` -> `You`

Shell + Kernel = `OS`
Shell + Application = `Software`

- Shell is an interface between the users and the Kernel/OS
- `CLI` is a Shell
- `GUI` is a Shell

## Find your shell

```shell
echo $0 # Current shell
echo $SHELL # The current user default shell
cat /etc/shells # Available shells
echo $? # Print the exit code
```

## Types of Shell

- `Gnome`: Graphical shell
- `KDE`: Graphical shell
- `sh`: Command line shell. Original linux shell. Born shell. Developed by Stephan Born, therefore the name
- `bash`: Born Again SHell (New version of sh)
- `csh` and `tcsh`: C oriented shells.
- `ksh`: Korn SHell (Most used in Solaris)

## Change the default shell

- Change default shell
- The shell binary must be authorized in `/etc/shells`

```shell
# Change the default shell for the current user
chsh -s "shell"

# Example for zsh
chsh -s $(which zsh) # Log out to apply!

# Check the user shell
cat /etc/passwd | grep "username"
echo $SHELL
```

## Shell Scripting

- Shell: `#!/bin/bash`
- Comments: `# comments`
- Commands: `echo, cp, grep etc`
- Statements: `if, while, for etc`

--> Shell scripts MUST have executable permissions!
--> Shell scripts MUST be called from the absolute or relative path ./script.bash

## Aliases

```shell
# Create alias
alias ll = "ls -laF"
alias pl = "pws; ls"
alias tell = "whoami; hostname; pwd"
alias dir = "ls -l | grep ^d" # List only directories
alias d = "df -h | awk '{print \$6}' | cut -c1-4" # \$6 the \ is necessary! Otherwise the shell interprets as an environment variable

# List all aliases
alias

# Remove alias
unalias "alias_name"
```

## Shell History

```shell
# Show the last executed commands
history # 1000 by default

# The result of history feeds the less command
history | less

# Execute the nth command
!"command_number"
!455 # executes command number 455
```

- File the stores the history: `~/.bash_history`
