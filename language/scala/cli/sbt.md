# sbt

```shell
# Open sbt server with interactive prompt
sbt
```

## tasks

- List of tasks defined for the current project

```shell
sbt tasks
```

## run

```shell
# Build & Run the main class
sbt run
```

## clean

- Delete generated files in `target` directory

```shell
sbt clean
```

## compile

- Compile sources:
  - `src/main/scala`
  - `src/main/java`

```shell
sbt compile
```

## package

- Creates `jar` for:
  - `src/main/resources` (files)
  - `src/main/scala` (compiled classes)
  - `src/main/java` (compiled classes)

```shell
sbt package
```
