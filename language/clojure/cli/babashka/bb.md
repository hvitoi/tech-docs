# bb

- Babashka does not run on JVM

```shell
# Start a repl server at localhost:59376
bb --nrepl-server 59376
```

```shell
# input from from stdin
ls | bb -i '(take 2 *input*)'
```
