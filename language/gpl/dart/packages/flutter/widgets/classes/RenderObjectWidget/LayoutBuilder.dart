import 'package:flutter/widgets.dart';

Widget main() {
  return LayoutBuilder(
    // constraints: define how a widget is rendered on the screen
    builder: (BuildContext ctx, BoxConstraints constraints) {
      return Container(
        height: constraints.maxHeight,
        child: Text('hello'),
      );
    },
  );
}
