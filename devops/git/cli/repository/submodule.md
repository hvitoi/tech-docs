# submodule

```shell
# Clone submodules
git submodule update --init

# Automatically clone submodules as well
git clone --recursive "repo"

# pull submodules
git pull --recurse-submodules
```

```shell
# ignore dirty commits in the submodule
git config -f .gitmodules submodule.mymodule.ignore dirty
```