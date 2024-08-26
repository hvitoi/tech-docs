# branch

- Branch types
  - `main` (local)
  - `origin/main` (local)
  - `main` (remote)

## List

```shell
# List all local branches
git branch # * is the current branch

# List all remote branches
git branch -r

# List all local and remote branches
git branch --all

# List branches and corresponding remote branch
git branch -vv # * main 61d49e6 [origin/main] Create hello.txt (branch local/main synced with origin/main)
# to track new branches, check out to them

# List merged branches
git branch --merged

# Setup a track (link) between a local and remote branch
git branch -u origin/main main # local main branch will follow remote origin/main branch
```

## Create

- New branches created are pointed to the same commit as the previous branch

```shell
# Create a new branch
git branch "branch-name"

# Create a new branch and check it out
git branch -b "branch-name"

# Create branch out of specific SHA1 hash
git branch "branch" "SHA1"
```

## Modify

```shell
# Rename branch
git branch -m "old-name" "new-name"

# Set default branch
git branch -M "main"
```

## Delete

```shell
# Delete branch (only merged branch - no additional commits)
git branch -d "branch-name"

# Delete branch (non-merged branch - with additional commits)
git branch -D "branch-name"

# Delete branch from remote
git push "remote" --delete "branch-name"
```
