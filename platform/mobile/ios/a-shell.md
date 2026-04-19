# a-shell

- scp, curl, vim, ed, grep, awk, sed
- nslookup, ping, whois, ifconfig

## Home directory

- In iOS, you cannot write in the home directory (`~`)
- However, you can write to only in `~/Documents/`, `~/Library/` and `~/tmp`

### Changing the home directory

- The home directory is located at `/private/var/mobile/Containers/Data/Application/<uuid>`
- Where uuid (`25A07DC9-ED08-4394-BC82-9F3E1D5A6602F`) is the uuid of the a-shell app

### Shared Directory

- You can change the home directory by using ability to access directories in other Apps sandbox

```shell
pickFolder
```

- This will open for you the folder `/private/var/mobile/Containers/Shared/AppGroup/<uuid>/File Provider Storage/`
- Where uuid is the id of the App that owns that folder

## Git

- `lg2` (git replacement) <https://libgit2.org/>

```shell
ssh-keygen -t ed25519 # key is saved to ~/Documents/.ssh/
ssh -T git@github.com # test connection

# Configure (it's required since the path to ssh isn't ~/.ssh/)
lg2 config —-global user.name "<your name>"
lg2 config —-global user.email "<your email>"
lg2 config —-global user.identityFile "~/Documents/.ssh/<private key filename>"

# Use
lg2 clone https://github.com/hvitoi/foo.git
```
