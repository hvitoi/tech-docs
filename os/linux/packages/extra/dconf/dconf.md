# dconf

- Database of configuration
- `/etc/dconf/db`

## list

- List contents of the database

```shell
dconf list "/"
```

## update

```shell
# recompile the database
dconf update
```

## dump

- Dump all the content to stout

```shell
dconf dump "/"
```
