# run

- Run a .NET project or builded project
- To run web apps, dotnet uses the `Kestrel Web Server` for local development
  - Kestrel web server must not be used for production
- Builded applications are located at `bin/Release/net5.0/publish/app.dll`

```shell
# Run (build & execute) current project
dotnet run
```

```shell
# Run builded project
dotnet "awesome-app.dll"
```
