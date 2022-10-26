# pass

- Pass - The Standard Unix Password Manager
- Each password lives inside of a `gpg encrypted file` whose `filename is the title of the website or resource` that requires the password
- Plugins
  - `passff`: firefox plugin
  - `qtpass`: desktop GUI

```sh
# list all passwords
pass

# decrypt a password
pass "facebook.com"
gpg -d "~/.password-store/topsecret.gpg" # using gpg directly
```

## init

```sh
# create a gpg secret key
gpg --full-generate-key # gpg: key 0123456789ABCDEF marked as ultimately trusted

# initialize password store with the gpg id
pass init "0123456789ABCDEF"

# initialize password store with the gpg email
pass init "user@mail.com"
```

## insert

- Insert a password into the store
- Uses the gpg public key to encrypt it

- Stores password files at `~/.password-store`
- Each password is a .gpg file. E.g., `facebook.com.pgp`
- `.gpg-id` is your gpg id of your secret key

```sh
pass insert "facebook.com"
```

## rm

```sh
pass rm "facebook.com"
```

## ls

```sh
# list all passwords
pass ls
```
