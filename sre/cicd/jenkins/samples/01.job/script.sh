#!/bin/bash

# All theses variables are taken from the jenkins environment variables
FIRST_NAME=$1
LAST_NAME=$2
SHOW=$3

if [ "$SHOW" = "true" ]
then
  echo "Hello, $FIRST_NAME $LAST_NAME"
else
  echo "If you want to see the name, please mark the show option."
fi

# HOW TO RUN THIS SCRIPT
# chmod +x ./script.sh
# docker container cp ./script.sh jenkins:/tmp/script.sh (if jenkins in a container)
# ./script.sh $FIRST_NAME $LAST_NAME $SHOW 
# ./script.sh Henrique Vitoi true 
# Jenkins cannot run scripts from /media/...