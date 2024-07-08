# ssh

- Secure connection between computers

## SSH server

- In a VM, the bridge mode must be enabled to use SSH
- `/etc/ssh/sshd_config`: Configuration file for a ssh server
- `~/.ssh/authorized_keys/`: Stores public keys of the allowed clients

```shell
# Install ssh-server
apt install openssh-server

# Check ssh service
systemctl status ssh
ps -ef | grep sshd # /usr/sbin/sshd

# Get ip of the machine
ip addr # enp0s3 (192.168.0.109)

# Test connection to itself
ssh localhost
```

## SSH client

- Keys are generated at user level (`~/.ssh`)
- `id_rsa`: secret file and never share
- `id_rsa.pub`: share with github, heroku, etc

```shell
# Test connection
ssh -T "git@github.com" # Accept 'yes'

# Conventional ssh
ssh "user@hostname"
ssh "root@192.168.1.10"

# Specify user
ssh "192.168.1.10" -l "root"

# Specify port
ssh "root@localhost" -p "9090"

# Specify key
ssh "root@localhost" -i "private_key"

# Port tunnel
ssh "root@localhost" -L # or -D and -R
```
