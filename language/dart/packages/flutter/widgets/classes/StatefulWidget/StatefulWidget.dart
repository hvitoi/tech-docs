import 'package:flutter/widgets.dart';

class MyWidget extends StatefulWidget {
  String _message = "hello";

  MyWidget({Key? key}) : super(key: key);

  @override // attach the StatefulWidget to its State
  State<MyWidget> createState() => _MyWidgetState();
}

/**
 * - State build-in properties
 * - `widget`: reference to the properties of the StatefulWidget
 * - `context`: reference to the context of the StatefulWidget
 */

class _MyWidgetState extends State<MyWidget> {
  void doSomething() {
    // setState forces the build method to be rerun
    setState(() {
      widget._message = "in a bottle"; // property from MyWidget
    });
  }

  @override
  Widget build(BuildContext context) {
    return Text(widget._message);
  }
}
