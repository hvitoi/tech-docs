import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

/**
 * A MultiProvider accepts multiple providers
 */

void main() {
  runApp(MultiProvider(
    child: MaterialApp(),
    providers: [
      ChangeNotifierProvider(create: (providerContext) => Counter()),
      ChangeNotifierProvider(create: (providerContext) => ReverseCounter())
    ],
  ));
}

class Counter extends ChangeNotifier {
  int value = 0;

  void increment() {
    this.value++;
    notifyListeners();
  }
}

class ReverseCounter extends ChangeNotifier {
  int value = 0;

  void decrement() {
    this.value--;
    notifyListeners();
  }
}
