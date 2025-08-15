## Set/unset shell variables

# Append to a list ($PATH is a list)
set PATH /usr/local/bin /usr/sbin $PATH

# Remove element from list
set PATH (string match -v /usr/local/bin $PATH)

# Export variables so that it's available to child processes
set -x "<key>" "<val>"

# Global variable (within a shell session)
set -g "<key>" "<val>"

# Local variables (within a function/block)
set -l "<key>" "<val>"

# Erase variables
set -e key

# Check if a variable is defined
set -q key

key=value echo $key
begin
    set -lx key value
    echo $key
end
