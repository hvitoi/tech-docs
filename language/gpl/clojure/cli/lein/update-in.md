# lein update-in

- Perform arbitrary transformations on your project map.

```shell
lein update-in :plugins conj '[mydep/mydep "0.13.0"]' -- mydep-cli doctor

# Update project.clj before running a lein command
# Useful for injecting the required debugging dependencies before running a repl session
environment=test \
lein update-in :dependencies conj '[nrepl,"1.1.1"]' \
  -- update-in :plugins conj '[cider/cider-nrepl,"0.47.1"]' \
  -- update-in '[:repl-options,:nrepl-middleware]' conj '["cider.nrepl/cider-middleware"]' \
  -- repl :headless
```
