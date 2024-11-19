# Proxy

- A proxy is an intermediary server that sits between a client (e.g., a browser) and a destination server
- It forwards requests from the client to the server and then sends the server's response back to the client
- Proxies are used for various purposes, including security, anonymity, and caching.

## Forward Proxy

- Acts on behalf of the client
- The client sends requests to the proxy, which forwards them to another server
- Often used to:
  - Hide the client’s IP address
  - Enforce corporate internet policies
  - Cache frequently accessed resources for faster retrieval

- `Client` -> `Forward Proxy` -> `Server`

## Reverse Proxy

- Acts on behalf of the server
- A `rever proxy` is proxy server that appears to any client to be an ordinary web server, but in reality merely acts as an intermediary that forwards the client's requests to one or more ordinary web servers
- The client sends requests to the reverse proxy, which forwards them to one or more backend servers
- Often used for:
  - `Load balancing`: Distributing traffic across multiple servers
  - `SSL termination`: Handling HTTPS encryption/decryption
  - `Caching`: Storing responses for faster delivery
  - `Security`: Protecting backend servers by hiding their identity and filtering malicious requests.
  - Centralized authentication and logging

- `Client` -> `Reverse Proxy` -> `Server(s)`

## Nginx

- `Nginx` (pronounced "engine-x") is a `web server` and `reverse proxy server`
- **Features**
  - `Reverse Proxy`: Routes incoming requests to backend servers and provides features like load balancing and SSL termination.
  - `Web Server`: Serves static content (HTML, CSS, JavaScript, etc.) and processes HTTP/HTTPS requests.
  - `Load Balancer`: Distributes traffic across multiple backend servers to ensure high availability and scalability.
  - `Content Caching`: Caches frequently accessed content for faster response times.
  - `HTTP/2 and gRPC Support`: Offers modern protocol support for improved performance.
  - `Security`: Includes features like rate limiting, IP whitelisting/blacklisting, and integration with firewalls.

```conf
server {
    listen 80;

    server_name example.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
