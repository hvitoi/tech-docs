# search

```sh
# Search a chart in a repo
helm search repo "stable" # show latest version of charts found
helm search repo "strimzi"
helm search repo "strimzi" --version 0.20 # show charts by version
helm search repo "strimzi" --versions # list all the versions (-l)
```
