# annex

- Manage files with git, without checking their contents into git
- Syncs two git repos (one local and one remote)

## init

- Initialize a git repo with git annex
- The git annex repository has a description

```shell
git annex init "MyFiles"
```

## add

- Add a large file with git annex

```shell
git annex add "song.mp3"
```

## get

- Get the file from a symlink

```shell
git annex get "song.mp3"
```

## sync

- Sync files using changes from the remote remote
- Uses info from the remotes to sync

```shell
git annex sync
git annex sync --content # sync the big files content too
```
