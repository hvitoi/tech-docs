# Password Grant

- It's deprecated and unsafe
- The "resource owner" has a trust relation with the "client"
- The client gets the user password (through a form, for example)
- The client uses this password to request a token

## Get access token

```http
POST https://authorization-server.com/oauth2/token HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Accept: application/json

&grant_type=password
&username=john
&password=admin
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
