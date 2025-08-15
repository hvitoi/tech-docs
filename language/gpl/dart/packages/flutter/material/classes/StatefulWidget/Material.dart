import 'package:flutter/material.dart';

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
