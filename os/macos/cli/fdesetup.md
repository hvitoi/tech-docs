# fdesetup

- Configure FileVault

## list

- Lists all the crypto users
- Also shown using `diskutil apfs listCryptoUsers diskX`

```shell
sudo fdesetup list -extended
```

## haspersonalrecoverykey

- Checks whether it's using a PRK

```shell

fdesetup haspersonalrecoverykey
```

## hasinstitutionalrecoverykey

- Checks whether it's using a IRK

```shell
fdesetup hasinstitutionalrecoverykey
```

## changerecovery

- Change PRK

```shell
fdesetup changerecovery -personal
```

- It will prompt for the user name and password
- For user name, you can user both the name itself or the uuid
- You can also use the current PRK, in this case use the PRK's uuid as the user name
