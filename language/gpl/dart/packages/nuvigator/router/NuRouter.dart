import 'package:flutter/material.dart';
import 'package:nuvigator/next.dart';

// Define a new NuRoute
class MyRoute extends NuRoute {
  // route path
  @override
  String get path => 'my-route';

  // set a screen type per route (different from Nuvigator.routes)
  @override
  ScreenType get screenType => materialScreenType;

  // screen to render
  @override
  Widget build(BuildContext context, NuRouteSettings settings) {
    // access the parameters
    Map<String, dynamic> params = settings.rawParameters;
    return IconButton(
      icon: const Icon(Icons.add),
      onPressed: () => nuvigator.open('next-route'), // nuvigator available here
    );
  }
}

// Define your NuRouter
class MyRouter extends NuRouter {
  @override
  String get initialRoute => 'my-route';

  @override
  List<NuRoute> get registerRoutes => [
        MyRoute(),
      ];
}

// Render home just like a normal widget
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Nuvigator App',
      home: Nuvigator(
        router: MyRouter(),
      ),
    );
  }
}
