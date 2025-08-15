# Java CLI

```shell
# Java version
java -version

# Run a compiled code
java "Main" # set the current folder as the classpath
cd "~/Documents"; java "Main" # if the compiled binary is in another folder

# Set system property
java -D"key"="value" "Main"
java -Dfile.encoding=UTF-8 "Main"
java -Dserver.port "Main"

# Set classpath
java -cp "~/Documents" -D"name"="value" "Main"

# Run jar file
java -jar "avro-tools-1.10.2.jar"

# Debug mode
java -agentlib:jdwp=transport=dt_socket,server=n,suspend=y,address=localhost:38585 "Main"

# Compile and run source code
# You must first cd into the directory where the code is located
java "Main.java"
```
