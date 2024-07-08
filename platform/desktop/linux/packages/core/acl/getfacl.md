# getfacl

- Get File Access Control List

```shell
getfacl <file>

# output to a file
getfacl -R /some/path > permissions.txt
setfacl --restore=permissions.txt # restore it
```
