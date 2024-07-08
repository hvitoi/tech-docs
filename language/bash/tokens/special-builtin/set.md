# set

- Set or unset values of `shell options` and positional parameters.
- Documentation: <https://pubs.opengroup.org/onlinepubs/9699919799.2018edition/utilities/V3_chap02.html#set>

```shell
# List environment variables
set

# Strict mode: Immediately exits after an error is returned (> 0). Recommended!
set -e

# Error out when trying to expand an unset parameter (other than @ and *)
set -u

# Abort on errors within pipes (return status code of the last failed command)
set -o pipefail

# Debugging mode
set -x
set -v # additionally logs raw inputs
```

```shell
# Combine options
set -euo pipefail
```
