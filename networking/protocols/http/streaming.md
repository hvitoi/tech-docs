# Streaming

- In HTTP, when you make a request, the server can send the response `all at once` or in a `streamed/chunked way`
- This concept is similar to what you have with database cursors
- While streaming, your `HTTP connection stays open`
  - The server keeps the connection open while sending data in chunks.
  - When the server finishes sending all data, it closes the connection (or signals the end of the stream, e.g., with a zero-length chunk in HTTP/1.1).

```http
> GET /streaming/mystream HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/8.7.1
> accept: application/json

< HTTP/1.1 200 OK
< date: Sun, 17 Aug 2025 02:56:00 GMT
< server: uvicorn
< content-type: application/x-ndjson
< x-process-time: 0.000737959002435673
< transfer-encoding: chunked
```

- HTTP streaming responses typically use the header `Transfer-Encoding: chunked`
- Content-Type
  - `application/x-ndjson`
  - `text/event-stream`: server-side events

## Streaming formats

- The key is that the format must allow `partial consumption`, you shouldn't need the whole file or array in memory to process the first piece.

### JSON Lines (NDJSON)

- Each record is a separate line.
- Easy to parse as it arrives.
- Example: logs, telemetry, large datasets.

```json
{"a":1}
{"b":2}
{"c":3}
```

### CSV / TSV

- Each row can be processed immediately.
- Often used for bulk exports or analytics data.

```csv
id,name\n1,Alice\n2,Bob\n
```

### Binary formats with framing

- Examples: Protocol Buffers (with length-prefix), Avro, MessagePack.
- Efficient for large datasets; you can deserialize records as they stream in.

### Media / large files

- Audio (.mp3, .wav), video (.mp4, .mkv), images.
- Typically streamed as raw bytes or in chunks over HTTP.

### Server-Sent Events (SSE) or WebSockets messages

- For continuous updates or real-time feeds.
- Each message is discrete and can be handled as it arrives.
