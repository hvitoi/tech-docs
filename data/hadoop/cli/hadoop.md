# hadoop

## fs

- Manipulate the HDFS

```sh
# list files at root dir
hadoop fs -ls "/"

# create directory
hadoop fs -mkdir "mydir"

# remove directory
hadoop fs -rmdir "mydir"

# copy from local
hadoop fs -copyFromLocal "file.txt" "/file.txt"

# remove file
hadoop fs -rm "/file.txt"
```
