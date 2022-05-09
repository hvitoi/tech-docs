#!/bin/bash

for i in $(seq 1 10); do echo $i; done

for i in 1 2 3 4 5; do
  echo "Welcome $i times"
done

for i in eat run jump play; do
  echo $i
done

for i in {1..5}; do # same as 1 2 3 4 5
  touch $i
done
