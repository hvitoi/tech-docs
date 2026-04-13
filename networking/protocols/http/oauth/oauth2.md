# OAuth 2.0

- <https://oauth.net/2>
- `OAuth 2.0` is a specification for authorization (and authentication)
  - `OpenID Connect` is another specification based on OAuth 2.0 used for authentication only
- It Gives permissions to the `application object`

## Roles (Entities)

- `Resource Owner`: entity that owns the data (e.g., a logged user)
- `Resource Server`: server that hosts the protected resource. Access is only granted with the use of access tokens
- `Client`: The application that requests a token to the authorization server in behalf of the resource owner
- `Authorization Server`
  - The identity provider, it issues the authorization codes and the access tokens
  - Autorize the client and emit tokens
  - SSO (Single Sign On)
  - E.g., Azure AD
- `Access Token`: security token requested by the client to the authorization server in order to access the resource server

## Clients

- `Confidential Client`
  - Client running in a backend (server)
  - Protects the client_key and client_secret
- `Public Client`
  - Clients that do not have a client_secret
  - Client running in a frontend (browser, mobile)

## 2LO vs. 3LO

- 3LO (3-Legged OAuth) are flows that involves three parties (the "three legs"):

1. User (Resource Owner)
2. Application (Client)
3. Authorization/Resource Server

- Contrast with 2LO (2-Legged OAuth), where only two parties are involved (the `client` and the `server`). There's no user in the loop.

## Grant Types

- <https://oauth.net/2/grant-types/>
- Each grant type has its own flow to acquire an access token

- `Authorization Code`: client_id + redirect_uri
- `PKCE`
- `Client Credentials`: client-id + client-secret
- `Device Code`
- `Refresh Token`
- `Implicit Flow` (legacy)
- `Password Grant` (legacy)

## Protocols

- **OpenID Connect / OAuth 2.0**
  - JSON
  - Simple
  - Bearer token (access token)
  - When to use?
    - Default
    - Single-page
    - Mobile
    - REST Services

- **SAML v2**
  - XML
  - More mature
  - More complex
  - When to use?
    - Monoliths
    - Apps with SAML support
    - If you have fancy requirements
