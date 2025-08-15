import 'package:flutter/material.dart';

/**
 * Android-style App
*/

Widget main() {
  return MaterialApp(
    title: 'Personal Expenses', // title of the app in the task manager
    home: Scaffold(appBar: AppBar(title: const Text('Home'))),
    debugShowCheckedModeBanner: false,
    theme: ThemeData.dark(),

    // stores the state of the Navigator in a global key
    // navigatorKey.current context to get the BuildContext of the Navigator widget
    navigatorKey: GlobalKey<NavigatorState>(),

    initialRoute: '/',
    routes: {
      // When navigating to the "/" route, build the Text widget.
      '/': (context) => const Text("root"),
      // When navigating to the "/second" route, build the Text widget.
      '/second': (context) => const Text("second"),
    },

    // a route generator returns a Route based on the settings provided
    // "onGenerateRoute" is used instead on "routes"
    onGenerateRoute: (RouteSettings settings) {
      // route based on the route name
      // it's triggered when invoking Navigator.pushNamed(ctx, routename)
      switch (settings.name) {
        case '/':
          if (settings.arguments != null) {/* ... */}
          return MaterialPageRoute(builder: (ctx) => const Text("root"));
        case 'second':
          return MaterialPageRoute(builder: (ctx) => const Text("second"));
        default:
          return MaterialPageRoute(builder: (ctx) => const Text("not found"));
      }
    },
  );
}
