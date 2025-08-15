import 'package:flutter/material.dart';

/**
 * - Position widgets on top of each other
 * - E.g., an image with a text in the foreground
 */

Widget main() {
  return Stack(
    children: <Widget>[
      Container(
        width: 100,
        height: 100,
        color: Colors.red,
      ),
      Container(
        width: 90,
        height: 90,
        color: Colors.green,
      ),
      Container(
        width: 80,
        height: 80,
        color: Colors.blue,
      ),
    ],
  );
}
