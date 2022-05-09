import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

/**
 * Defines a "provider", which is the store with a set of values being monitored
 * Theses notifiers are initialized once (singleton) and reused/consumed when needed
 */

void main() {
  runApp(ChangeNotifierProvider(
    create: (context) => Counter(), // notifiers to be monitored
    child: MaterialApp(), // entrypoint widget
  ));
}

class Counter extends ChangeNotifier {
  int value = 0;

  void increment() {
    this.value++;
    notifyListeners(); // similar to "setState()"
  }
}
