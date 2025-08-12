# Cookies

## How it works

1. **Server sends a cookie**
    - In an HTTP response, the server includes a Set-Cookie header:
    - This tells the client: "Store a cookie named session_id with value abc123."

```http
HTTP/1.1 200 OK
Content-Type: text/html
Set-Cookie: session_id=abc123; Path=/; HttpOnly
```

1. **Browser stores it**
    - Your browser (or HTTP client library) saves that cookie according to its rules (domain, path, expiry, security flags).

1. **Browser sends it back**
    - On every subsequent request to the same domain and matching path, the browser includes the cookie in the Cookie header

```http
GET /dashboard HTTP/1.1
Host: example.com
Cookie: session_id=abc123
```

1. **Server uses it**
    - The server reads the cookie and uses it fo

## Options

- `Domain` & `Path` decide when the cookie is sent.
- `Expires` & `Max-Age` decide how long it lasts.
- `Secure` means it's only sent over HTTPS.
- `HttpOnly` means JavaScript in the browser can't read it (security against XSS).
- `SameSite` can prevent cross-site request forgery (CSRF).
