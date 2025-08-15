import 'package:flutter/widgets.dart';

/**
 * Force the box into its available space
 * If it's too large, it's shrunk
 * Prevents overflowing elements
 */

Widget main() {
  return FittedBox(
    child: Text('hello'),
  );
}
