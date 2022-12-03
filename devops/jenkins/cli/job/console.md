# console

- Console output of a specific build
- As if you are doing `cat build.log`

- The build is referenced by the build number or the permalink
  - Defaults to lastBuild if not specified

```shell
# show build log
jenkinscli console "job-name" "build-number"
jenkinscli console "job-name" # last build

# display last n linest
jenkinscli console "job-name" -n "10"

# follow build log if in progress
jenkinscli console "job-name" -f
```
