import 'package:flutter/material.dart';

/**
 * - A GridView with some styling
 * - Good to be used along with ListView
 */

Widget main() {
  return ListTile(
    // usually an image
    leading: CircleAvatar(
      radius: 30,
      child: Text('aaa'),
    ),

    // title of the item
    title: const Text('ListTile with red background'),
    tileColor: Colors.red,

    // text below the title
    subtitle: Text('my description'),
  );
}
