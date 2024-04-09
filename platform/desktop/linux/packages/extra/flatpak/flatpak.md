# flatpak

- Run apps in containers
  - Apps with same prefix run in the same container
  - E.g., com.valvesoftware.Steam, com.valvesoftware.Steam.CompatibilityTool.Proton, com.valvesoftware.Steam.Utility.gamescope

## remotes

- List all remotes

```shell
flatpak remotes
```

## remote-add

```shell
flatpak remote-add --if-not-exists flathub "https://flathub.org/repo/flathub.flatpakrepo"
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

## update

```shell
# update all apps
flatpak update
```

## run

```shell
flatpak run "com.spotify.Client"

# exec into the container running an app
flatpak run --command=bash com.valvesoftware.Steam
```

## kill

```shell
flatpak kill "com.valvesoftware.Steam"
```

## override

- Set filesystem permission for an app

```shell
# application type
flatpak override com.foo.Bar --user
flatpak override com.foo.Bar --system # required to run as root
flatpak override com.foo.Bar # same as system

# show overrides
flatpak override --show com.foo.Bar

# filesystem permission
flatpak override --filesystem "/give/permission/to/dir/" com.foo.Bar

# reset existing overrides
flatpak override --reset com.foo.Bar

# set environment variable
flatpak override --env=VARIABLE_NAME=VARIABLE_VALUE com.foo.Bar
```
