# mktree

- Create tree object
- Tree object is a `pointer` to other git objects
- The tree that has no other trees poiting to itself is a `root directory`
- `TAB` must be used between hash and filename

- **Example tree object content**

```txt
100644 blob ac675a8ba820e2d5edf774a0eca36a22aaedd8fa  file1.txt
100644 blob b7aec520dec0a7516c18eb4c68b64ae1eb9b5a5e  file2.txt
```

```shell
cat tree.txt | git mktree
```
