# hash-object

- Create `blob` object
- `.git` maintains a separate database with its own files
- Every object in git is stored with a hash filename in the `.git` folder
- Hash-object returns the hexadecimal `SHA1 hash` of the object
- The hash location is `.git/objects/hash-folder/hash-file`, where:
  - Hash folder: first 2 letters of the hash
  - Hash file: the remaining characters of the hash
- Different values generate different hashes, therefore git can keep track of what files are identical and what files are not

- **Example blob object**

```txt
blob 11\0Hello, Git
```

```shell
# Generate object hash
git hash-object `value`
git hash-object `/path/to/file`
echo `value` | git hash-object --stdin

# Write object to git's database
git hash-object `value` -w
git hash-object `/path/to/file` -w
echo `value` | git hash-object --stdin -w
```

```shell
# Create object with value
echo "Hello, Git" | git hash-object --stdin -w

# Create object with filename
git hash-object ./index.js -w
```

## Hash function

- Take any-length input and convert it to a fixed length hash
- Hash function always generate `same hash` for `same input`
- Different input generate completely different hashes
- It's a `one-way function`. You cannot take the input value from the hash
- The input can be anything from a short string to a gigabyte file

- Some hash functions

  - `MD5` (128bit)
  - `SHA1` (160bit - 40 hex)
  - `SHA256` (256bit)
  - `SHA384` (384bit)
  - `SHA512` (512bit)

### SHA1

```shell
# Generate SHA1 hash
echo "Hello" | shasum
```

- Number of different hashes from `SHA1` hash function
  - 2^160 = 16^40 = 1.461501637×10^48
- Chance of producing same exact hash for different files in `SHA1` (`Dice theory`)
  - Probability of each SHA1 hash: 1/(2^160)
  - Probability of same exact hash: (1/(2^160))\*(1/\_(2^160)) = 1/(2^320)
- Chance of producing any exact hash for different files in `SHA1` (`Hash collision probability`)
  - Probability of same any hash: for 2 files: 2.84\*10^49
  - The probability increases with more files. E.g., 3 files -> 2.05\*10^48
