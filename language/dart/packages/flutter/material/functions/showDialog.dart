import 'package:flutter/material.dart';

class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return IconButton(
      icon: const Icon(Icons.add),
      onPressed: () {
        showDialog(
          context: context,
          builder: (ctxDialog) {
            return SimpleDialog();
            // return AlertDialog();
          },
        ).then((value) => null); // what to do when it's closed
      },
    );
  }
}
