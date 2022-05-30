# rebase

- With rebase, the commits from the main branch are merged as fast-forward into the feature branch (`rebase`)
- All the commits from the feature branch are then `rewritten` on top of the new latest commit

```shell
# switch to feature branch
git checkout "feature"

# rebase "feature" branch on top of main branch
git rebase "main" # "main" under the hood is SHA1 of the last commit in main

# switch to main branch
git checkout "main"

# merge "feature" branch into base branch (FF will be used)
git merge "feature"
```

## Rebasing conflicts

- When rebasing, first git remove all new commits in the feature branch. And merge the new commits from main branch in fast-forward
- Then git takes each new commit in the feature branch, one at a time
- At each commit, it's checked wether it can be fast-forwarded, or if there are conflicts
- If there are conflicts, you must resolve it, add it to staging area (do not commit) and continue the rebasing process

```shell
# first resolve the conflicts and add changes them to staging area
git rebase --continue # continue to next feature commit
git rebase --skip # skip the conflicting feature commit (it will be discarded)
git rebase --abort # abort the whole rebasing process
```

## Rebase with squash

- Squash is a rebase with a commit in the own branch
- Squash can condense all commits of a feature branch into a single commit
- Must be done `interactively`
- `SHA1` is usually the first commit in the feature branch (the new base - rebase)

```shell
git rebase "SHA1" --interactive
git rebase "62079b5" -i
```

- `pick` (p): use commit
- `reword` (r): use commit, but edit its message
- `edit` (e): use commit, but stop for amending
- `squash` (s) use commit, but meld into previous commits

```txt
pick 100001 Message1
squash 100002 Message2
squash 100003 Message3
```

```shell
# Alternatively you can squash with the following:
git reset "SHA1" # first commit in the feature branch
git add -A && git commit -m "condensed commit"
```
