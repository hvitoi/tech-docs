import 'package:flutter/material.dart';

/**
 * - A Column wrapped with a SingleChildScrollView
 * - A Column with infinite height
 *    - Therefore it must be wrapped inside a Container or SizedBox with height
 *    - Otherwise flutter doesn't know how to size it
 */

Widget main() {
  return ListView(
    scrollDirection: Axis.horizontal, // vertical by default
    padding: const EdgeInsets.all(8),
    children: <Widget>[
      Container(
        height: 50,
        color: Colors.amber[600],
        child: const Center(child: Text('Entry A')),
      ),
      Container(
        height: 50,
        color: Colors.amber[500],
        child: const Center(child: Text('Entry B')),
      ),
      Container(
        height: 50,
        color: Colors.amber[100],
        child: const Center(child: Text('Entry C')),
      ),
    ],
  );
}

/**
 * BUILDER
 */

// - Lazy loads the elements of the list (good for very long lists)
// - Loads the elements as they become visible in the screen

Widget mainBuilder() {
  List<String> list = ["a", "b", "c"];
  return ListView.builder(
    itemCount: list.length < 10 ? list.length : 10, // execute itemBuild n times
    itemBuilder: (ListViewContext, i) => Text(list[i]),
    shrinkWrap: true,
    padding: EdgeInsets.all(8),
  );
}
