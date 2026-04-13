# Implicit Flow

- Deprecated! Use authorization_code with PKCE instead
- Used for applications that have no server-side component and runs completely on the browser (single-page applications)
- Similar to authorization_code, but in this case an access token is provided directly (instead of a authorization code)

## Get access token (public)

- Query parameters:
  - `response_type`: must be "token". Tells the authorization server to initiate the implicit flow
  - `redirect_uri`: where to send the access token to
  - `client_id`: public identifier of the application
  - `scope`: which permissions the application is requesting
  - `state`: random string (prevent CSRF attacks)

```shell
curl -X GET "https://authorization-server.com/oauth2/authorize
  ?response_type=token
  &client_id=client-id
  &redirect_uri=https://client.com/callback/"
```

- The `access token` is sent back to the `redirect_url` (which is part of the application). E.g., <https://client.com/callback#access_token=12345&token_type=example&expires_in=3600>
- The fragment (#) stays on the browser and cannot be get by an backend application

## Get resource

```shell
curl -X GET https://resource-server.com/file.txt \
  -H "Authorization: Bearer $TOKEN"
```
