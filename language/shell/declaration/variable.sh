#!/bin/bash

# variables are tied to a session
# variables in uppercase are usually reserved for system variables!
# prefer using variables in lowercase

name=Herique
surname=Vitoi
msg="How are you?"                      # Muti-word strings must be in quotes!
echo                                    # Print blank line
echo "Good day, $name $surname. $msg\!" # quote quotes will print the variable values!
echo 'Good day, $name $surname. $msg!'  # single quote will NOT print variable values!

# variable as output of a command (executed in a sub-shell)
dir_content=$(ls) # or `ls` (deprecated)
echo $dir_content
