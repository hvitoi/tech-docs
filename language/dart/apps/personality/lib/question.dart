import 'package:flutter/material.dart';

class Question extends StatelessWidget {
  // all instance fields of a StatelessWidget must be final (good practice)
  final String questiontext;

  Question(this.questiontext);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity, // as much width as it can get
      margin: EdgeInsets.all(10), // 10 pixels margin around the container
      child: Text(
        questiontext,
        style: TextStyle(fontSize: 28),
        textAlign: TextAlign.center, // must be in a container to align
      ),
    );
  }
}
