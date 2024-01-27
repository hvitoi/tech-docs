# ostree

## init

- Initialize an empty ostree repo

```shell
ostree init \
  --repo=/path/to/new/repo
```

## commit

- commit a directory into the repo
- The directory do not need to live in the repo structure. The repo can manage a completely isolated filesystem
- If `--repo` is not speficied, defaults to the current directory (if a ostree repo)

```shell
ostree commit \
  --repo==<repo-path> \
  --branch=mybranch \
  "tree/"
```

## checkout

- Checkout (copies) the files of the repo into a directory

```shell
ostree checkout \
  --repo=<repo>
  <branch> \
  <target-dir>
```

## refs

- Show all the refs (or branches) of a given repo

```shell
ostree refs \
  --repo=<repo>
```

## ls

- Inspect the filesystem of a given repo

```shell
ostree ls --repo=<repo> <branch>
```

## cat

- cat a file in the filesystem of a given repo

```shell
ostree cat --repo=<repo> <branch> <file>
```
