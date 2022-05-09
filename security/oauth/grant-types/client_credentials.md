# Client Credentials

- Used by clients to obtain an access token outside of the context of the user (no user login prompt)
- Only used by confidential clients (client must run in the backend)

## Get access token

- `resource` specifies domain for the protected resource (access token will be valid only for this resource)

```http
POST https://authorization-server/oauth2/token HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Accept: application/json

&grant_type=client_credentials
&client_id=client-id
&client_secret=client-secret
&resource=https://resource-server.com
```

```json
{
  "token_type": "bearer",
  "expires_in": "3600",
  "access_token": "12345678abcdef"
}
```

## Get resource

```http
GET https://resource-server.com/file.txt HTTP/1.1
Authorization: Bearer bearer-token
```
