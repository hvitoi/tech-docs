import 'package:flutter/material.dart';

void main() {
  ThemeData(
    // global theme
    primarySwatch: Colors.purple, // primary color/shade
    errorColor: Colors.red[900], // 900 is the weight
    fontFamily: 'Quicksand', // name from the pubspec.yaml
    textTheme: ThemeData.light()
        .textTheme
        .copyWith(button: TextStyle(color: Colors.white)),
    buttonTheme: ButtonThemeData(
      buttonColor: Colors.blueAccent[700],
      textTheme: ButtonTextTheme.primary,
    ),
    appBarTheme: const AppBarTheme(
      toolbarTextStyle: TextStyle(
        fontFamily: 'OpenSans', // default font for appbar
        fontSize: 20,
        // fontWeight: FontWeight.bold,
      ),
      titleTextStyle: TextStyle(
        fontFamily: 'OpenSans',
        fontSize: 20,
        fontWeight: FontWeight.bold,
      ),
      // textTheme: const TextTheme(
      //   headline6: TextStyle(
      //     fontFamily: 'OpenSans',
      //     fontSize: 20,
      //     fontWeight: FontWeight.bold,
      //   ),
      // ),
    ),
  );
}

/**
 * DARK
 */

void mainDark() {
  ThemeData.dark();
}
