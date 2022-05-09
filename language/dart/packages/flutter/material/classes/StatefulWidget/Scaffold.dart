import 'package:flutter/material.dart';

/**
 * - Background, app bar, etc
 * - It's usually nested in "MaterialApp" or "CupertinoApp"
 * - Adds the "debug" sign at the app
*/

Widget main() {
  return Scaffold(
    appBar: AppBar(title: const Text('Home')),
    body: Text('hey'),
    floatingActionButton: FloatingActionButton(
      onPressed: () {},
      tooltip: 'Increment',
      child: const Icon(Icons.add),
    ),
    floatingActionButtonLocation:
        FloatingActionButtonLocation.centerFloat, // bottom center
  );
}
