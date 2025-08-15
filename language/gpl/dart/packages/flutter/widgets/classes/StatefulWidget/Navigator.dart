import 'package:flutter/material.dart';

// PUSH
// the push method stacks screen over other screens

class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return IconButton(
      icon: const Icon(Icons.add),
      onPressed: () {
        // show new widget (and show a back button too)
        final Future<MyForm?> formData = Navigator.push(
          context,
          MaterialPageRoute(builder: (ctx) {
            return MyForm();
          }),
        );

        // receive value asynchronously from another screen
        formData.then((value) {
          print(value);
        });
      },
    );
  }
}

// PUSHNAMED
class MyWidget2 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return IconButton(
      icon: const Icon(Icons.add),
      onPressed: () {
        // routes must be defined in the MaterialApp widget
        Navigator.pushNamed(
          context,
          '/second',
          arguments: 'args', // args can be handled by the onGenerateRoute fn
        );
      },
    );
  }
}

// PUSHANDREMOVEUNTIL
class MyWidget3 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return IconButton(
      icon: const Icon(Icons.add),
      onPressed: () {
        // open the screen and only return back when the predicate is met
        Navigator.pushNamedAndRemoveUntil(
            context, '/second', (Route route) => true);
      },
    );
  }
}

// POP
class MyForm extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return IconButton(
      icon: const Icon(Icons.add),
      onPressed: () {
        Navigator.pop(context); // just close
        Navigator.pop(context, "myvalue"); // close and send data
        // Navigator.of(context).pop() // same
      },
    );
  }
}
