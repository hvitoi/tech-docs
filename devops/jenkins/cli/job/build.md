# build

`-c`: only run if there has been an SCM (source code management) change
`-f`: follow the build progress. Interrupts are not passed to the build process
the job
`-s`: follow the build progress. Interrupts are passed to the build process
`-p`: build parameters in the key=value format.
`-v`: print console output of the build. Use with -s or -f
`-w`: Wait until the start of the command (default: false)

```shell
# build with parameters
jenkinscli build "job-name" -p "key1=value1" -p "key2=value2"

# build and follow progress
jenkinscli build "job-name" -s
jenkinscli build "job-name" -f # same as -s but interrupt will not reflect to the build process

# build and follow progress and print console output
jenkinscli build "job-name" -s -v

# wait until build start
jenkinscli build "job-name" -w
```
