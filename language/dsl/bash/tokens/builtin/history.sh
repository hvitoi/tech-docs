# Show the last executed commands
history # 1000 by default

# clear history in the current shell
history -c # clear history in the current shell
history -d # delete entry
history -w # save to history file

# Execute the nth command "!<command-number>"
!455 # executes command number 455
!!   # executes last command
!$   # last argument

# - File the stores the history: `~/.bash_history`
