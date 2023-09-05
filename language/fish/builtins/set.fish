# Append to a list ($PATH is a list)
set PATH /usr/local/bin /usr/sbin $PATH

# Remove element from list
set PATH (string match -v /usr/local/bin $PATH)
