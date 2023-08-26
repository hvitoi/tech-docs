# ls

- `ls` is used for navigation through the `Linux File System`

## Output

| `type`     | `links` | `owner` | `group` | `size` | `month` | `day` | `time` | `name`     |
| ---------- | ------- | ------- | ------- | ------ | ------- | ----- | ------ | ---------- |
| drwxrwxrwx | 1       | foo     | root    | 4096   | mar     | 22    | 2:52   | Javascript |

## Listing

```shell
ls
ls -1 # multiline output
ls -l
ls -la
ls -laF
ls -ltr # Time reverse order
ls -al / > lsout.txt # List the root dir and saves in the text file
ls -la /etc/cron.* # List the content of each folder starting with cron.
ls -latrc # show modification time (instead of creation time)
```

## Listing with wildcards

- Zero or more chars
  - `*` - `ls abc*`
- A single char
  - `?` - `ls ?bc*`
- Pick of characters
  - `[]` - `ls *[aeiou]*` # Either a, e, i, o, u
- Range of chars
  - `{}` - `touch abc{1..9}-xyz`
- Escape character
  - `\`
- Beginning of line
  - `^` - `ls -l | grep ^d` # List directories
- End of line
  - `$`
