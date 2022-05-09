# new

```sh
# List template projects
dotnet new --list

# Create dotnet console project
dotnet new "template-name" # create in the current folder (using project name inherited from the folder name)
dotnet new "template-name" --name "project-name" # create subfolder
dotnet new "console" --name "console-project"
dotnet new "webapp" --name "webapp-project"

# .gitignore
dotnet new "gitignore"
```

- `bin/` and `obj/` folders can be safely removed
