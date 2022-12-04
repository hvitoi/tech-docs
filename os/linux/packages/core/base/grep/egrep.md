# egrep

- A grep with multiple keywords

```shell
# Create sample file
echo "a b c" > "file.txt"
```

```shell
# OR operator
egrep -i "keyword1|keyword2" "file.txt" # Either the key1 or key2
egrep -i "a|z" "file.txt"
dmesg | egrep -i 'blue|firm'
```
