# trap

- Detect and abort on common errors and print a message:

```shell
set -euo pipefail
trap "echo 'error: Script failed: see failed command above'" ERR
```
