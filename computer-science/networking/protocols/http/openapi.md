# OpenAPI

- `OpenAPI` (previously known as `Swagger`) is the open specification for building APIs (now part of the Linux Foundation).

## Security Schemes

- OpenAPI has a way to define multiple security "schemes"

### apiKey

- An application specific key that can come from:
  - A query parameter
  - A header
  - A cookie

### http

- Standard HTTP authentication systems, including:
  - Bearer: a header Authorization with a value of Bearer plus a token. This is inherited from OAuth2.
  - HTTP Basic authentication.
  - HTTP Digest, etc.

### oauth2

- All the OAuth2 ways to handle security (called "flows")
- Several of these flows are appropriate for building an OAuth 2.0 authentication provider (like Google, Facebook, Twitter, GitHub, etc):
  - implicit
  - clientCredentials
  - authorizationCode
  - password

### openIdConnect

- has a way to define how to discover OAuth2 authentication data automatically
- This automatic discovery is what is defined in the OpenID Connect specification.
