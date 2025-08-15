import 'dart:async';

import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_crashlytics/firebase_crashlytics.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

void main() {
  /**
   * Static
   */
  FirebaseCrashlyticsInstance();

  FirebaseCrashlyticsRecordFlutterError();
  FirebaseCrashlyticsCrash();

  FirebaseCrashlyticsRecordError();
  FirebaseCrashlyticsSetCustomKey();
  FirebaseCrashlyticsSetUserIdentifier();

  FirebaseCrashlyticsSetCrashlyticsCollectionEnabled();
  FirebaseCrashlyticsIsCrashlyticsCollectionEnabled();
}

void FirebaseCrashlyticsInstance() {
  FirebaseCrashlytics fcl = FirebaseCrashlytics.instance;
}

void FirebaseCrashlyticsRecordFlutterError() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  FirebaseCrashlytics fcl = FirebaseCrashlytics.instance;

  // Pass all uncaught errors from the framework to Crashlytics.
  // override FlutterError.onError to automatically catch all errors that are thrown within the Flutter framework
  FlutterError.onError = fcl.recordFlutterError;

  // use it to detect low level errors (on the dart language)
  runZonedGuarded<Future<void>>(() async {
    runApp(MaterialApp());
  }, fcl.recordError);
}

void FirebaseCrashlyticsCrash() {
  FirebaseCrashlytics fcl = FirebaseCrashlytics.instance;

  // force an exception (crash)
  fcl.crash();
}

void FirebaseCrashlyticsRecordError() {
  FirebaseCrashlytics fcl = FirebaseCrashlytics.instance;

  try {
    throw Exception();
  } catch (e) {
    // send exception to google firebase servers
    fcl.recordError(e, null);
  }
}

void FirebaseCrashlyticsSetCustomKey() {
  FirebaseCrashlytics fcl = FirebaseCrashlytics.instance;

  try {
    throw Exception();
  } catch (e) {
    // set custom keys before sending the crash
    fcl.setCustomKey('exception', e.toString());
    fcl.setCustomKey('req_body', '{"a":1}');

    fcl.recordError(e, null);
  }
}

void FirebaseCrashlyticsSetUserIdentifier() {
  FirebaseCrashlytics fcl = FirebaseCrashlytics.instance;

  try {
    throw Exception();
  } catch (e) {
    // set user identifier before sending the crash
    fcl.setUserIdentifier('user123');

    fcl.recordError(e, null);
  }
}

void FirebaseCrashlyticsSetCrashlyticsCollectionEnabled() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  FirebaseCrashlytics fcl = FirebaseCrashlytics.instance;

  if (kDebugMode) {
    // if it's a dev environment ...
    await fcl.setCrashlyticsCollectionEnabled(false);
  } else {
    await fcl.setCrashlyticsCollectionEnabled(true);
    FlutterError.onError = fcl.recordFlutterError;
  }

  runApp(MaterialApp());
}

void FirebaseCrashlyticsIsCrashlyticsCollectionEnabled() {
  FirebaseCrashlytics fcl = FirebaseCrashlytics.instance;

  // send crash only if the collection is enabled (by setCrashlyticsCollectionEnabled)
  if (fcl.isCrashlyticsCollectionEnabled) {
    fcl.recordError(Exception(), null);
  }
}
