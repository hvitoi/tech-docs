# ls-remote

- Get remote information

```shell
# Get the hash of the latest commit
git ls-remote https://github.com/t2linux/linux-t2-patches.git refs/heads/main | cut -d$'\t' -f1
```
