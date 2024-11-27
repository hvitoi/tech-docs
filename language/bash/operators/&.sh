# & (amp)
# - Used for job management
# - The job will run in background on the current user session only. If the terminal is closed, the jobs are terminated

# This will print messages from the subscript, but you can replace the `&` with `>/dev/null &` and suppress the output.
for _ in $(seq 1 10); do
  curl http://example.com &
done

## Short cuts
# - `Ctrl+z`: puts a job in background
# - `Ctrl+c`: stops the currently running job
