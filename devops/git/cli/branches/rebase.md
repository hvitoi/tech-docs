# rebase

```shell
git checkout feature
git rebase master # rebase feature branch on top of base branch
git checkout master
git merge feature # merge feature branch into base branch (FF will be used)
```

## rebase with conflicts

```shell
# first resolve the conflicts and add changes them to staging area
git rebase --continue
git rebase --skip # skip commit
git rebase --abort # abort
```

## Rebase with squash

- Condense all commits of a feature branch as a single commit
- Must be done `interactively`
- `SHA1` must be the `common commit` between feature and base branches

```shell
git rebase "SHA1" --interactive
git rebase "62079b5" -i
```

- `pick` (p): use commit
- `reword` (r): use commit, but edit its message
- `edit` (e): use commit, but stop for amending
- `squash` (s) use commit, but meld into previous commits

```txt
pick 100001 a
squash 100002 b
squash 100003 c
```

- After rebasing with squash, merge can be done via `fast-forward`
