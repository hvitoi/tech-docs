import 'package:flutter/material.dart';

/**
 * - Styled Container widget
 * - Has shadow, background, padding, etc...
 * - By default `assumes the size of its child` or the `size defined by the parent`
 */

Widget main() {
  return Card(
    elevation: 6, // more shadow for the card
    color: Colors.blue,
    margin: EdgeInsets.all(20),
    child: Text('hey'),
  );
}
