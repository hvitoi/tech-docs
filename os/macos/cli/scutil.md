# scutil

- Access/modify config store

## get

```shell
scutil --get HostName
scutil --get LocalHostName
scutil --get ComputerName
```

## set

```shell
# primary hostname - fully qualified hostname e.g., mymac.domain.com
scutil --set HostName "new-hostname"

# bonjour hostname - usable only on the local network e.g., my-mac.local
scutil --set LocalHostName "new-hostname"

# computer name
scutil --set ComputerName "new-name"
```

## dns

- Also: `cat /etc/resolv.conf`

```shell
# show DNS resolver servers
scutil --dns
```
