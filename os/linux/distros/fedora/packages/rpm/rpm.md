# rpm

- Package manager for red hat linux distributions

## Package information

```shell
# List all packages
rpm -qa

# Number of packages installed
rpm -qa | wc -l

# Check a specific package
rpm -qa | grep <package>

# Show package information
rpm -qi <package> # E.g., ksh-20120801-137.e17.x86_64

# Show package configuration
rpm -qc <package>

# Show the package that a command belongs to
rpm -qf `command-dir`
rpm -qf /etc/bin/ksh
```

## Install/Uninstall packages

```shell
# Install rpm package from file
rpm -ihv "/package/location.rmp"

# Uninstall a package
rpm -e <package> # E.g., ksh-20120801-137.e17.x86_64
```

```shell
# find files not owned by any package
sudo find / ! -path "/home/*" ! -path "/proc/*" -path "/dev/*" -path "/sys/*" | xargs rpm -qf | grep 'not owned'
```
