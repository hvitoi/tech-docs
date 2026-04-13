# Password Grant

- It's deprecated and unsafe
- The "resource owner" has a trust relation with the "client"
- The client (a web page, for example) gets the user and password (through a form, for example)
- The client uses this user + password to request a token

## Scopes

- Scopes are are normally used to declare specific security permissions
- Scopes are passed as form data in the `scope` key. It's a string separated by spaces

- `users:read` or `users:write` are common examples.
- `instagram_basic` is used by Facebook / Instagram.
- `https://www.googleapis.com/auth/drive` is used by Google.

## Get access token

```shell
curl -X POST https://authorization-server.com/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded; charset=utf-8" \
  -H "Accept: application/json" \
  -d "grant_type=password
     &username=john
     &password=admin
     &scope=users:read users:write"
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

```shell
curl -X GET https://resource-server.com/file.txt \
  -H "Authorization: Bearer $TOKEN"
```
