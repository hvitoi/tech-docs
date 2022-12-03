# less

- View the content one line at a time

```shell
# Read text file line by line (q quits)
less "file.txt"
less "file.txt" "file2.txt" # :n (next file), :p (previous file)
less +F "/var/log/syslog"
ls -la | less

# Follow
less +F "/var/log/syslog"
```

## Search

- **Forward search**

  - `/`: search for a pattern which will take you to the next occurrence
  - `n`: for next match in forward
  - `N`: for previous match in backward

  - You must escape slashes on forward search: `/\/home\/ramesh\/`

- **Backward Search**

  - `?`: search for a pattern which will take you to the previous occurrence.
  - `n`: for next match in backward direction
  - `N`: for previous match in forward direction

  - You don't need to escape slashes on backward search: `?/home/ramesh/`

## Navigation

- `j`: forward one line
- `10j`: forward 10 lines
- `CTRL+D`: forward half window
- `CTRL+F`: forward one window

- `k`: backward by one line
- `10k`: backward 10 lines
- `CTRL+U`: backward half window
- `CTRL+B`: backward one window

- `g`: start of file
- `G`: end of file
- `q` or `ZZ`: exit

## Info

- `CTRL+G`: current file name, line, byte and percentage
- `v`: using the configured editor edit the current file.
- `h`: summary of less commands
- `&pattern`: display only the matching lines, not all.
