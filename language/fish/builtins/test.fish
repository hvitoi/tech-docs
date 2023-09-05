
if test (cat /etc/hostname) = foo
    echo hey
end

# Assert string
if test "$fish" = flounder
    echo FLOUNDER
end

# Assert number
if test "$number" -gt 5
    echo $number is greater than five
else
    echo $number is five or less
end

# This test is true if the path /etc/hosts exists
# - it could be a file or directory or symlink (or possibly something else).
if test -e /etc/hosts
    echo We most likely have a hosts file
else
    echo We do not have a hosts file
end
