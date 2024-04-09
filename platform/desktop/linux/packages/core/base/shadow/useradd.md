# useradd

```shell
useradd "user" # If no group is specified, it's added to a group with the same name

useradd \
  -g "group" \
  -s "/bin/bash" \
  -c "description" \
  -d "/home/user" \
  -m \
  "user"
# g - add user to a group
# s - shell
# c - description
# d - home directory
# m - create the home directory

useradd \
  -rm \
  -d /home/ubuntu \
  -s /bin/bash \
  -g root \
  -G sudo \
  -u 1000 \
  hvitoi
```

## /etc/passwd

- Where all login data of users is stored
- This file is readable to all users but can only be modified by the root user

- **user name**
  - user name
- **user-password**
  - `x` means the password is encrypted and stored at /etc/shadow
- **user id** (uid)
  - root (0), system accounts (< 500), normal user (> 500), first user (1000)
- **group-id** (gid)
  - ID of the user's primary group
- **description**
  - A comments (also known as GECOS). E.g, first and last name, email, telephone number, etc
- **home dir**
  - home directory path
  - /root for root user
- **shell**
  - shell to be launched at login
  - if this points to a shell that does not exist, the user won't be able to log in

```txt
awesome:x:1000:1000::/home/awesome:/bin/zsh
```

## /etc/shadow

- Stores encrypted user passwords

- **Username**
  - Name to be used for login
- **Encrypted password**
  - The encrypted password has for format `$id$salt$hashed`
  - The id can be:
    - `$1$`: encrypted using MD5 algorithm
    - `$2a$`: encrypted using Blowfish algorithm
    - `$2y$`: encrypted using Blowfish algorithm
    - `$5$`: encrypted using SHA-256 algorithm
    - `$6$`: encrypted using SHA-512 algorithm
- **Password last changed**
  - Date when the password was last changed (unix epoch)
- **Minimum password age**
  - The minimum number of days that must pass before the password can be changed
- **Maximum password age**
  - The maximum number of days for which the password is valid
- **Warning period**
  - The number of days before password expiration that the user is warned about the upcoming expiration
- **Inactive period**
  - The number of days after password expiration that account will be disabled
- **Account expiration**
  - The date (unix epoch) on which the account will expire and the user will no longer able to log in
- **Reserved for future**
  - ...

```txt
root:*:14871::::::
awesome:blablabla:15326:0:99999:7:::
```

## Linux Account Authentication

- **Types of accounts**

  - Local account
  - Domain/Directory account

- **Directory Service**

  - _Microsoft_
    - Directory service:`Active Directory`
    - Login protocol: `LDAP`
  - _RHEL_
    - Directory Service: `IDM` (Identity Manager)
  - _IBM_
    - IBM Directory Server
  - _Cloud_
    - JumpCloud

- **Login Protocols** (used to authenticate against a directory)
  - `LDAP` (Lightweight Directory Access Protocol): Used mostly on Windows
  - `WinBIND`: Windows users (AD) access their account in Linux machines (SAMBA)
  - `OpenLDAP` - Open authentication protocol: Used mostly on Linux. `slapd` service

### OpenLDAP server

- Service for configuring the OpenLDAP server: `slapd`
- Configuration folder `/etc/openldap/slapd.d/`
- `/etc/nsswitch.conf` shows the options to choose for account management
  - Checks the field `passwd: files sss`
  - `sss` is the ldap server, it's the second option after a user is not found locally

```shell
# Install
sudo apt install *openldap*

# Service
systemctl status slapd
ps -ef | grep slapd
```
