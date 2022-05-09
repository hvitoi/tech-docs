import 'package:flutter/material.dart';

/**
 * This method return a `Future<DateTime>`
 */

class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return IconButton(
      icon: const Icon(Icons.add),
      onPressed: () {
        showDatePicker(
          context: context,
          initialDate: DateTime.now(),
          firstDate: DateTime(2019),
          lastDate: DateTime.now(),
        );
      },
    );
  }
}
