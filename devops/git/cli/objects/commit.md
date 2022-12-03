# commit

- Create a commit including the file changes
- Create a `new tree` object
- Create `new blob` objects (if it is needed/not present)
- The first first commit is called `root commit`
- Commit object also have a hash number
- Commit is a `wrapper` around a specific tree object

- **Example commit object content**

```txt
tree a8a1a18475a2f51b278b7a384e91152a7e4a1302
parent 0fda841818ae2217bb22f37fe758877e9a8291ff
author Henrique Vitoi <hvitoi@gmail.com> 1610246726 -0300
committer Henrique Vitoi <hvitoi@gmail.com> 1610246726 -0300

Second commit
```

- Time in commit is formatted in Unix timestamp (1 Jan 1970 - Unix epoch) + timezone
- Parent is the hash of the previous commit

```shell
# Commit files with a message
git commit -m "description"
git commit -m "description" --allow-empty # empty commit

# Commit all files currently in the working directory
git commit -a -m "description"
```

## Amend

- Amend modifies the very last commit
- A `new commit` is created and the other one is garbage collected

```shell
# Modify author
git commit --amend --author="Mike Githubber <mike.githubber@gmail.com>" # change author

# Modify message
got commit --amend -m "New message because the last one was wrong"

# Add new files to the last commit
git add .
git commit --amend --no-edit
```
