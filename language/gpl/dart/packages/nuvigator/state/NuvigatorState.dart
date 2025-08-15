import 'package:flutter/material.dart';
import 'package:nuvigator/next.dart';

class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final NuvigatorState nuvigator = Nuvigator.of(context);
    return IconButton(
      icon: const Icon(Icons.add),
      onPressed: () {
        // open deeplink
        nuvigator.open('second');
        nuvigator.open('myapp://second'); // same

        // open deeplink with parameters
        nuvigator.open(
          'second',
          parameters: {'a': 1, 'b': 2},
        );
        nuvigator.open('myapp://second?a=1&b=2');

        // open deeplink with callback function
        nuvigator
            .open('myapp://second')
            .then((value) => print('returned value: $value'));

        // close screen with data
        nuvigator.pop('i was closed');

        // Close all screens (avoids many pops)
        nuvigator.closeFlow();
      },
    );
  }
}
