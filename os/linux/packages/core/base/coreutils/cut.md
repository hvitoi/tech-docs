# cut

- Cut parts of lines
- Print the result to the stout

```shell
# Cut by letters
cut -c 2,4,6 "foo.txt" # 2nd 3rd, 6th letter of each line
cut -c 2-5 "foo.txt" # 2nd to 4th letter of each line
cut -c 2-4,6-8 "foo.txt" # ...

# Cut by bytes. 1 letter = 1 byte
cut -b 1-3 "foo.txt"

# Cut with delimiter
cut -d ":" -f 6,7 "foo.txt" # Returns the 6th and 7th "field" of the line separated by the "delimiter" :
cut -d " " -f 1,3 "foo.txt" # Delimiter is a space

# Cut from stdin
ls -l | cut -c 2-4
```
