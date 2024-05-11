# OAuth 2

- `OAuth 2.0` is the industry-standard protocol for authorization (and authentication)
- `OpenID Connect` is the industry-standard protocol for authentication only
- Gives permissions to the `application object`

## Roles

- `Resource Owner`: entity that owns the data (e.g., a logged user)
- `Resource Server`: server that hosts the protected resource. Access is only granted with the use of access tokens
- `Client`
  - The application that requests a token to the authorization server in behalf of the resource owner
- `Authorization Server`
  - The identity provider, it issues the authorization codes and the access tokens
  - Autorize the client and emit tokens
  - SSO (Single Sign On)
- `Access Token`: security token requested by the client in order to access the resource server

## Clients

- `Confidential Client`
  - Client running in a backend (server)
  - Protects the client_key and client_secret
- `Public Client`
  - Clients that do not have a client_secret
  - Client running in a frontend (browser, mobile)

## Grant Types

- <https://oauth.net/2/grant-types/>
- Each grant type has its own flow to acquire an access token

- `Authorization Code`
- `PKCE`
- `Client Credentials`
- `Device Code`
- `Refresh Token`
- `Implicit Flow` (legacy)
- `Password Grant` (legacy)

## Protocols

- OpenID Connect / OAuth 2.0

  - JSON
  - Simple
  - Bearer token (access token)
  - When to use?
    - Default
    - Single-page
    - Mobile
    - REST Services

- SAML v2
  - XML
  - More mature
  - More complex
  - When to use?
    - Monoliths
    - Apps with SAML support
    - If you have fancy requirements
