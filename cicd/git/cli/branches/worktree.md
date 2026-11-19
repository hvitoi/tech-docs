# git worktree

- Git won't let the same branch be checked out in two places at once
- If a branch is already checked out in a separate worktree (a second working directory linked to the same repo), your main checkout can't have it too.

```shell
# Work in a worktree
cd /private/tmp/claude-501/.../319f5f08-10de-46f2-a806-6c16820b999f/scratchpad/wt/138

# List work trees
git worktree list
git worktree remove <path-from-above>   # add --force if it has uncommitted changes
git worktree prune # cleanup stale entries
```
