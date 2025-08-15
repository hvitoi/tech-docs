import 'package:flutter/widgets.dart';

/**
 * - Scrollable content
 * - Can be used for the broad `Scaffold` widget itself
 * - Can be used for subwidgets (e.g., `Container`) inside the app
 * - Alternatively use a `ListView`!
*/

Widget main() {
  return SingleChildScrollView(
    scrollDirection: Axis.horizontal, // vertical by default
    child: Text("hello"),
  );
}
