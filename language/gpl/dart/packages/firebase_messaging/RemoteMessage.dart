import 'package:firebase_messaging/firebase_messaging.dart';

void main() async {
  FirebaseMessaging messaging = FirebaseMessaging.instance;
  RemoteMessage message = (await messaging.getInitialMessage())!;

  // notification
  RemoteNotification notification = (message.notification)!;
  notification.title;
  notification.body;

  // data
  Map<String, dynamic> data = message.data; // additional key-value pairs
}
