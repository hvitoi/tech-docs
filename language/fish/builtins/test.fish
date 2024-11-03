# =
test (hostname) = foo
test "$fish" = flounder

# -gt
test 10 -gt 5

# -e
test -e /etc/hosts # file, directory or symlink

# -d directory
if test -d /Volumes/music
    echo "The drive is mounted at /Volumes/music."
else
    echo "The drive is not mounted."
end
