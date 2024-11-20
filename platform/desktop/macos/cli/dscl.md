# dscl

- `Directory Service` command line utility

## Path Specification

- You can specify the `datasource` as a `node` or as a `host`
- The path specification differs depending on the kind of datasource chosen

```shell
# as a node
dscl . -list "/Users"

# as a host
dscl localhost -list "/Local/Default/Users"
```

## -f

- Specifies a `local node database` file path to be opened as a `host`

```shell
node_database='/Volumes/Macintosh HD - Data/private/var/db/dslocal/nodes/Default'
dscl -f "$node_database" localhost -list "/Local/Default/Users"
dscl -f "$node_database" localhost -passwd "/Local/Default/Users/root"
```

## list

```shell
dscl . -list "/"
dscl . -list "/Users"
```

## read

```shell
dscl . -read "/Users/root"
```

## create

- Create a new user

```shell
dscl . -create "/Users/myuser"
```

## passwd

- Change password

```shell
# Change root password
dscl . -passwd "/Users/root"
```

## delete

```shell
dscl . -delete /Groups/mygroup
dscl . -delete /Users/myuser
```
