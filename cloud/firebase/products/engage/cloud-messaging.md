# Firebase Cloud Messaging (FCM)

- Used to **send/receive** messages to peer devices (iOS, Android, Web)
- Messages can be addressed to single devices, groups of devices or topics
- The mobile device app instance register itself with the `firebase cloud messaging server`
- On your backoffice, you submit a request to `firebase cloud messaging server` to send the desired message to a target

## Message types

- Send `push notifications` to devices
- Send `data` to devices. E.g., posts, comments

## Token

- The message can be redirected to a specific device using a `token`
- The token is assigned to a device at the application startup
- Ideally the token must be cached in the device's internal storage

## Permissions

- The device must have permissions to receive notifications (must be allowed in the device)

## App State

- **Foreground**
  - App is open
  - Normally the notification is not received (because it's already open)
- **Background**
  - App is minimized
  - Notification is delivered
- **Terminated**
  - App is closed

## FCM Console

- It's possible to send messages directly from Google Firebase Console (without an internal backoffice)
- Access your firebase project in the firebase console and find it under `Cloud Messaging` tab

- **Notification**

  - Title
  - Text
  - Image (optional)
  - Name (optional)

- **Target**

  - User segment
  - Topic
  - Groups

- **Scheduling**

  - Now
  - Tomorrow
  - ...

- **Conversion events** (optional)

  - Send notification upon an event (`goal metric`)
  - E.g., first_open, in_app_purchase, etc
  - Add Analytics label for metrics

- **Additional options** (optional)

  - Additional key-value pairs (`RemoteMessage.data` field)
  - Sound: true/false
  - Expire date (after which it won't be delivered anymore)
