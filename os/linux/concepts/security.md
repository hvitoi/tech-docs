# Linux OS Hardening

- Password policy (`/etc/shadow`, `/etc/login.defs`, `/etc/pam.d/system-auth`)
- Enable firewall (iptables/firewalld)
  - `firewall-cmd --help` and `/etc/firewalld` directory
- Enable SELinux
  - Secure Enhanced Linux. Uses the linux security module (LSM)
  - Establish the access and permission rights for every user, app, processes, etc
  - `sestatus`
  - `/etc/sysconfig/selinux` configuration file
