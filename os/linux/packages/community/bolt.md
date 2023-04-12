# bolt

## boltctl

```shell
# List
boltctl list # list thunderbolt peripherals
boltctl list --all # list all (peripherals & host)

# Authorize
boltctl authorize <uuid>
boltctl authorize <uuid> --chain

# Enroll
boltctl authorize <uuid> # authorize and save to db
boltctl authorize <uuid> --chain

```
