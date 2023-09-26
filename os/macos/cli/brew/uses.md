# uses

```shell
# lists packages that depends on m4 package
brew uses m4 --installed
```

```shell
brew uses m4 --installed # required by rbenv
brew remove m4 --ignore-dependencies
brew reinstall rbenv
```
