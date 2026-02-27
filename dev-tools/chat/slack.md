# slack

## Slack Apps

- Your apps (bot): <https://api.slack.com/apps>
- Slack Platform documentation: <https://docs.slack.dev/>

## APIs

### Incoming Webhooks

- It's the simplest way to interact with Slack
- You [install the and on a channel](https://api.slack.com/apps/<app-id>/install-on-team) and it will generate a URL for you
- You get an unique URL per channel (for the channel you installed onto) that allows you to post messages (and only it! Very limited) no oauth required
- You can disable incoming webhooks on <https://api.slack.com/apps/A0AD0RYKZH8/incoming-webhooks>

```shell
curl -X POST https://hooks.slack.com/services/T.../B.../... \
 -H 'Content-type: application/json' \
 -d '{
        "text": "Hello, world."
     }'
```

### Socket Mode

...

### Events API

...

### Web API

- Requires the oauth token, which is a long-lived token.
  - Request an oauth token, by installing it on Slack <https://api.slack.com/apps/A0AD0RYKZH8/install-on-team>
  - If you have disabled incoming webhooks, it will not ask you for a channel, just the org name

- Tokens
  - `xoxp-...`: user token. The user must have joined the channel
  - `xoxb-...`: bot token. Type `/invite @YourBotName` to invite it first

#### /auth.test

```shell
curl https://slack.com/api/auth.test \
  -H "Authorization: Bearer xoxb-xxxxxxxxx-xxxx"

```

#### /conversations.list

- List all channels
- In Slack, messages inhabit conversations. A conversation is a catch-all term that covers `public channels`, `private channels`, `direct message conversations`, and `group` (or multi-party) direct message conversations.

```shell
curl -X POST https://slack.com/api/conversations.list \
  -H "Authorization: Bearer xoxb-xxxxxxxxx-xxxx"
```

#### /chat.postMessage

- <https://slack.com/api/chat.postMessage>

```shell
curl -X POST "https://slack.com/api/chat.postMessage" \
  -H "Authorization: Bearer xoxb-xxxxxxxxx-xxxx" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
        "channel": "C062TK76L0Z",
        "text": "Hey!",
        "markdown_text": "**Hey!**", # formatting is different
        "blocks": [{
          "type": "section",
          "text": {
            "type": "mrkdwn",
            "text": "**Hey!**"
          }
        }],
        "thread_ts": "1770298071.095679", # post it as "sub-message" in a slack thread
      }'
```

```json
// Response
{
  "ok": true,
  "channel": "C062TK76L0Z",
  "ts": "1770298071.095679",
  "message": {
    "user": "U0ACKHDLC87",
    "type": "message",
    "ts": "1770298071.095679",
    "bot_id": "B0ADV9KKK4G",
    "app_id": "A0AD0RYKZH8",
    "text": "I hope the tour went well, Mr. Wonka.",
    "team": "T024U97V8",
    "bot_profile": {
      "id": "B0ADV9KKK4G",
      "app_id": "A0AD0RYKZH8",
      "user_id": "U0ACKHDLC87",
      "name": "Marinator",
      "icons": {
        "image_36": "https://avatars.slack-edge.com/2026-02-04/10442885988642_67e5c0f6179cb3506ccd_36.png",
        "image_48": "https://avatars.slack-edge.com/2026-02-04/10442885988642_67e5c0f6179cb3506ccd_48.png",
        "image_72": "https://avatars.slack-edge.com/2026-02-04/10442885988642_67e5c0f6179cb3506ccd_72.png"
      },
      "deleted": false,
      "updated": 1770296570,
      "team_id": "T024U97V8"
    },
    "blocks": [
      {
        "type": "rich_text",
        "block_id": "P49cp",
        "elements": [
          {
            "type": "rich_text_section",
            "elements": [
              {
                "type": "text",
                "text": "I hope the tour went well, Mr. Wonka."
              }
            ]
          }
        ]
      }
    ]
  },
  "warning": "missing_charset",
  "response_metadata": {
    "warnings": [
      "missing_charset"
    ]
  }
}
```

#### /chat.update

```shell
curl -X POST https://slack.com/api/chat.update \
  -H "Authorization: Bearer xoxb-xxxxxxxxx-xxxx"
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
        "channel": "C062TK76L0Z",
        "ts": "1770300403.519119",
        "text": "Updated message text"
      }'
```

#### /chat.delete

```shell
curl -X POST https://slack.com/api/chat.delete \
  -H "Authorization: Bearer xoxb-xxxxxxxxx-xxxx"
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
        "channel": "C062TK76L0Z",
        "text": "Hey!",
        "ts": "1770298071.095679",
      }'
```
