# lfs

```shell
pacman -S "git-lfs"
```

- `Git Large File Storage` (LFS) replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the file contents on a remote server like GitHub.com or GitHub Enterprise.

## install

- Set up the git repo as an lfs repo
- Updates git hooks (`pre-push`, `post-merge`, `post-commit`, `post-checkout`)

```shell
git lfs install
```

## track

- Start tracking some files as lfs
- This adds info to the `.gitattribute` file

```shell
git lfs track "*.mp3"
```

```conf
*.mp3 filter=lfs diff=lfs merge=lfs -text
```

## env

```shell
git lfs env
```
