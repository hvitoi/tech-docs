import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter/material.dart';

void main() async {
  // Ensure app is completely initialized
  WidgetsFlutterBinding.ensureInitialized();

  // Firebase project
  await Firebase.initializeApp();

  // FCM config
  messagingConfig();

  // Run App
  runApp(const MaterialApp());
}

void messagingConfig() async {
  // FCM instance
  FirebaseMessaging messaging = FirebaseMessaging.instance;

  // Notification permissions
  NotificationSettings settings = await messaging.requestPermission(
    alert: true,
    announcement: true,
    badge: true,
    carPlay: true,
    criticalAlert: true,
    provisional: true,
    sound: true,
  );

  // Get the token conditionally
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

  // Register callback handlers for the messages
  FirebaseMessaging.onMessage.listen((RemoteMessage message) {
    Map<String, dynamic> data = message.data; // message data
    RemoteNotification? notification = message.notification; // notification
  });
}
