# Create

readarray -t MY_ARRAY < <(ls -la)

# indexed array
declare -a indexed_array
declare -a indexed_array=("a" "b" "c")
indexed_array=("a" "b" "c")
indexed_array=([0]="a" [1]="b" [2]="c")
indexed_array[0]="a"
indexed_array[1]="b"
indexed_array[2]="c"

# associative array
declare -A associative_array=(["lala"]="a" ["lele"]="b" ["lili"]="c")
associative_array["lolo"]="d"

#
FOO=("alpha" "beta" "gamma") # can contain different data types

# Access
echo $FOO # array itself (prints first)

echo ${FOO[@]} # @ refers to all elements
echo ${FOO[*]} # * refers to all elements
echo ${FOO[0]} # first element

echo ${#FOO[@]} # size
echo ${!FOO[@]} # indexes (keys)

# Update

FOO[0]="new-alpha" # update first element
echo ${FOO[*]}

FOO+=("delta") # add element
echo ${FOO[*]}

# Remove

unset FOO[0] # remove first element
echo ${FOO[*]}

# Iteration
# iterations does not print in the same order of the array elements

for el in ${FOO[@]}; do
  echo $el
done

for i in ${!FOO[@]}; do
  echo "index/key": $i
  echo "value": ${FOO[$i]}
done
