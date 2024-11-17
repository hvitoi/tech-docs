# ssh

- Secure connection between computers
- Key-pairs are generated at user level (`~/.ssh`)
  - `id_rsa`: secret file and never share
  - `id_rsa.pub`: share with github, heroku, etc
- Private key files should have 400 permissions

```shell
ssh "user@hostname"
ssh "root@192.168.1.10"
```

## -T

- Test connection

```shell
ssh -T "git@github.com" # Accept 'yes'
```

## -l (Login name / User)

- Specify user
- You can also use the syntax `user@host`

```shell
ssh "192.168.1.10" -l "root"
```

## -p (Port)

- Specify port

```shell
ssh "root@localhost" -p "9090"
```

## -i (Identity file)

- Specify the private key

```shell
ssh "root@localhost" -i "private_key"
```

## -L

- Port tunnel

```shell
ssh "root@localhost" -L # or -D and -R
```

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
