# deps

```shell
# dependency graph
brew deps --tree --installed

# depedencies of explicitly installed packages only
brew deps --tree $(brew leaves)
```
