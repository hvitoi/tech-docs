# Iterates over a list

for i in $(seq 1 5); do
  echo $i
done

for i in 1 2 3 4 5; do
  echo "Welcome $i times"
done

for i in eat run jump play; do
  echo $i
done

for i in {1..5}; do # same as 1 2 3 4 5
  touch $i
done

for file in ~/.config/*; do
  echo $file
done

for word in $(cat ~/.zshrc); do
  echo $word
done
