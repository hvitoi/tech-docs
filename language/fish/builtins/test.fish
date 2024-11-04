# = (equals to)
test (hostname) = foo
test "$fish" = flounder

# -gt (greater than)
test 10 -gt 5

# -e (file, dir or symlink exists)
test -e /etc/hosts

# -d (directory exists)
test -d /Volumes/music

# -n (var is defined)
test -n $argv[1]
