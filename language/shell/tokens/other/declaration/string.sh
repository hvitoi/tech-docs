# variables are tied to a session
# variables in uppercase are usually reserved for system variables!
# prefer using variables in lowercase

first_name=Henrique
last_name=Vitoi
msg="How are you?"                              # Muti-word strings must be in quotes!
echo                                            # Print blank line
echo "Good day, $first_name $last_name. $msg\!" # quote quotes will print the variable values!
echo 'Good day, $first_name $last_name. $msg!'  # single quote will NOT print variable values!
echo $(pwd)                                     # variable from function stdout

# substring
echo ${msg:1}   # enrique
echo ${msg:1:5} # enriq

if [ -z ${msg+x} ]; then
  echo "var is unset"
else
  echo "var is set to '$msg'"
fi

echo "String size ${#first_name})"
