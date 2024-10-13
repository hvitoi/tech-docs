# gpg

- GnuPG allows you to encrypt and sign your data and communications using public key cryptography
- It is based on the original PGP (`Pretty Good Privacy`) software
- GnuPG (also known as `GPG`) is a command line tool with features for easy integration with other applications

## Create

```shell
# generate gpg key (secret + public)
gpg --full-generate-key

# don't ask for PIN
gpg --full-generate-key --pinentry-mode=loopback
```

- This creates
  - `~/.gnupg/trustdb.gpg` (trustdb)
  - `~/.gnupg/pubring.kbx` (keybox)
  - `~/.gnupg/openpgp-revocs.d/<pub_id>.rev` (revocation certificate)

- In order to use the gpg key for git commit signature (without having to specify the id manually), the real name and email must match exactly.

## List

```shell
# list keys
gpg --list-keys # public keys
gpg --list-secret-keys # secret keys
gpg --list-secret-keys --keyid-format "LONG" # GPG key id are the last 16 hex digits (sec)
```

## Edit

```shell
# edit key
gpg --edit-key "0123456789ABCDEF"
  # gpg> help --> show all commands
  # gpg> list --> list all user IDs
  # gpg> adduid --> add a user ID (name + email + comment)
  # gpg> deluid --> delete selected user IDs (select with "uid 1")
  # gpg> save --> save and quit
```

## Remove

```shell
gpg --delete-secret-keys "key-id"
gpg --delete-keys "key-id"
```

## Import/Export

```shell
# import public key (to encrypt messages to others and verify their signatures)
gpg --import "public.key"
curl -sS "https://download.spotify.com/debian/pubkey_0D811D58.gpg" | gpg --import -

# Import keys from a server
gpg \
  --recv-keys 38DBBDC86092693E \
  --keyserver keyserver.ubuntu.com
```

## Export

- You can export the following files to another machine:
  - `~/.gnupg/private-keys-v1.d/*`: dir 700 permission, files 600 permission
  - `~/.gnupg/pubring.kbx`: file 644 permission

```shell
# ascii armored output
gpg --armor --export "0123456789ABCDEF" # print public key
gpg --armor --export-secret-key "0123456789ABCDEF" # print secret key
```

## Verify signature

```shell
# verify signature
gpg \
  --verify "archlinux-version-x86_64.iso.sig" \
  --keyserver-options "auto-key-retrieve"
```

## Encrypt content

```shell
gpg -c file.txt
```

## Decrypt content

- Try to decrypt using your `GPG secret key`
- A prompt will open to ask for the password

```shell
gpg -d "topsecret.gpg"
```
