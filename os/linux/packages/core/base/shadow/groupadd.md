# groupadd

```shell
# Create a group
groupadd "group"
```

## /etc/group

- Store all groups information

- **group name**
  - name of the group
- **group password**
  - group password as "x" means the password is stored at `/etc/gshadow`
  - group password blank means no password
- **group id** (gid)
  - the group-id is also stored at /etc/passwd
  - root (0), whell (998), $USER (1000)
- **group members**
  - Users that are part of this group

```txt
root:x:0:brltty,root
```

## /etc/gshadow

- Contains encrypted password for each group
- Contains group membership and administrator information

- **group name**
  - name of the group
- **encrypted password**
  - if not, non-members can join the group by typing the password (using `newgrp`)
  - if `!` is set, no user is allowed to join using `newgrp`
  - if null, only group members can log into the group
- **group administrators**
  - users that can add or remove group members using the `gpasswd`
- **group members**
  - group members

```txt
root:::brltty,root
```
