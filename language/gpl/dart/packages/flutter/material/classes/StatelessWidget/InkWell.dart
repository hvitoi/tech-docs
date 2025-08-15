import 'package:flutter/material.dart';

/**
 * Usually wrapped with a "Material" widget
 */

Widget main() {
  return Material(
    color: Colors.red,
    child: InkWell(
      onTap: () {
        print("a");
      },
      child: Text("a"),
    ),
  );
}
