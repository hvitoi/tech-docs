# dnf

- DNS is the default package manager in Fedora
- Eliminates the need of using `rpm` directly
- It's the replacement for `yum` (which is deprecated)
- General config: `/etc/dnf/*`
- Repo config: `/etc/yum.repos.d`

## search

```shell
dnf search <package>
```

## install

```shell
dnf install <package>
```

## reinstall

```shell
dnf reinstall <package>
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
dnf list # --all (default)
dnf list --installed
dnf list --installed | sort -k 3
```

## info

```shell
dnf info <package>
dnf info --installed # info for all installed packages
```

## mark

- Mark/unmark package as installed by the user

```shell
dnf mark install <package> # mark package as installed by user ?
dnf mark remove <package> # unmark package as installed by user ?
```

## provides

- Finds which package provides a given value (e.g., a binary or file)
- Similar to `pacman -F <file>`

```shell
dnf provides <value>
dnf provides "ping" # returns the iputils package
```

## repository-packages

- Get the repo-id with `dnf repolist`

```shell
dnf repository-packages <repo> list
dnf repository-packages <repo> list --installed
```

## group

- Groups are a collection of bundled packages
- Types of Groups
  - `Group`: Groups of packages
  - `Environment Group`: Groups of groups

```shell
# Installed groups (groups & environment groups)
dnf group list
dnf group list --hidden # show also the groups which are part of other groups
dnf group list -v # show group id
dnf group list --installed # installed only

# Group information (includes the contents of the group)
dnf group info <group>

# install
dnf group instal <group>
dnf group install "Fedora Workstation" # by group-name
dnf group install "workstation-product-environment" # by group-id
```

## repolist

```shell
dnf repolist
dnf repolist -v
```

## repoquery

```shell
# Query all packages (in all repos)
dnf repoquery
dnf repoquery --all # same
dnf repoquery '*' # same
dnf repoquery --userinstalled # explicitly installed
dnf repoquery --installed # explicitly installed
dnf repoquery --nevra # (default) name-epoch:version-release.architecture
dnf repoquery --nvr # name-version-release

# Get the group that a package belongs to
dnf repoquery --groupmember <package>
dnf repoquery --groupmember <package>

# Find packages that depends on a package
dnf repoquery --whatrequires <package> # mandatory
dnf repoquery --alldeps --whatdepends <package> # packages that depends on a provider
dnf repoquery --exactdeps --whatdepends <package> # packages that depends on a provider or exact dependencyc

# Capabilities by packages
dnf repoquery --requires <package> # mandatory capabilities
dnf repoquery --provides <package> # capabilities provided by this package
dnf repoquery --requires --resolve <package> # resolve capabilities into packages

# Package that own a file
dnf repoquery -f <file>
dnf repoquery -f "/usr/bin/vim" # must be full-path

# List files in a package
dnf repoquery -l <package>

# Package info
dnf repoquery -i <package>
```

## leaves (plugin)

- Install plugin: `sudo dnf install 'dnf-command(leaves)'`
- List installed packages not required by any other package

```shell
dnf leaves
```