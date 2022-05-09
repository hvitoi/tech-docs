# gRPC

- `RPC` (Remote Procedure Call): Execute a function in the destination target

## HTTP/2

- `gRPC` uses HTTP/2 (launched in 2015)
- Uses the same TCP connection (multiplex), instead of opening multiple requests
- Data flow as binaries, instead of text
- Headers are compressed

## Protobuf

- `Protocol Buffers (Protobuf)`: Mechanism for serializing structured data to a binary data

## gRPS connection types

- `Unary`: Client (Request) - Server (Response)
- `Server streaming`: Client (Request) - Server (Multiple responses)
- `Client streaming`: Client (Multiple request) - Server (Reponse)
- `Bidirectional streaming`: Client (Multiple request) - Server (Multiple response)

## Advantages & Disavantages

- `Advantages`
  - Type safety
  - Transmits binary data
  - Auto-generation of client code for most languages
- `Disadvantages`
  - No curl-like tool for ad hoc testing
  - Will not work with some cloud load balancers
  - More complicated than TCP or Redis
  - Data not human readable
- `It's most helpful when...`
  - Used by client from different programming languages
  - You have a lot of MSs with several methods
  - You are transmitting large amount of data

## Using gRPC with javascript

- Requires the lib `@grpc/proto-loader`
