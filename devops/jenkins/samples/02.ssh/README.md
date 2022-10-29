# Run a script in a remote machine via ssh

## SSH server

```sh
# Generate keys to access the SSH server
ssh-keygen -m "PEM" -f "./ubuntu/ubuntu-key"
```

```Dockerfile
FROM ubuntu:latest
RUN apt update && apt install -y "openssh-server" "sudo"
RUN useradd -rm -d "/home/ubuntu" -s "/bin/bash" -g "root" -G "sudo" -u "1000" "ubuntu"
RUN echo "ubuntu:123" | chpasswd
RUN mkdir -p "/home/ubuntu/.ssh" && chmod "700" "/home/ubuntu/.ssh"
COPY "ubuntu-key.pub" "/home/ubuntu/.ssh/authorized_keys"
RUN chown "ubuntu:root" -R "/home/ubuntu/.ssh" && chmod "600" "/home/ubuntu/.ssh/authorized_keys"
RUN service ssh start
CMD /usr/sbin/sshd -D
EXPOSE 22
```

```yml
version: "3"
services:
  jenkins:
    container_name: jenkins
    image: jenkins/jenkins
    ports:
      - "8080:8080"
    volumes:
      - "$HOME/jenkins_home:/var/jenkins_home"
    networks:
      - net
  ubuntu:
    image: ubuntu-ssh
    build:
      context: .
    ports:
      - "22:22"
networks:
  net: {}
```

- Test connection (Jenkins -> Ubuntu)

```sh
# Copy the ssh key to jenkins
docker container cp "./ubuntu/ubuntu-key" "jenkins:/tmp/ubuntu-key"
ssh "ubuntu@remote-host" # Access via SSH (with password)
ssh "ubuntu@remote-host" -i "/tmp/ubuntu-key"  # Access via SSH (with ssh key)
```

## SSH Plugin

- Need to install the jenkins plugin SSH
- `Dashboard` / `Manage Jenkins` `Manage Plugins`
  - Search for `SSH`: This plugin executes shell commands remotely using SSH protocol.
  - Install and restart jenkins (or install without restart and then restart manually)
  - After that, it will appear under the `Installed` tab

## Configure credentials in Jenkins

- `Dashboard` / `Manage Jenkins` / `Manage Credentials`
  - `Jenkins Scope` / `Global credentials (unrestricted)` / `Add Credential`
- Enter SSH username with private key
  - Username: remote host
  - Private key: ------BEGIN RSA PRIVATE KEY------ ...

### Test SSH connection in Jenkins

- `Dashboard` / `Manage Jenkins` / `Configure System` / `SSH remote hosts`
  - Hostname: remote-host
  - Port: 22
  - Creatials: (previously created)
- Check connection!

## Run jobs on remote host

- `Dashboard` / `New Item` / `Freestyle project`
  - `Build` / `Execute shell script on remote host using ssh`
- The script will be executed in the host server via SSH
