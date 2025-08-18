# uniq

- Uniq identifies duplicates
- It's important to always sort first!

```shell
sort "file" | uniq    # Display the unique lines
sort "file" | uniq -c # Display the unique lines and the number of occurrences for each
sort "file" | uniq -d # Display only the unique lines that had at least 2 occurrences
```
