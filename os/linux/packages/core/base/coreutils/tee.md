# tee

- Store and view at same time

```shell
# Display and save to a file
echo "Example" | tee "file.txt" # Replaces text (>)
echo "Example" | tee -a "file.txt" # Appends text (>>)

# Display and save to multiple files
echo "Example" | tee "file1.txt" "file2.txt" "file3.txt"
```

```shell
# privileges to write
sudo echo 1 > "/proc/sys/kernel/sysrq" # won't work! redirect does not have permissions
echo 1 | sudo tee "/proc/sys/kernel/sysrq" # works!
```
