import 'package:flutter/material.dart';
import 'package:nuvigator/next.dart';

// Each route individually

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Nuvigator App',
      builder: Nuvigator.routes(
        initialRoute: 'home',
        routes: [
          NuRouteBuilder(
            path: 'home',
            builder: (_, __, NuRouteSettings settings) {
              // access the parameters
              Map<String, dynamic> params = settings.rawParameters;
              return const Text("HomeScreen");
            },
          ),
        ],
      ),
    );
  }
}
