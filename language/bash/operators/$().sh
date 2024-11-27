# $()

# variable as output of a command (executed in a sub-shell)
dir_content=$(ls)
# dir_content=`ls` (deprecated form)
echo "$dir_content"
