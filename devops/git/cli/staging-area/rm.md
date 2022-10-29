# rm

- Remove files from repository `git rm`
- Remove files from repository + filesystem `git rm --cached`

```sh
# Remove file from repository and filesystem. Remove from index only when you commit
git rm "filename"
git rm "filename" -r # recursive
git rm "filename" --force

# remove file from repository only
git rm --cached "filename"
git rm --cached -r "folder"
```
