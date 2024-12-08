# Simple Email Service

- `Simple Email Service` is a SMTP server

## SMTP Credentials

- Console -> Amazon SES -> SMTP Settings

- The `SMTP credentials` are generated based on an `IAM User`. You need to create an iam user specifically for SES

```shell
# Create SES user
aws iam create-user --user-name ses-smtp-user

# Attach the necessary policies to the user
aws iam attach-user-policy \
    --user-name ses-smtp-user \
    --policy-arn arn:aws:iam::aws:policy/AmazonSESFullAccess

# Generate Access Key
aws iam create-access-key --user-name ses-smtp-user
```

```json
{
  "AccessKey": {
    "UserName": "ses-smtp-user",
    "AccessKeyId": "AKIAEXAMPLE",
    "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "Status": "Active",
    "CreateDate": "2024-12-05T12:00:00Z"
  }
}
```

- The `SMTP user` is the `AccessKeyId`
- The `SMTP password` is derived from the `SecretAccessKey`. You can convert it

```shell
SECRET_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
echo -ne "\x02$(echo -n 'SendRawEmail' | openssl dgst -sha256 -hmac $SECRET_KEY -binary)" | base64
```

## Sending E-Mails

```txt
# email.txt
From: "Your Name" <your_email@example.com>
To: recipient@example.com
Subject: Test Email from SES
MIME-Version: 1.0
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: 7bit

This is a test email sent via AWS SES SMTP using curl.
```

```shell
set smtp_endpoint "smtp://email-smtp.us-east-1.amazonaws.com:587"
curl --url "$smtp_endpoint" \
  --ssl \
  --mail-from "your_email@example.com" \
  --mail-rcpt "recipient@example.com" \
  --upload-file email.txt \
  --user "SMTP_USERNAME:SMTP_PASSWORD"
```

```shell
#!/bin/bash

SMTP_HOST="email-smtp.us-east-1.amazonaws.com"
SMTP_PORT="587"
SMTP_USER="YOUR_SMTP_USERNAME"
SMTP_PASS="YOUR_SMTP_PASSWORD"
FROM="your_email@example.com"
TO="recipient@example.com"
SUBJECT="Test Email from SES"
BODY="This is a test email sent via AWS SES."

echo -e "From: $FROM\nTo: $TO\nSubject: $SUBJECT\n\n$BODY" > email.txt

curl --url "smtp://$SMTP_HOST:$SMTP_PORT" \
  --ssl \
  --mail-from "$FROM" \
  --mail-rcpt "$TO" \
  --upload-file email.txt \
  --user "$SMTP_USER:$SMTP_PASS"
```
