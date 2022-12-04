# cut

- Cut parts of lines
- Print the result to the stout

```shell
# Create sample file
echo "A a
B a
C c
D d" > family
```

```shell
# Cut by letters
cut -c 2,4,6 "file" # 2nd 3rd, 6th letter of each line
cut -c 2-5 "file" # 2nd to 4th letter of each line
cut -c 2-4,6-8 "file" # ...

# Cut by bytes. 1 letter = 1 byte
cut -b 1-3 "file"

# Cut with delimiter
cut -d ":" -f 6,7 "file" # Returns the 6th and 7th "field" of the line separated by the "delimiter" :
cut -d " " -f 1,3 "file" # Delimiter is a space

# Cut from pipe
ls -l | cut -c 2-4
```
