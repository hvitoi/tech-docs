(sleep 1 && echo hey) &

# PID of the last executed command
echo $!
kill $!
