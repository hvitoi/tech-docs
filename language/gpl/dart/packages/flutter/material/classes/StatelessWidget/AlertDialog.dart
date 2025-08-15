import 'package:flutter/material.dart';

Widget main() {
  return AlertDialog(
    title: Text('hello'),
    content: TextField(),
    actions: [
      TextButton(
        onPressed: () {},
        child: Text('Cancel'),
      ),
      TextButton(
        onPressed: () {
          // Navigator.pop()...
        },
        child: Text('Confirm'),
      )
    ],
  );
}
