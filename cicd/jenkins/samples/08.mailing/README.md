# Mailing

- Plugin: `mailer`
- Use the AWS SES (Simple E-mail Service) as mail sender

## AWS SES

- Manage Jenkins -> Configure System -> `E-mail notification`
  - `SMTP server`: email-smtp.sa-east-1.amazonaws.com
  - Use SMTP authentication (with credentials created in AWS SES)
    - SMTP Username: AKIAWTUUJNI3GRBLYSVT
    - SMTP Password: BF3YW+JLUfxGpn/ojwFy13x2DV1WXl58czx+/nFhv9ET
  - Use SSL
  - SMTP port 465
  - Reply to: mymail@mail.com
- Configure System Admin email address: Configure System -> Jenkins location

## Gmail

- `SMTP server`: smtp.gmail.com
- Authentication: your email & password
- In gmail settings allow `Less secure apps`
  - <https://myaccount.google.com/lesssecureapps>

## Add notifications to the jobs

- Configure Item
- `Post-build Action`
  - `E-mail notification`
  - Send email for every unstable build
  - Send separate emails to individuals who broke the build
