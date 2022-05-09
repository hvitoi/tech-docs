import 'package:flutter/widgets.dart';

/**
 * - Allow multiple nested widgets
 * - Axis
 *    - `Main Axis`: horizontal
 *    - `Cross Axis`: vertical
 */

Widget main() {
  return Row(
    mainAxisAlignment: MainAxisAlignment.center, // default is "start"
    crossAxisAlignment: CrossAxisAlignment.stretch, // default is "start"
    children: [
      Text("hey"),
      Text("hello"),
    ],
  );
}
