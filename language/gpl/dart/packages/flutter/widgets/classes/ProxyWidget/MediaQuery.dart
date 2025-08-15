import 'package:flutter/widgets.dart';

class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return SizedBox(
      // the full device height includes everything, including the status bar at the top
      height: (MediaQuery.of(context).size.height - /* full device size*/
              MediaQuery.of(context).padding.top) * /* status bar size */
          0.7, // get 70% of that size
      child: Text("hey"),
    );
  }
}
