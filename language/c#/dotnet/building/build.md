# build

- Builds the project into the `bin` folder
- Each folder in `bin` is a build configuration
- The code to be published is inside of the `publish` folder
- `./bin/Release/net5.0/publish`

```shell
# Build project (inside of the project folder)
dotnet build

# Specify build configuration
dotnet build -c "Release"
```
