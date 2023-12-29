# dnf

- DNS is the default package manager in Fedora
- Eliminates the need of using `rpm` directly
- It's similar to `yum`

## search

```shell
dnf search <package>
```

## install

```shell
dnf install <package>
```

## remove

```shell
dnf remove <package>
```

## upgrade

- Checks the repositories for newer packages and updates them.

```shell
dnf upgrade
```

## check-update

- Checks for updates, but does not download or install the packages.

```shell
dnf check-update
```

## autoremove

- Removes packages installed as dependencies that are no longer required by currently installed programs

```shell
dnf autoremove
```

## list

```shell
dns list --installed
```
