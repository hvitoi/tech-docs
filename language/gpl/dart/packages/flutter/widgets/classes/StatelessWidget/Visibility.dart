import 'package:flutter/widgets.dart';

/**
 * Configures wether another widget is visible or not
 */

Widget main() {
  return Visibility(
    visible: (() => true)(),
    child: Text("hello"),
  );
}
