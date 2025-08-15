if command -sq fish; and grep fish /etc/shells
    echo fish is installed and configured
end

# Returns 0 only if it exists as an external program
command -q fish # 0
command -q set # 127
