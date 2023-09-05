# with test
if test "$fish" = flounder
    echo FLOUNDER
end

# with arbitrary command
if grep fish /etc/shells
    echo Found fish
else if grep bash /etc/shells
    echo Found bash
else
    echo Got nothing
end

# and / or

if command -sq fish; and grep fish /etc/shells
    echo fish is installed and configured
end
