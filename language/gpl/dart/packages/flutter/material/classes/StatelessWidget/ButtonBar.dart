import 'package:flutter/material.dart';

Widget main() {
  return ButtonBar(
    alignment: MainAxisAlignment.center,
    children: [
      TextButton(onPressed: () {}, child: Text("a")),
      TextButton(onPressed: () {}, child: Text("b")),
      TextButton(onPressed: () {}, child: Text("c")),
    ],
  );
}
