# Base64

- It's a `binary-to-text encoding scheme`
- Takes binary data (like bytes, images, PDFs).
- Converts it into text made of only 64 characters: `A–Z`, `a–z`, `0–9`, `+`, `/` (and `=` as padding)
- To safely transmit binary data through systems that only handle text (like JSON, XML, HTTP headers, email)
