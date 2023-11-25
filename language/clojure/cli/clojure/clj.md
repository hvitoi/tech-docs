# clj

- `clj` and `clojure` differ in that 'clj' has extra support for use as a REPL in a terminal, and should be preferred unless you don't want that support, then use 'clojure'.
- Fetches and uses the dependencies are defined at `deps.edn`

```shell
# start repl using dependencies from deps.edn
clj
```

## Exec Opts

```shell
# Execute a function (src/ is used as default classpath)
clj -X "myns/myfn"

# Execute an alias (defined at deps.edn)
clj -A:mycustomalias
```

## Clj Opts

```shell
# Specify a custom deps data (other than deps.edn)
clj -S deps "customdeps.edn"

# Start a nrepl server (nrepl://localhost:59566)
clojure \
  -Sdeps '{:deps {nrepl/nrepl {:mvn/version,"1.0.0"},
                  cider/cider-nrepl {:mvn/version,"0.28.5"}}}' \
  -M -m nrepl.cmdline \
  --middleware "[cider.nrepl/cider-middleware]"
```

## Main Opts

```shell
# Call the -main function of a given namespace
clj -m "myns"
```
