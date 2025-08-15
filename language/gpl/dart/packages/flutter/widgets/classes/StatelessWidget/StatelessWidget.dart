import 'dart:async';

import 'package:flutter/widgets.dart';

class MyWidget extends StatelessWidget {
  String _txt; // private attribute
  String iAmRequired; // required attribute
  String? iAmOptional; // optional attribute

  // Positional Parameters
  MyWidget(
      this._txt, this.iAmRequired, this.iAmOptional, String? createdOnTheFly,
      {Key? key})
      : super(key: key);

  // Named Parameters
  MyWidget.secondConstructor(this._txt, // named parameters can't be private
      {required this.iAmRequired,
      this.iAmOptional,
      String? createdOnTheFly});

  @override
  Widget build(BuildContext context) {
    return Text(_txt);
  }
}

void main() {
  MyWidget("blabla", "required", "optional", "onthefly");
  MyWidget.secondConstructor(
    "blabla",
    iAmRequired: "required",
    iAmOptional: "optional",
    createdOnTheFly: "onthefly",
  );
}
