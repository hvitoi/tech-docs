import 'package:flutter/material.dart';

/**
 * Receives user input
 */

class MyWidget extends StatefulWidget {
  @override
  State<MyWidget> createState() => _MyWidgetState();
}

class _MyWidgetState extends State<MyWidget> {
  // controller connects the controller with the text field  (listens and saves user input)
  // works good only on StatefulWidgets! (State)
  final TextEditingController _controller = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return TextField(
      keyboardType: TextInputType.number, // numeric keyboard
      obscureText: true, // do not show the content (good for passwords)
      maxLength: 15,

      controller: _controller,

      decoration: InputDecoration(
        icon: Icon(Icons.monetization_on),
        border: OutlineInputBorder(),
        labelText: 'Password',
      ),
      style: TextStyle(
        fontSize: 16.0,
        letterSpacing: 24,
      ),
      textAlign: TextAlign.center,

      onChanged: (val) {
        print(val);
      },

      // For the keyboard "enter". Good for validations
      onSubmitted: (val) {
        print(_controller.text);
      },
    );
  }
}
