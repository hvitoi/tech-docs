# OAuth App

- <https://github.com/settings/developers>
- Designed for third-party web apps that need to act on behalf of a user after they log in
- Works with browser login
- Token acts as the user who authorized it

Step 1: redirect the user to GitHub's authorization page:

```txt
https://github.com/login/oauth/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_CALLBACK_URL&scope=repo,read:user
```

Step 2: user authorizes, GitHub redirects back with a `code` to the callback URL. The user uses the code to exchange it for an access token:

```shell
curl -Lsf -X POST \
  -H "Accept: application/json" \
  https://github.com/login/oauth/access_token \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET" \
  -d "code=THE_CODE_FROM_CALLBACK"

# returns: {"access_token":"gho_xxxx","token_type":"bearer","scope":"repo,read:user"}
```

Step 3: use the token (acts as the user who authorized it):

```shell
curl -Lsf \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer gho_xxxx" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/user
```
