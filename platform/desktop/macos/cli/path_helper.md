# path_helper

- A helper for constructing PATH environment variable

- `/etc/paths`: a list of directories, one per line
- `/etc/paths.d/*`: drop-in files where packages can add their own paths

```shell
/usr/libexec/path_helper -s
```
