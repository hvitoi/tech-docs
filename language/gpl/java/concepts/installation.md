# Java

- Java binaries are installed at:
  - Compiler: `/usr/lib/jvm/default/bin/javac`
  - Runtime: `/usr/lib/jvm/default/bin/java` (or default-runtime)
- Alternatively you can invoke the symlink `/usr/bin/java`

## Brew (MacOS)

- openjdk is `keg-only`

```shell
brew install openjdk
sudo ln -sfn \
  /opt/homebrew/opt/openjdk/libexec/openjdk.jdk \
  /Library/Java/JavaVirtualMachines/openjdk.jdk
```

## Pacman (Archlinux)

- Packages
  - `jdk-openjdk`
  - `openjdk-doc`
  - `openjdk-src`

```shell
pacman -S "jdk11-openjdk" "openjdk11-doc" "openjdk11-src"
```

```shell
# Show installed JDKs
archlinux-java status

# Show default JDK
archlinux-java get

# Change default JDK
archlinux-java set "java-17-openjdk" # create symlink /usr/lib/jvm/default -> /usr/lib/jvm/java-17-openjdk
```

## Apt (Debian)

```shell
# Show java locations
sudo update-java-alternatives -l

## If not, java must be using another jdk, then:
sudo update-alternatives --config java # Java executor
sudo update-alternatives --config javac # Java compiler
```

## Setup Java Home

- There's no need to set JAVA_HOME if the binaries are already in your `$PATH`

```shell
sudo vim "/etc/environment"
JAVA_HOME="/usr/lib/jvm/default"
JAVA_HOME="/usr/lib/jvm/java-11-amazon-corretto"
JAVA_HOME="/usr/lib/jvm/java-16-openjdk"
source "/etc/environment" # update the current terminal
echo "$JAVA_HOME"

# Or...
export JAVA_HOME=$(readlink -f /usr/bin/javac | sed "s:/bin/javac::")
```
