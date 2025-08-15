import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';

/**
 * Access the provider (store) directly (without subscribing to it)
 */

class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    Counter counter = Provider.of<Counter>(
      context,
      listen: false,
    );
    counter.increment();
    return Text(counter.value.toString());
  }
}

class Counter extends ChangeNotifier {
  int value = 0;

  void increment() {
    this.value++;
    notifyListeners(); // tells to other widgets that this value has changed
  }
}
