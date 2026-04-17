# Client Credentials

- Used by clients to obtain an access token outside of the context of the user (no user login prompt)
- Only used by confidential clients (client must run in the backend)

## Get access token

- `resource` specifies domain for the protected resource (access token will be valid only for this resource)

```shell
curl -X POST https://authorization-server.com/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded; charset=utf-8" \
  -H "Accept: application/json" \
  -d "grant_type=client_credentials
     &client_id=client-id
     &client_secret=client-secret
     &resource=https://resource-server.com"
```

```json
// The access token is valid only for the resource specified in the request

{
  "token_type": "bearer",
  "expires_in": "3600",
  "access_token": "12345678abcdef"
}
```

## Get resource

```shell
curl -X GET https://resource-server.com/file.txt \
  -H "Authorization: Bearer $TOKEN"
```
