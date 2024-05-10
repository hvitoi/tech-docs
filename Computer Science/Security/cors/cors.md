# Cross Origin Resource Sharing (CORS)

- The CORS policy is implemented at backend API
- It blocks by default all requests coming from cross-origins (different origins)
  - `Origin`: Protocol + Host + Port. e.g.,: <http://myhost.com:80>
- In order to allow some requests from cross-origins in your API, these origins must be explicitly allowed in the cors policy

## AJAX

- HTTP client from browsers (e.g., `XMLHttpRequest`, `FetchAPI`)
- Load the content of an URL without accessing it via address bar
- The AJAX request must obey the CORS policies

## Preflight Request

- The browser will perform a `preflight request` to the target origin in order to check if it allows CORS.
- It's a `OPTIONS` request with `Host` (target origin) and `Origin` (source origin)
- The target origin responds with the allowed methods
- Preflight Request -> Preflight Response -> Request -> Response
- Preflight Response
  - `Access-Control-Allow-Origin: http://www.source-origin.com`
  - `Access-Control-Allow-Methods: GET, PUT, DELETE`
