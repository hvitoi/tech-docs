# CORS (Cross-Origin Resource Sharing)

- CORS refers to the situations when a frontend running in a browser has JavaScript code that communicates with a backend, and the backend is in a different "origin" than the frontend
- `Origin`: Protocol + Host + Port. e.g.,: <http://myhost.com:80>

- The CORS policy is implemented at backend API
- It blocks by default all requests coming from cross-origins (different origins)
- In order to allow some requests from cross-origins in your API, these origins must be explicitly allowed in the cors policy

## AJAX

- HTTP client from browsers (e.g., `XMLHttpRequest`, `FetchAPI`)
- Load the content of an URL without accessing it via address bar
- The AJAX request must obey the CORS policies

## Preflight Request

- The browser will perform a `preflight request` to the target origin (an http server) in order to check if it allows CORS.
- It's a `OPTIONS` request with `Host` (target origin) and `Origin` (source origin)
- The target origin responds with the `allowed methods` and the `allowed origins`
- Preflight Request -> Preflight Response -> Request -> Response

```http
# Preflight Request

OPTIONS / HTTP/1.1
Origin: http://myhost.com
Access-Control-Request-Method: GET
```

```http
# Preflight Response

HTTP/1.1 200 OK
Access-Control-Allow-Methods: DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT
Access-Control-Max-Age: 600
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: http://myhost.com
```
