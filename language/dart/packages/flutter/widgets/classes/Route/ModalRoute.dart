import 'package:flutter/material.dart';

// Extract arguments from ModalRoute available at the context

class MyWidget extends StatelessWidget {
  static const routeName = '/mywidget'; // must be defined in MaterialApp

  @override
  Widget build(BuildContext context) {
    // Extract the arguments from the current ModalRoute
    // settings and cast them as String
    Route? route = ModalRoute.of(context);
    RouteSettings settings = route!.settings;
    String arg = settings.arguments as String;

    return Scaffold(
      appBar: AppBar(
        title: Text(arg),
      ),
      body: Center(
        child: Text(arg),
      ),
    );
  }
}

class Main extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () {
        // When the user taps the button,
        // navigate to a named route and
        // provide the arguments as an optional
        // parameter.
        Navigator.pushNamed(
          context,
          MyWidget.routeName,
          arguments: 'This message is extracted in the build method.',
        );
      },
      child: const Text('Navigate to screen that extracts arguments'),
    );
  }
}
