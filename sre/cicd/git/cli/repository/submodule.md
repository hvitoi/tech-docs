# submodule

- Submodule config is stored at `.gitmodules`

## add

- Add a submodule into an existing git repo

```shell
cd themes
git submodule add https://github.com/devcows/hugo-universal-theme # clones at themes/hugo-universal-theme
```

```conf
# .gitmodules
[submodule "themes/hugo-universal-theme"]
 path = themes/hugo-universal-theme
 url = https://github.com/devcows/hugo-universal-theme
```

- A placeholder file is created at the submodule location to indicate that a repo is cloned there

```diff
diff --git a/themes/hugo-universal-theme b/themes/hugo-universal-theme
new file mode 160000
index 0000000..b3bcc5e
--- /dev/null
+++ b/themes/hugo-universal-theme
@@ -0,0 +1 @@
+Subproject commit b3bcc5e18f155ffd019c1d953381ea6352a345fd
```

## update

```shell
git submodule update --init
```

## Other operations with submodules

```shell
# Automatically clone submodules as well
git clone --recursive <repo.git>

# pull submodules
git pull --recurse-submodules

# ignore dirty commits in the submodule
git config -f .gitmodules submodule.mymodule.ignore dirty
```
