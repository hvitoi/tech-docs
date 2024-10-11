# Forking

- Fork for github is a conventional repo which has a link to the original repo forked

```shell
# Add the upstream repo
git remote add upstream "https://github.com/ORIGINAL_OWNER"

# Remotes must contain origin and upstream
git remote -v

# Fetch content from upstream
git fetch "upstream"
```

## Pull request to upstream

- A PR can be opened from the forked repository to the parent (upstream) repository
- Click `compare across forks` to select the base repository/branch send the PR
- The PR is then opened in the base repository
- After PR approval, the forked repo must pull the new changes from upstream
