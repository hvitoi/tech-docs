# help

- Documentation: </cli>
- Binary: </jnlpJars/jenkins-cli.jar>
- Credentials configuration: </me/configure>

## HTTP connection mode

```shell
# username + password
java -jar "jenkins-cli.jar" \
  -s "http://localhost:8080" \
  -http -auth "admin:123" \
  help

# username + token
java -jar "jenkins-cli.jar" \
  -s "http://localhost:8080" \
  -http -auth "admin:abc1234ffe4a" \
  help

# credentials file
java -jar "jenkins-cli.jar" \
  -s "http://localhost:8080" \
  -http -auth "@/home/hvitoi/.jenkins-cli" \
  help

# bearer token
java -jar "jenkins-cli.jar" \
  -s "http://localhost:8080" \
  -http -bearer "my-token" \
  help
```

- Instead of defining `-auth` param, you can set it as environment variables

```shell
export JENKINS_USER_ID=admin
export JENKINS_API_TOKEN=abc1234ffe4a
java -jar "jenkins-cli.jar" "http://localhost:8080" help
```

## WebSocket connection mode

- Avoid problems with many reverse proxies or the need for special proxy configuration
  SSH connection mode

```shell
java -jar "jenkins-cli.jar" \
  -s "http://localhost:8080" \
  -webSocket -auth "admin:123" \
  help
```

## SSH connection mode

- Authentication via SSH keypair
- Acts like a native ssh command

```shell
java -jar "jenkins-cli.jar" \
  -s "http://localhost:8080" \
  -ssh -user "admin" \
  help
```

## Alias

```shell
echo "alias jenkinscli=\"java -jar ~/bin/jenkins-cli.jar -s http://localhost:8080 -webSocket -auth admin:123\"" >> ~/.zshrc
```
