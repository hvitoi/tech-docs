import 'package:flutter/widgets.dart';

Widget main() {
  return ConstrainedBox(
    constraints: const BoxConstraints(
      minHeight: 15, // pick from the constraints (e.g., constrainst.maxHeight)
    ),
    child: const Text('hello'),
  );
}
