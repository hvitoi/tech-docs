## SPLIT
set foo 'a:b'
echo $foo | string split ':'

## TRIM
set foo ' abc  '
string trim $foo

set foo my-package
string trim -lc my- $foo # remove prefix (equivalent to bash's ${FOO#my-})
