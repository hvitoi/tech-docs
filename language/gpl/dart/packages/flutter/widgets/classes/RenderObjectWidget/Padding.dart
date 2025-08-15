import 'package:flutter/material.dart';

/**
 * Avoids using a container just to use padding
 */

Widget main() {
  return Padding(
    padding: const EdgeInsets.all(10), // padding on all sides
    child: Text('hello'),
  );
}
