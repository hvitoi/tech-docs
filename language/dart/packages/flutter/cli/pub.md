# pub

## add

- Add a new dependency

```sh
flutter pub add "package-name"
flutter pub add "package-name" --dev # as dev dependency
```

## get

- Download and install dependencies

```sh
flutter pub get
flutter pub get "packages/foo" # get from a subdirectory
```

## global

- Global dependency

```sh
# List all global packages
flutter pub global list

# Make a package executable globally available
flutter pub global activate "derry"

# Run a global package (alternatively export $HOME/.pub-cache/bin to PATH)
flutter pub global run "derry"
```
