# Curl

- Similar to `wget`
- Mostly used for REST request

```shell
curl example.com
```

## --request (-X)

- By default `GET` is used

```shell
curl https://httpbin.org/get -X GET
```

## --data (-d)

```shell
# json
curl https://httpbin.org/post \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'

# url-encoded
curl https://wordpress.com/wp.login.php \
  --data "log=admin&pwd=password"

# from file
curl https://httpbin.org/post \
  --request POST \
  --header "Content-Type: application/json" \
  --data @search.json
```

## --header (-H)

- Add headers to the request

```shell
curl https://httpbin.org/post \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

## --silent (-s)

- Silent mode

```shell
curl -s https://httpbin.org/get
```

## --show-error (-S)

- Show error even when -s is used
- On its own, it does nothing. It only matters with -s

```shell
curl -sS https://httpbin.org/get
```

## --remote-name (-O)

- Save file with its original filename

```shell
curl http://mirror.bytemark.co.uk/ubuntu-releases/18.04.4/ubuntu-18.04.4-desktop-amd64.iso -O
```

## --output (-o)

- Save file with a provided filename

```shell
curl example.com -o example.html
```

## --head (-I)

- Show response headers only

```shell
curl -I example.com
```

## --list-only (-l)

- Saves the redirected page
- The http page is redirecting to the https page, so nothing is displayed

```shell
curl -l example.com
```

## --location (-L)

- Follow redirects

```shell
curl -L https://deb.nodesource.com/setup_14.x | bash -
```

## --verbose (-v)

- TLS handshake - Additional information regarding the connection

```shell
curl -v <url>
```
