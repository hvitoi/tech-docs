# Webhooks

- Allow service to call your Agent and create `incident` investigations
- Uses HMAC authentication
- <https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-invoking-devops-agent-through-webhook.html>

```shell
#!/usr/bin/env bash
set -euo pipefail

WEBHOOK_URL="https://event-ai.us-east-1.api.aws/webhook/generic/<UUID>"
SECRET="..."

TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%S.000Z) # E.g., "2026-04-21T18:05:10.826Z"
INCIDENT_ID="test-alert-$(date +%s)"

PAYLOAD=$(
  cat <<EOF
{
"eventType": "incident",
"action": "created",
"priority": "HIGH",
"incidentId": "$INCIDENT_ID",
"title": "Test Alert",
"description": "Test alert description",
"service": "TestService",
"timestamp": "$TIMESTAMP",
"data": {"investigation_id":"123"}
}
EOF
)

# HMAC-SHA256 over "<timestamp>:<payload>", base64-encoded
SIGNATURE=$(printf '%s' "${TIMESTAMP}:${PAYLOAD}" |
  openssl dgst -sha256 -hmac "$SECRET" -binary |
  base64)

curl -sS -X POST "$WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -H "x-amzn-event-timestamp: $TIMESTAMP" \
  -H "x-amzn-event-signature: $SIGNATURE" \
  -d "$PAYLOAD"
```
