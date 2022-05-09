# lein

- It's the build tool for clojure

## Configuration files

- `~/.lein/project.clj`: common config for all projects

```clojure
;; ~/.lein/project.clj
:repositories {"my.datomic.com" {:url "https://my.datomic.com/repo"
                                 :creds :gpg}}
:dependencies [[com.datomic/datomic-pro $VERSION]]
```

- `~/.lein/credentials.clj.gpg`: secrets

```clojure
{#"my\.datomic\.com" {:username "mymail@mail.com"
                      :password "mypass"}}
```

- `~/.lein/profiles.clj`: additional plugins

```clojure
{:user {:plugins [[lein-exec "0.3.7"]]}}
```

## new

```shell
# create a project
lein new "app" "my-app" # "app" template
lein new "my-app" # "default" template
```

## run

```shell
# run the current project (-main function in :main namespace)
lein run

# run with arguments
lein run "arg1" "arg2"

# run a different function
lein run -m "namespace/function" "arg1" "arg2"
```

## test

- Run tests

```shell
lein test
```

## uberjar

```shell
# Package up the project files and all dependencies into a jar file
lein uberjar
```

## repl

```shell
# start a local REPL server
lein repl
lein repl --headless

```

```repl
(-main)
(println "Hello World!") => nil
(+ 2 3) => 5
```

## deps

```shell
# install dependencies
lein deps
```

## exec

- Requires `lein-exec` plugin in `profiles.clj`

```clojure
{:user {:plugins [[lein-exec "0.3.7"]]}}
```

```shell
lein exec "app.clj"
```
