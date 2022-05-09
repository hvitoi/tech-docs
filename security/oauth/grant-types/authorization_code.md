# Authorization Code

- Optimized for confidential clients

## Get authorization code (public)

- Requested by frontend application
- Sends a request to the to the `authorization server`, where the resource owner will enter its credentials

- `response_type`: must be "code". Means that client is performing an **Oauth 2.0 Authorization Code Workflow**. Returns the authorization code to the redirect uri
- `redirect_uri`: where to send the code to
- `client_id`: public identifier of the application
- `scope`: which permissions the application is requesting
- `state`: random string (prevent CSRF attacks)

```http
GET https://authorization-server.com/oauth2/authorize?
    response_type=code&
    client_id=client-id&
    scope=email+offline_access&
    redirect_uri=https://client.com/callback/
```

- The `authorization code` is sent back to the `redirect_url` (which is part of the application). E.g., <https://client.com/callback?code=12345>

## Get access token (confidential)

- Requested by backend application
- The client uses the code received from the authorization server to get an access token
- The authorization server `authenticates the client`, `validates the authorization code` and `verify the redirection uri`

```http
POST https://authorization-server.com/oauth2/token HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Accept: application/json

&grant_type=authorization_code
&redirect_uri=https://client.com/callback/&
&code=12345
```

```json
{
  "token_type": "bearer",
  "expires_in": "3600",
  "access_token": "123456abcdef",
  "refresh_token": "abcdef123456" // optional
}
```

## Get resource

```http
GET https://resource-server.com/file.txt HTTP/1.1
Authorization: Bearer bearer-token
```
