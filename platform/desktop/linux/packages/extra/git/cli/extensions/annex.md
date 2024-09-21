# annex

- Manage files with git, without checking their contents into git
- Syncs two git repos (one local and one remote)

## init

```shell
git init
git annex init
git annex init "My repo" # repo description
```

## initremote

- Creates a special (non-git) remote

### Rclone remote

- Under the hood it interacts with rclone using the `rclone gitannex` command
- `rclone gitannex -h` for more info

```shell
# Get to know all the available options for a remote
git annex initremote MyRemote type=rclone --whatelse

# Create special remote
git annex initremote "Google Drive" \
      type=rclone \
      encryption=none \
      rcloneremotename=google-drive \
      rcloneprefix=my-files # defaults to "git-annex-rclone" directory
```

## enableremote

```shell
git annex enableremote "Google Drive"
```

## testremote

```shell
git annex testremote "Google Drive"
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

- Whenever an annexed file is moved to a subfolder, the symlink is broken. It it latter corrected by git-annex when committing the file (by a pre-commit hook)

## copy

- Copy annexed file to/from another remote

```shell
# to a special remote
git annex copy "image.png" --to "Google Drive"
```

## get

- Get the file from a symlink

```shell
# Get all symlink contents
git annex get .

# Get specific symlink
git annex get "song.mp3"
```

## sync

- Sync all `symlinks` to a remote repo
- It's a combination of the `git annex pull` and `git annex push` commands

```shell
# Sync metadata only
git annex sync

# specify the remote to sync with
git annex sync "my-remote"

# sync metadata + content
git annex sync --content
```

## drop

- Remove the content of a file from the local repository
- The file can have been removed from the tree but it is still present in the local repo

```shell
git annex drop "file.img"
```

## unused

```shell
# Get annex objects not referenced in the git tree
git annex unused

# ... in a special remote
git annex unused --from <remote>
```

## dropunused

```shell
git annex dropunused <number>
git annex dropunused 1
git annex dropunused 1-4
git annex dropunused all

# ... in a special remote
git annex dropunused --from <remote> <number>
```
