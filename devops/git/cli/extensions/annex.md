# annex

- Manage files with git, without checking their contents into git
- Syncs two git repos (one local and one remote)

## init

```shell
git init
git annex init
git annex init "My repo" # repo description
```

## add

- Files added with git annex become a symlink to a blob object at `.git/annex/objects` (even before checkout)
- The symlink is usually called `sidecar file`

```shell
# Add all
git annex add .

# Add a file
git annex add "image.png"
```

```shell
# automatically annex files which matches the wildcard as part of the conventional git add
git config annex.largefiles 'include=*.png'
```

## sync

- Sync all `symlinks` to a remote repo
- It's a combination of the `git annex pull` and `git annex push` commands

```shell
# Sync metadata only
git annex sync

# specify the remote to sync from
git annex sync "my-remote"

# sync metadata + content
git annex sync --content
```

## get

- Get the file from a symlink

```shell
# Get all symlink contents
git annex get .

# Get specific symlink
git annex get "song.mp3"
```

## drop

- Remove the content of a file from the local repository
- The file can have been removed from the tree but it is still present in the local repo

```shell
git annex drop "file.img"
```
