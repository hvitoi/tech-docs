#!/opt/homebrew/bin/fish
set foo "a:b"

echo $foo | string split ":"
