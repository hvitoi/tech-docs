# > (redirecting output)

# - Standard input (`/dev/stdin`): file descriptor number `0`
# - Standard output (`/dev/stdout`): file descriptor number `1`
# - Standard error (`/dev/stderr`): file descriptor number `2`

# - <https://web.archive.org/web/20230315225157/https://wiki.bash-hackers.org/howto/redirection_tutorial>
# - <https://www.baeldung.com/linux/pipes-redirection>

## Output Redirection "n> file"
# - Changes the file descriptor 1 (stdout) or 2 (stderr)

# stdout to file
echo "hello" >stdout.log
echo "hello" 1>stdout.log
echo "hello" 1>/dev/null # to black hole

# stderr to file
echo "hello" 2>stderr.log

# stdout and stderr to file
echo "hello" &>stdout_stderr.log

# stdout to one, stderr to another
echo "hello" 1>stdout.log 2>stderr.log # it's not possible to redirect both to the same file like that. Whichever comes last wins.

# new file descriptor (rarely used)
echo "hello" 3>mydescriptor.log

## Duplicating File Descriptor "n>&m"

# 1. ">file" redirects stdout to file
# 2. "2>&1" redirects stderr to where stdout redirects (file)
echo "hello" >file.log 2>&1

# stderr goes to the same place where stdout goes
ls /tmp/ doesnotexist 2>&1 | less # shows both streams

echo "hello" "Folder not allowed." 1>&2

# swap stdout with stderr
ls -la "i-dont-exist" 3>&2 2>&1 1>&3 | wc -l
