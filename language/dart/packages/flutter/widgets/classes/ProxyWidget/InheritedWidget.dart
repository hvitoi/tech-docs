import 'package:flutter/widgets.dart';

/**
 * Propagate information down the widget tree
 * It's commonly used to encapsulated the MaterialApp
 */

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final MyDependencies deps = MyDependencies.of(context);

    return MyDependencies(
      name: "Henry", // initialize MyDependencies with values
      child: Text(deps.name),
    );
  }
}

class MyDependencies extends InheritedWidget {
  final String name;

  const MyDependencies({
    Key? key,
    required this.name,
    required Widget child,
  }) : super(key: key, child: child);

  // Method to access the information from the InheritedWidget
  static MyDependencies of(BuildContext context) {
    final MyDependencies? result =
        context.dependOnInheritedWidgetOfExactType<MyDependencies>();
    assert(result != null, 'No MyDependencies found in context');
    return result!;
  }

  // notify every time "name" is changed
  @override
  bool updateShouldNotify(MyDependencies old) => name != old.name;
}
