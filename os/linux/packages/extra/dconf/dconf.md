# dconf

- Database of configuration
- All preferences are stored in a single large binary file: `~/.config/dconfig/user`
- **Profiles**
  - Profile is a list of config databases that dconf consults
  - Defaults to `~/.config/dconfig/user` only

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
