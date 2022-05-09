import 'package:firebase_messaging/firebase_messaging.dart';

void main() {
  /**
   * Static
   */
  FirebaseMessagingInstance();
  FirebaseMessagingOnMessage();
  FirebaseMessagingOnBackgroundMessage();

  /**
   * Instance
   */
  FirebaseMessagingGetToken();
  FirebaseMessagingRequestPermission();
  FirebaseMessagingGetInitialMessage();
}

void FirebaseMessagingInstance() {
  FirebaseMessaging messaging = FirebaseMessaging.instance;
}

void FirebaseMessagingOnMessage() async {
  // Register callback handlers for foreground messages
  FirebaseMessaging.onMessage.listen((RemoteMessage message) {
    RemoteNotification? notification = message.notification; // notification
    Map<String, dynamic> data = message.data; // additional data
  });
}

void FirebaseMessagingOnBackgroundMessage() async {
  // Register callback handlers for background messages
  FirebaseMessaging.onBackgroundMessage((RemoteMessage message) async {
    RemoteNotification? notification = message.notification; // notification
    Map<String, dynamic> data = message.data; // additional data
  });
}

void FirebaseMessagingGetToken() async {
  FirebaseMessaging messaging = FirebaseMessaging.instance;

  // The token uniquely identifies the device
  // Get this token (and cache it) and send to the backoffice at the application startup (main)
  // This way the backoffice will be able to tell FCM to send notification to a specific device
  String? token = await messaging.getToken();

  // Retrieve a token for webapps (you must provide the web push certificate)
  String? token2 = await messaging.getToken(vapidKey: 'webpushcertificate');
}

void FirebaseMessagingRequestPermission() async {
  FirebaseMessaging messaging = FirebaseMessaging.instance;

  // Notification permissions
  NotificationSettings settings = await messaging.requestPermission(
    alert: true,
    announcement: true,
    badge: true, // the "+1"  when you didn't open the notification yet
    carPlay: true,
    criticalAlert: true,
    provisional: true,
    sound: true, // whether the notification is silent
  );
  if (settings.authorizationStatus == AuthorizationStatus.authorized) {
    print('Permission granted permanently.');
    String? token = await messaging.getToken();
    // Get unique token that identifies the device
    // You must send it to the backoffice after getting it
  } else if (settings.authorizationStatus == AuthorizationStatus.provisional) {
    print('Permission granted only this time.');
    String? token = await messaging.getToken();
  } else {
    print('Permission denied.');
  }
}

void FirebaseMessagingGetInitialMessage() async {
  FirebaseMessaging messaging = FirebaseMessaging.instance;

  // represents the message used to open the app (if any)
  // it can be used to do something when the application is started by a click on a push notification
  RemoteMessage? message = await messaging.getInitialMessage();
  if (message is RemoteMessage) {
    print("I was opened by a click in the notification!");
  }
}
