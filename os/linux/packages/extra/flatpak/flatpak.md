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
```

## run

```shell
flatpak run "com.spotify.Client"
```

## override

- Set filesystem permission for an app

```shell
flatpak override \
  --user \
  --filesystem "/path/to/mounted/drive" \
  "com.valvesoftware.Steam"
```
