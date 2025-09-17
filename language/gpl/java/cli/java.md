# Java CLI

## -version

```shell
# Java version
java -version
```

## -

- You must be in the directory of the file/class which you want to run in order to run it
- It sets the current directory as the `classpath`

```shell
# Compile and run source code
cd ./Documents; java "Main.java"

# Run a compiled code
cd "~/Documents"; java "Main"
```

## -D

- Set system property

```shell
java -D"key"="value" "Main"
java -Dfile.encoding=UTF-8 "Main"
java -Dserver.port "Main"
```

## -cp

- Set classpath

```shell
java -cp "~/Documents" "Main"
```

## -jar

- Run jar file

```shell
java -jar "avro-tools-1.10.2.jar"
```

## -agentlib

- Debug mode

```shell
java -agentlib:jdwp=transport=dt_socket,server=n,suspend=y,address=localhost:38585 "Main"
```
