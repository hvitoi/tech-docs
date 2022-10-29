# checkout

- Checkout a `commit` or `branch`
- Git changes the value of the HEAD located in `.git/HEAD`
- Practically Files are taken from `git repository` and placed into `working directory` and `staging area`
  - Completely override the content of the working directory
- Travel between different versions of the project (commits or branches)

```sh
# Go to commit
git checkout "commit-hash"

# Go to branch
git checkout "branch-name"
git checkout "-" # go to the previous branch you were working on
git checkout -b "brach-name" # Create branch if not exists
git checkout -b "local-branch" "remote-branch" # Track remote branch (or git checkout branch-name)

# Checkout to head references
git checkout "HEAD@{6}" # 6 heads back
```
