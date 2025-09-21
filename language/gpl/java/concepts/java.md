# Java

## JDK, JRE, JVM

- `JDK`
  - Create java programs. Takes the source code and convert executable format
  - Debuggers
  - Java compiler (creates the .class files)
  - Comes with the JRE in it
- `JRE`
  - Run java program
  - Libraries
  - Java launcher (the JVM)
- `JVM`:
  - It's a part of the JRE
  - It's a machine that only runs java code
  - The JVM and be created in many different operating systems
  - Java JDK doesn't compile the code for the OS but for the JVM
  - It makes java a little slower than the other languages

## JAR

- `Java Archive`: it's similar to a zip, but with extension .jar
- Stores your compiled code (not the source code)

### META-INF

- The `main` method must be specified on jar creation in order to make it executable
- The `META-INF` folder contains a file called `MANIFEST.MF` which points to the Main-Class (that contains the main method)
