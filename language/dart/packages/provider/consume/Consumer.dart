import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';

/**
 * Consume value from the store
 * It's used when a widget needs to "subscribe" to a value and refresh when the state changes
 */

class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Consumer<Counter>(builder: (consumerCtx, obj, child) {
      // "obj" is the instance of the class to be retrieved
      obj.increment(); // invoke methods that change the state
      return Text(obj.value.toString());
    });
  }
}

class Counter extends ChangeNotifier {
  int value = 0;

  void increment() {
    this.value++;
    notifyListeners(); // tells to other widgets that this value has changed
  }
}
