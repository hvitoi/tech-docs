import 'package:flutter/material.dart';

/**
 * Usually inside of Scaffold
*/

Widget main() {
  return AppBar(
    // backgroundColor: Theme.of(context).primaryColor,
    title: const Text("Personal Expenses"), // title in the app bar
    actions: <Widget>[
      IconButton(onPressed: () {}, icon: const Icon(Icons.add)),
    ],
  );
}
