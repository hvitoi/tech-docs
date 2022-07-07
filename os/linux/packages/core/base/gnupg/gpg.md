# gpg

- GnuPG allows you to encrypt and sign your data and communications using public key cryptography
- It is based on the original PGP (`Pretty Good Privacy`) software
- GnuPG (also known as `GPG`) is a command line tool with features for easy integration with other applications

## GPG keys

```shell
# generate gpg key (secret + public)
gpg --full-generate-key # gpg: key 0123456789ABCDEF marked as ultimately trusted. This is the gpg id of the secret key

# list keys
gpg --list-keys # public keys
gpg --list-secret-keys # secret keys
gpg --list-secret-keys --keyid-format "LONG" # show GPG key id (last hex digits)

# edit key
gpg --edit-key "0123456789ABCDEF"
  # gpg> help --> show all commands
  # gpg> list --> list all user IDs
  # gpg> adduid --> add a user ID
  # gpg> deluid --> delete selected user IDs (select with "uid 1")
  # gpg> save --> save and quit
```

## Import/Export

```shell
# ascii armored output
gpg --armor --export "0123456789ABCDEF" # print public key
gpg --armor --export-secret-key "0123456789ABCDEF" # print secret key

# import public key (to encrypt messages to others and verify their signatures)
gpg --import "public.key"
curl -sS "https://download.spotify.com/debian/pubkey_0D811D58.gpg" | gpg --import -
```

## Verify signature

```shell
# verify signature
gpg \
  --verify "archlinux-version-x86_64.iso.sig" \
  --keyserver-options "auto-key-retrieve"
```

## Decrypt content

- Try to decrypt using your `GPG secret key`
- A prompt will open to ask for the password

```shell
gpg -d "topsecret.gpg"
```
