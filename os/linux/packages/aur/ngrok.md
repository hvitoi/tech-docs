# ngrok

- Expose your localhost
- It's reverse proxy
- Creates a secure tunnel of a public endpoint to a service running in your machine
- Web UI to inspect the requests: <http://localhost:4040>

## Login

```sh
# Login
ngrok authtoken "token"
```

## HTTP services

```sh
# Expose HTTP service
ngrok http "3000" # generates a random URL

# Expose HTTP service with basic auth
ngrok http -auth "username:password" "3000"
```

## TCP services

```sh
# Expose SSH service
ngrok tcp "22"

# Expose Postgres service
ngrok tcp "5432"
```

## Filesystem

```sh
# Expose your filesystem
ngrok http "file:///home/hvitoi/Downloads"
```
