# Proof Key for Code Exchange (PKCE)

- It's an extension to the oauth authorization_code flow
- Prevent vulnerabilities where a wrong client receives the authorization code
- PKCE binds the authorization code to the initial client that requested it
- Used for `public clients`

## Get authorization code (public)

- Client generates a `code_verifier` (string of 43-128 characters)
- Client uses that code_verifier to generate a `code_challenge` (S256 or PLAIN)
  - S256: code_challenge = SHA256(code_verifier)
  - PLAIN: code_challenge = code_verifier
- Client includes the `code_challenge` and the `code_challenge_method` in the request

```http
GET https://authorization-server.com/oauth2/authorize?
    response_type=code&
    client_id=client-id&
    scope=email+offline_access&
    redirect_uri=https://client.com/callback/&
    code_challenge=code-challenge-base64-encoded
    code_challenge_method=S256
```

## Get access token (confidential)

- Client uses the `authorization_code` and the `code_verifier` in order to retrieve an access token

```http
POST https://authorization-server.com/oauth2/token HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Accept: application/json

&grant_type=authorization_code
&code=12345
&code_verifier=code-verifier
&redirect_uri=https://client.com/callback/
```

## Get resource

```http
GET https://resource-server.com/file.txt HTTP/1.1
Authorization: Bearer bearer-token
```
