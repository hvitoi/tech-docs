# Web API

- Requires the oauth token, which is a long-lived token.
  - Request an oauth token, by installing it on Slack <https://api.slack.com/apps/A0AD0RYKZH8/install-on-team>
  - If you have disabled incoming webhooks, it will not ask you for a channel, just the org name

- Tokens
  - `xoxp-...`: user token. The user must have joined the channel
  - `xoxb-...`: bot token. Type `/invite @YourBotName` to invite it first

## /auth.test

```shell
curl https://slack.com/api/auth.test \
  -H "Authorization: Bearer xoxb-xxxxxxxxx-xxxx"

```

## /conversations.list

- List all channels
- In Slack, messages inhabit conversations. A conversation is a catch-all term that covers `public channels`, `private channels`, `direct message conversations`, and `group` (or multi-party) direct message conversations.

```shell
curl -X POST https://slack.com/api/conversations.list \
  -H "Authorization: Bearer $SLACK_API_KEY"
```

## /chat.postMessage

- <https://slack.com/api/chat.postMessage>
- If there are links, Slack will cache the preview (`unfurl`) once at post time. It's not possible to refresh it afterwards, even when a message is updated

```shell
# With plain text or markdown text
curl -X POST "https://slack.com/api/chat.postMessage" \
  -H "Authorization: Bearer $SLACK_API_KEY" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
        "channel": "C0AHXKUJJ6S",
        "text": "Hey!",
        "markdown_text": "**Hey!**", # formatting is different
        "thread_ts": "1770298071.095679", # post it as "sub-message" in a slack thread
      }'

# With blocks
curl -X POST "https://slack.com/api/chat.postMessage" \
  -H "Authorization: Bearer $SLACK_API_KEY" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
        "channel": "C0AHXKUJJ6S",
        "blocks": [{
          "type": "section",
          "text": {
            "type": "mrkdwn",
            "text": "**Hey!**"
          }
        }]
      }'
```

```json
// Response
{
  "ok": true,
  "channel": "C0AHXKUJJ6S",
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

## /chat.update

```shell
# Update text
curl -X POST https://slack.com/api/chat.update \
  -H "Authorization: Bearer $SLACK_API_KEY"
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
        "channel": "C0AHXKUJJ6S",
        "ts": "1770300403.519119",
        "text": "Updated message text"
      }'

# Update block (Updating a block doesn't mark the message as "edited")
curl -X POST https://slack.com/api/chat.update \
  -H "Authorization: Bearer $SLACK_API_KEY" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
        "channel": "C0AHXKUJJ6S",
        "ts": "1772538556.786139",
        "blocks": [{
          "type": "section",
          "text": {
            "type": "mrkdwn",
            "text": "**Hey!!!**"
          }
        }]
      }'
```

## /chat.delete

```shell
curl -X POST https://slack.com/api/chat.delete \
  -H "Authorization: Bearer $SLACK_API_KEY"
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
        "channel": "C0AHXKUJJ6S",
        "text": "Hey!",
        "ts": "1770298071.095679",
      }'
```
