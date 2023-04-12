# Create

readarray -t MY_ARRAY < <(ls -la)
FOO=("alpha" "beta" "gamma") # can contain different data types

# Access
echo $FOO       # first element
echo ${#FOO[@]} # size
echo ${!FOO[@]} # indexes
echo ${FOO[0]}  # first element
echo ${FOO[*]}  # all elements

# Update

FOO[0]="new-alpha" # update first element
echo ${FOO[*]}

FOO+=("delta") # add element
echo ${FOO[*]}

# Remove

unset FOO[0] # remove first element
echo ${FOO[*]}
