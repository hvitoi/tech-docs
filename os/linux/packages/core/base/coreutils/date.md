# date

- Usually combined with scripts

```shell
# Show current date
date
```

## Input date

```shell
date -d '2023-12-31T12:00:00.000Z'
date -u -d '2023-12-31T12:00:00.000Z' # Output as UTC
```

## Format date

```shell
# json with minutes and hours
date +'{"hour":"%H","min":"%M"}'

# unix epoch
date +'%s'
```

## Set system date

```shell
date -s "12 Mar 2018 13:20:00"
```
