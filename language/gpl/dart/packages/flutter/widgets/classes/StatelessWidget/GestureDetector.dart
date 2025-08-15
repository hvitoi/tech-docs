import 'package:flutter/widgets.dart';

/**
 * Has the ability to wrap a widget that has no event detectors
 */

Widget main() {
  return GestureDetector(
    onTap: () {
      print("a");
    },
    child: Text("a"),
  );
}
