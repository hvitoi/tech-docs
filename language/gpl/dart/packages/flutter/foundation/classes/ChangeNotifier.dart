import 'package:flutter/material.dart';

/**
 * A "ChangeNotifier" monitors changes in the attributes
 */

class Counter extends ChangeNotifier {
  int value = 0;

  void increment() {
    this.value++;
    notifyListeners(); // tells to other widgets that this value has changed
  }
}
