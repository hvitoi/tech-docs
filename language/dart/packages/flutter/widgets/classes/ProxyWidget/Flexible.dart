import 'package:flutter/widgets.dart';

/**
 * Force the child to use the available space and can't grow
*/

Widget main() {
  return Flexible(
    flex:
        1, // by default every item has the same space (1), you can change it for individual items using the flex property (e.g., 2)
    fit: FlexFit
        .tight, // loose (default): child takes the necessary space, tight: child takes all the remaining space
    child: Text('hey'),
  );
}
