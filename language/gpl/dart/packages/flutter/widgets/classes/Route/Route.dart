import 'package:flutter/material.dart';

// Wraps a widget in a page with a return button

void main() {
  /**
   * Route
   */
  // Route route = ModalRoute.of(context); // get route from context
  Route route = MaterialPageRoute(
    builder: (ctx) => const Text('hello'),
  );

  /**
   * RouteSettings
   */
  RouteSettings settings = route.settings;
  Object? args = settings.arguments; // arguments passed to this route
}
