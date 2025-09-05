# HTTP Status Codes

## 100 - 199

- Used for "Information". You rarely use them directly.
- Responses with these status codes cannot have a body

## 200 - 299

- Used for "Successful" responses.
- 200 is the default status code, which means everything was "OK".
- 201, "Created". It is commonly used after creating a new record in the database.
- A special case is 204, "No Content". This response is used when there is no content to return to the client, and so the response must not have a body.

## 300 - 399

- Used for "Redirection".
- Responses with these status codes may or may not have a body, except for 304, "Not Modified", which must not have one

## 400 - 499

- Used for "Client error" responses.
- 404, for a "Not Found" response.
- For generic errors from the client, you can just use 400.

## 500 - 599

- Used for server errors.
- When something goes wrong at some part in your application code, or server, it will automatically return one of these status codes
