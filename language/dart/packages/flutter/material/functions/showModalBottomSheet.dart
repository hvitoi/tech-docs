import 'package:flutter/material.dart';

/**
 * - Show a `pop up` from the bottom up with a `widget`
 * - The `context` is received from upstream. Usually from the parameters in the .build() method
 */

class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return IconButton(
      icon: const Icon(Icons.add),
      onPressed: () {
        showModalBottomSheet(
          context: context,
          builder: (bCtx) {
            // bCtx is another context. Usually do nothing with it
            return Text("hello");
          },
        );
      },
    );
  }
}
