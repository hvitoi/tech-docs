# run

- `Compiles` and `Runs` the flutter code in an `Android`/`iOS` emulator currently running

```shell
# run in the first active device
flutter run

# some parameters
flutter run \
  --flavor "mycustombuild" \
  --device-id "iPhone 8" \
  --no-pub

# run in a web browser (this opens a http server which you can access via localhost:xxxxx)
flutter run -d "web-server"
```

- `flavor` specifies the flavor of the app
  - It build a custom app depending on platform-specific build setup
  - Supports the use of product flavors in Android Gradle scripts, and the use of custom Xcode schemes
