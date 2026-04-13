# GitHub App

- Recommended one for services/bots
- A GitHub App is its own identity, it acts as itself (e.g., @my-bot[bot]), not as a user.
- Installation token

## Step 0: Create App

- Create it at <https://github.com/settings/apps>
- After the app is created you can
  - Manage it: <https://github.com/settings/apps/my-app>
  - See it: <https://github.com/apps/my-app>

- Params
  - `Client secrets`: for the OAuth user-to-server flow (the app acts on behalf of an user authorized via browser)
  - `Private key (.pem)`: for server-to-server auth. The bot acts on behalf of itself (@my-app[bot])

## Step 1: Install App

- Go to its public page and install it: <https://github.com/apps/my-app>
- It will prompt:
  - On which account you want to install: `personal account` or `organization`
  - The `repositories` and other resources that you want to grant access to
- You can then manage the installation: <https://github.com/settings/installations/123456789>

## Step 1: Generate JWT

- Generate a JWT from the app's private key (valid for up to 10 minutes)

```shell
# requires: openssl
APP_ID="3363276"
pem_file="private-key.pem"

b64url() { openssl base64 -e -A | tr '+/' '-_' | tr -d '='; }

header=$(echo -n '{"alg":"RS256","typ":"JWT"}' | b64url)
now=$(date +%s)
payload=$(printf '{"iat":%d,"exp":%d,"iss":"%s"}' $((now - 60)) $((now + 600)) "$APP_ID" | b64url)
signature=$(echo -n "${header}.${payload}" | openssl dgst -sha256 -sign "$pem_file" | b64url)

jwt="${header}.${payload}.${signature}"
```

## Step 2: Generate access token

- Find the installation ID and exchange the JWT for an installation access token
- You can use the App Access Token just like a `PAT` (however it expires in 1 hour)

```shell
# list app installations to get the installation ID
curl -Lsf \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $jwt" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/app/installations


# create an installation token
INSTALLATION_ID=123587880
curl -Lsf -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $jwt" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/app/installations/$INSTALLATION_ID/access_tokens

# returns: {"token":"ghs_xxxx","expires_at":"...","permissions":{...}}

GH_ACCESS_TOKEN= # ghs_xxxx
```

## Step 3: use the installation token to call the API (acts as the app bot)

```shell
curl -Lsf \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GH_ACCESS_TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/hvitoi/tech-docs/pulls
```
