# set

- Set or unset values of `shell options` and positional parameters.
- Documentation: <https://pubs.opengroup.org/onlinepubs/9699919799.2018edition/utilities/V3_chap02.html#set>

```shell
# List environment variables
set

# Immediately exits after an error is returned (> 0)
set -e

# Return status code of the last failed command
set -o pipefail

# Error out when trying to expand an unset parameter (other than @ and *)
set -u
```

```shell
# Combine options
set -eo pipefail
```
