import 'package:flutter/material.dart';

class Answer extends StatelessWidget {
  final VoidCallback AnswerHandler;
  final String answerText;

  Answer(this.AnswerHandler, this.answerText);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      child: ElevatedButton(
        child: Text(answerText),
        style: ElevatedButton.styleFrom(
          primary: Colors.purple, // background
          onPrimary: Colors.white, // foreground
        ),
        onPressed: AnswerHandler,
      ),
    );
  }
}
