## Set/unset shell variables

# Append to a list ($PATH is a list)
set PATH /usr/local/bin /usr/sbin $PATH

# Remove element from list
set PATH (string match -v /usr/local/bin $PATH)

# Export variables to child processes
set -x key value
set -xg key value # global (global within a shell session)
set -xl key value # local (erased when the block ends)

# Erase variables
set -e key

# Check if a variable is defined
set -q key

key=value echo $key
begin; set -lx key value; echo $key; end
