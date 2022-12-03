# repl

- Start a repl session either with the current project or standalone

```shell
# start new REPL server and connect client
lein repl
lein repl :start # default

# start new REPL server but do not connect
lein repl :headless

# connect to existing REPL server
lein repl :connect nrepl://localhost:52684
```
