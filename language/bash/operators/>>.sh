# >> (redirect append)
# - Same as `>`, but appends to a file (instead of overwriting)

echo "hello" >>stdout.txt  # stdout only (default)
echo "hello" 1>>stdout.txt # stdout only
echo "hello" 2>>stderr.txt # stderr only