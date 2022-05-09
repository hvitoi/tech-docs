# Variables

## Type

```csharp
var name = "Henrique";  // "var" infers the variable type.

var age = 10;
Console.WriteLine(age); // automatic casting to string
Console.WriteLine(age.ToString()); // manual casting to string

var (name, prince, total) = ("pizza dough", 1.99m, 3); // m defines a decimal
```

## Strings

```csharp
var name = "Henrique";
Console.WriteLine(name.ToUpper());
```

## Dates

```csharp
var date = DateTime.UtcNow;
Console.WriteLine(
  $"On {date.ToLongDateString()} at {date.ToShortTimeString()}"
);
```

## List

```csharp
var names = new[] { "Ana", "Henrique", "Alice" };
foreach (var name in names)
{
  Console.WriteLine($"Hello {name}!");
}
```

```csharp
var names = new List<string>();
names.Add("Henrique");
names.Add("Erica");
```

```csharp
var names = new[] { "Ana", "Henrique", null, "Alice" };
names
  .Where(name => name?.Length >5) // filter
  .OrderBy(name => name) // order alphabetically
  .ToList()
  .ForEach(Console.WriteLine)
```
