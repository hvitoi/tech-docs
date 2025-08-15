# Brace expansion

# - Brace expansion is performed before any other expansion
# - Therefore a range like `{1..20}` cannot be expressed with variables using `{$a..$b}`
# - Use `seq` or a `for loop` instead, e.g., `seq $a $b` or `for((i=a; i<=b; i++)); do ... ; done.`

# Sequence
echo {1..10}

# enum
mv foo.{txt,pdf} some-dir

#
cp somefile{,.bak} # expands to cp somefile somefile.bak
