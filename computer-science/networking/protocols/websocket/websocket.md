# WebSocket

- `Normal HTTP`: A client makes a request → server sends a response → connection closes.
- `WebSocket`: After an HTTP handshake, the connection upgrades to a WebSocket and stays open. Both client and server can now send messages anytime (`full-duplex communication`).

- So instead of repeated requests (polling), you get a persistent, low-latency channel.

## Flow

1. Client asks the server: `Upgrade: websocket`
2. Server agrees and switches protocols
3. From then on, client and server exchange frames (messages) freely

Request

```http
GET /ws HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: <random>
Sec-WebSocket-Version: 13
```

Response

```http
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: <derived from client key>
```

## Protocol

- WebSocket is a protocol, standardized by RFC 6455
  - It defines how a client and server establish a connection (the HTTP upgrade handshake).
  - It defines how data is framed (text or binary messages broken into frames).
  - It defines control frames (like ping, pong, close).
  - It defines full-duplex communication over a single TCP connection.

- `wss://`
- `ws://`
