# variables are tied to a session
# variables in uppercase are usually reserved for system variables!
# prefer using variables in lowercase

name=Henrique
surname=Vitoi
msg="How are you?"                      # Muti-word strings must be in quotes!
echo                                    # Print blank line
echo "Good day, $name $surname. $msg\!" # quote quotes will print the variable values!
echo 'Good day, $name $surname. $msg!'  # single quote will NOT print variable values!
echo $(pwd)                             # variable from function stdout

# substring
echo ${name:1}   # enrique
echo ${name:1:5} # enriq
