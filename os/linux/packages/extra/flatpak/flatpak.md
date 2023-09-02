# flatpak

## remotes

- List all remotes

```shell
flatpak remotes
```

## list

- List all installed packages

```shell
flatpak list
```

## install

```shell
flatpak install "flathub" "com.spotify.Client"
flatpak install "com.spotify.Client" # flathub by default
```

## uninstall

```shell
flatpak uninstall "com.valvesoftware.Steam.CompatibilityTool.Proton"
```

## run

```shell
flatpak run "com.spotify.Client"
```

## override

- Set filesystem permission for an app

```shell
# system-wide overrides
flatpak override com.foo.Bar
flatpak override --system com.foo.Bar

# user-wide overrides
flatpak override --user com.foo.Bar

# show overrides
flatpak override --show com.foo.Bar

# filesystem permission
flatpak override --filesystem "/give/permission/to/dir/" com.foo.Bar

# reset existing overrides
flatpak override --reset com.foo.Bar
```
