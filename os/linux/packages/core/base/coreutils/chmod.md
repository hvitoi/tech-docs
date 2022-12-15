# chmod

- The `user` is the user who created it (the owner of the file ).
- The `group` is the group of the owner
- `others` are all the other users
- `a` stands for all (u+g+o)

| type | user (u) | group (g) | others (o) |
| ---- | -------- | --------- | ---------- |
| -    | rwx      | rwx       | rwx        |

- rwx: Read, Write, eXecute
- E.g., 421, 421, 421, 700

| rwx | rw- | r-x | r-- | -wx | -w- | --x | --- |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7   | 6   | 5   | 4   | 3   | 2   | 1   | 0   |

```shell
chmod +x "file" # Make the file executable for all (u+g+o)
chmod 700 "file" # User can rwx, the rest can do nothing
chmod 731 "file" # User rwx, group -wx, others --x
chmod g-w "file" # Remove "write" from "group"
chmod a-r "file" # Remove "read" from all
chmod o+x "file" # Add "read" to others
chmod u-r "file" # Remove "read" from user
chmod a+rwx "file" # Add "read-execute" to all
```

## Directory permissions

- Folders MUST have executable permission (+x) in order to be accessible (cd into it)

```shell
# Default folder permission
chmod 755 "folder"

# Default file permission
chmod 644 "file"
```
