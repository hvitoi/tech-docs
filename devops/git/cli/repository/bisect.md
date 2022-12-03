# bisect

- Use binary search to find the commit that introducted a bug

```shell
git bisect start
git bisect bad # Current version is bad
git bisect good "v2.6.13-rc2" # v2.6.13-rc2 is known to be good
```
