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

...
