import 'package:flutter/widgets.dart';

Widget main() {
  return Text(
    'Hello! How are you?',
    textAlign: TextAlign.center,
    overflow: TextOverflow.ellipsis,

    // textDirection is mandatory if trying to create a widget directly from runApp
    textDirection: TextDirection.ltr, // left to right

    // style: Theme.of(context).textTheme.titleSmall, // pick style from global
    style: TextStyle(
      fontWeight: FontWeight.bold,
      fontFamily: 'Quicksand',
      fontSize: 20,
      // color: Colors.purple,
      // color: Theme.of(context).primaryColor, // color from the global theme
    ),
  );
}
