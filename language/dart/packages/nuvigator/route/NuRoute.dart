import 'package:flutter/material.dart';
import 'package:nuvigator/next.dart';

class MyArgs {
  MyArgs({
    required String name,
    required String surname,
  });

  static MyArgs fromJson(Map<String, dynamic> json) {
    return MyArgs(
      name: json['name'],
      surname: json['surname'],
    );
  }
}

// Define a new NuRoute
class MyRoute extends NuRoute<NuRouter, MyArgs, String> {
  // route path
  @override
  String get path => 'my-route';
  // String get path => 'product/screen1'; // nested route

  // set a screen type per route (different from Nuvigator.routes)
  @override
  ScreenType get screenType => materialScreenType;

  // tells to the Route who is the conversor (json <-> object)
  @override
  ParamsParser<MyArgs> get paramsParser => MyArgs.fromJson;

  // screen to render
  @override
  Widget build(BuildContext context, NuRouteSettings<MyArgs> settings) {
    // access the parameters
    // myapp://second?a=1&b=2 --> {"a": 1, "b": 2}
    Map<String, dynamic> params = settings.rawParameters;
    MyArgs args = settings.args; // raw parameters parsed into MyArgs

    return IconButton(
      icon: const Icon(Icons.add),
      onPressed: () => nuvigator.open('next-route'), // nuvigator available here
    );

    // Return a Router! (allows nested navigator)
    // return Nuvigator(
    //   router: FirstFlowRouter(),
    // );
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
