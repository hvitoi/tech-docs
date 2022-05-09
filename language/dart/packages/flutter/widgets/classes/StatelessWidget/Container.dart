import 'package:flutter/material.dart';

/**
 * - Offer rich `Style` and `alignment` options
 * - Allows 1 child only
 * - `child` < `padding` < `border` < `margin`
 * - `MediaQuery` allows fetching information about the device orientation, measures, user settings, etc
 */

Widget main() {
  return Container(
    width: double.infinity, // as much width as it can get
    height: 300,
    // height: MediaQuery.of(context).size.height * 0.6, // 60% of the screen
    margin: const EdgeInsets.symmetric(
      vertical: 10,
      horizontal: 50,
    ),
    decoration: BoxDecoration(
      border: Border.all(
        color: Colors.black,
        // color: Theme.of(context).primaryColor, // color from the global theme
        width: 2,
      ),
      color: Color.fromRGBO(220, 220, 220, 1),
      borderRadius: BorderRadius.circular(20),
    ),
    padding: const EdgeInsets.all(10), // 10 pixels margin around the container
    child: Text("hey"),
  );
}
