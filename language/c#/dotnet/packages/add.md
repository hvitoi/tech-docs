# add

- Add a package and run `dotnet restore` to get that package
- The dependency is added to the `.csproj` file

```sh
# Add package
dotnet add package "package" # latest
dotnet add package "package" --version "version" # specific version
```

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net5.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Azure.Storage.Blobs" Version="12.8.3" />
  </ItemGroup>

</Project>
```

## Packages

```sh
dotnet add package "Azure.Storage.Blobs"
dotnet add package "Azure.Storage.Queues"
dotnet add package "System.Data.SqlClient"
```
