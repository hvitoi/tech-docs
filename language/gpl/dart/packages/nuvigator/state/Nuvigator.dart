import 'package:flutter/material.dart';
import 'package:nuvigator/next.dart';

// Nuvigator.routes
// Create routes

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Nuvigator App',
      builder: Nuvigator.routes(
        screenType: materialScreenType,
        initialRoute: 'home',
        routes: [
          NuRouteBuilder(
            path: 'home',
            builder: (_, __, ___) => const Text("HomeScreen"),
          ),
          NuRouteBuilder(
            path: 'second',
            builder: (_, __, ___) => const Text("SecondScreen"),
          ),
          // Route1(), // routes can be injected here too
          // Route2(),
        ],
      ),
      // builder: Nuvigator(
      //   router: MyRouter(), // use a router instead
      // );
    );
  }
}

// Nuvigator.of
// access to the NuvigatorState

class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final nuvigator = Nuvigator.of(context);
    return IconButton(
      icon: const Icon(Icons.add),
      onPressed: () {
        nuvigator.open('second');
      },
    );
  }
}
