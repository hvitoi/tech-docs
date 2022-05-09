# remote

```shell
# Show information about remotes
git remote
git remote -v # verbose
```

## add

```shell
# Add/remove remote
git remote add "remote-name" "remote-uri" # Name is usually origin
git remove add "origin" "git@github.com:hvitoi/docs.git"
git remove add "localorigin" "~/docs/"
```

## remove

```shell
git remote remove "remote-name" "remote-uri"
```

## show

```shell
# Show specific remote
git remote show "remote" # This command fetches metadata from remote
git remote show "origin"
```

## prune

```shell
# Remove from remote the things deleted locally (E.g., branches)
git remote prune "remote"
```

## update

```shell
# Remove from local the things deleted remotely (E.g., branches)
git remote update "remote" --prune
```
