import 'package:flutter/material.dart';
import 'question.dart';
import 'answer.dart';

class Quiz extends StatelessWidget {
  final Function answerHandler;
  final int questionIndex;
  final List<Map<String, Object>> questions;

  Quiz(
      {required this.answerHandler,
      required this.questions,
      required this.questionIndex});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Question(questions[questionIndex]['text'] as String),
        ...(questions[questionIndex]['answers'] as List<Map<String, Object>>)
            .map((a) =>
                Answer(() => answerHandler(a["score"]), a['text'] as String))
            .toList(),
      ],
    );
  }
}
