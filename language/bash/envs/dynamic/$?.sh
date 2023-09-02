# exist status code of the last command
echo $?

# Code "0" means no error
# Code anything other than "0" means error
# The error code is defined per application

if [ $? -eq 0 ]; then
  echo 'Success!'
fi
