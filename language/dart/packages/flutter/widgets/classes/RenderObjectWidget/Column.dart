import 'package:flutter/widgets.dart';

/*
  - Allow multiple nested widgets
  - Arrange them vertically
  - Has the width of its widest child
  - Offers alignment, but not styling
  - Axis
    - `Main Axis`: vertical
    - `Cross Axis`: horizontal
*/

Widget main() {
  return Column(
    mainAxisAlignment: MainAxisAlignment.center, // default is "start"
    crossAxisAlignment: CrossAxisAlignment.stretch, // default is "start"
    children: <Widget>[
      Text("hey"),
      Text("hello"),
    ],
  );
}
