readarray -t MY_ARRAY < <(ls -la)

FOO=("a" "b" "c")

FOO_SIZE=${#FOO[@]}
FOO_INDEXES=${!FOO[@]}
FOO_FIRST=${FOO[0]}
FOO_ALL=${FOO[*]}

echo $FOO_SIZE
echo $FOO_INDEXES
echo $FOO_FIRST
echo $FOO_ALL
