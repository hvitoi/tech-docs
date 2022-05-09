import 'package:flutter/material.dart';

/**
 * Allows changing Stateless Widgets
 */

Widget main() {
  return FutureBuilder<String>(
    // snapshot.data while the future is not yet resolved
    initialData: "I don't exist yet",

    // execute this this future first
    future: doSomething(),

    // when the result of the future is ready, build the widget
    builder: ((ctx, snapshot) {
      // snapshot contains info about the future
      switch (snapshot.connectionState) {
        case ConnectionState.none:
          // Future not yet executed
          break;
        case ConnectionState.waiting:
          // Future executed but not yet resolved
          break;
        case ConnectionState.active:
          // snapshot has a value but future is not yet completely resolved
          // good for streams
          break;
        case ConnectionState.done:
          // Future completely resolved
          break;
      }
      String myMessage = snapshot.data as String;
      return Text(myMessage);
    }),
  );
}

Future<String> doSomething() {
  return Future.value('hello');
}
