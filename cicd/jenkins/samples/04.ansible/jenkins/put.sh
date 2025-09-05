#!/bin/bash

id=0

while [ $id -lt 10 ]
do
  let id=id+1

  name=`nl people.txt | grep -w $id | awk '{print $2}'`
  surname=`nl people.txt | grep -w $id | awk '{print $3}'`
  age=`shuf -i 20-25 -n 1`

  mysql -uroot -p123 -e "USE people; INSERT INTO register VALUES ($id, '$name', '$surname', '$age')"
  echo "Person $count ($name $surname, $age) inserted into database"
done